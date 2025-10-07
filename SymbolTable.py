from StaticError import *
from Symbol import *
from functools import *

def simulate(list_of_commands):
    # kiem tra thu ten bien co hop le hay khong
    def is_identifier(s):
        return bool(s) and s[0].islower() and all(c.isalnum() or c == '_' for c in s)

    # phan tich no ra
    def parse_value(v):
        return ('number', v) if v.isdigit() else \
               ('string', v[1:-1]) if v.startswith("'") and v.endswith("'") and len(v) >= 2 and (v[1:-1].isalnum() or v[1:-1] == '') else \
               ('id', v) if is_identifier(v) else (None, None)

    # kiem thong tin bien trong scopes roi sau do minh tra ve (level, type)
    def do_lookup(scopes, name):
        matches = [(len(scopes) - 1 - i, sym.typ)
                   for i, sc in enumerate(scopes)
                   for sym in sc if sym.name == name]
        if not matches:
            raise Undeclared(f"LOOKUP {name}")
        return matches[0]

    # tra ve cac bien con hieu luc trong level hien tai
    def active(history, lvl):
        return list(filter(
            lambda h: h[1] <= lvl and not any(h2[0] == h[0] and h2[1] > h[1] for h2 in history),
            history
        ))

    #de quy xu ly tung lenh
    def rec(cmds, scopes, history, counter, lvl):
        return [] if not cmds and lvl == 0 else (
            (_raise(UnclosedBlock(lvl)) if lvl != 0 else [])
            if not cmds else
            _handle(cmds[0], cmds[1:], scopes, history, counter, lvl)
        )

    #giup raise loi
    def _raise(e): raise e

    # xu ly tung loai lenh insert,...
    def _handle(cmd, rest_cmds, scopes, history, counter, lvl):
        parts = cmd.split(' ')
        if cmd == 'BEGIN':
            # bat dau scope moi
            return rec(rest_cmds, [[]] + scopes, history, counter, lvl + 1)
        if cmd == 'END':
            # ket thuc scope, kiem tra neu END vo nghia
            return _raise(UnknownBlock()) if lvl == 0 else rec(
                rest_cmds,
                scopes[1:],
                list(filter(lambda x: x[1] != lvl, history)),
                counter,
                lvl - 1
            )
        if parts[0] == 'INSERT' and len(parts) == 3:
            name, typ = parts[1], parts[2]
            return _raise(InvalidInstruction(cmd)) if not is_identifier(name) or typ not in ['number', 'string'] else (
                _raise(Redeclared(cmd)) if any(sym.name == name for sym in scopes[0]) else
                ['success'] + rec(
                    rest_cmds,
                    [[Symbol(name, typ)] + scopes[0]] + scopes[1:],
                    history + [(name, lvl, counter)],
                    counter + 1,
                    lvl
                )
            )
        if parts[0] == 'ASSIGN' and len(parts) == 3 and is_identifier(parts[1]):
            name, val = parts[1], parts[2]
            return _assign(cmd, name, val, rest_cmds, scopes, history, counter, lvl)
        if parts[0] == 'LOOKUP' and len(parts) == 2 and is_identifier(parts[1]):
            level, _ = do_lookup(scopes, parts[1])
            return [str(level)] + rec(rest_cmds, scopes, history, counter, lvl)
        if cmd == 'PRINT':
            # in cac bien theo thu tu khai bao
            return [_print_output(active(history, lvl))] + rec(rest_cmds, scopes, history, counter, lvl)
        if cmd == 'RPRINT':
            # in cac bien theo thu tu nguoc
            return [_print_output(list(reversed(active(history, lvl))))] + rec(rest_cmds, scopes, history, counter, lvl)
        return _raise(InvalidInstruction(cmd))

    # xu ly lenh assi
    def _assign(cmd, name, val, rest_cmds, scopes, history, counter, lvl):
        try:
            _, decl_type = do_lookup(scopes, name)
        except Undeclared:
            raise Undeclared(f"ASSIGN {name} {val}")
        vtype, vval = parse_value(val)
        if vtype is None:
            raise InvalidInstruction(cmd)
        if vtype == 'id':
            try:
                _, source_type = do_lookup(scopes, vval)
            except Undeclared:
                raise Undeclared(f"ASSIGN {name} {val}")
            if decl_type != source_type:
                raise TypeMismatch(cmd)
        else:
            if decl_type != vtype:
                raise TypeMismatch(cmd)
        return ['success'] + rec(rest_cmds, scopes, history, counter, lvl)

    # in danh sach bien theo format ten//level
    def _print_output(lst):
        return reduce(
            lambda acc, x: acc + (' ' if acc else '') + x[0] + '//' + str(x[1]),
            lst,
            ''
        )

    return rec(list_of_commands, [[]], [], 0, 0)
