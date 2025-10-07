class StaticError(Exception):
    pass


class InvalidInstruction(StaticError):
    def __init__(self, instruction):
        super().__init__(f"Invalid: {instruction}")


class TypeMismatch(StaticError):
    def __init__(self, instruction):
        super().__init__(f"TypeMismatch: {instruction}")


class Undeclared(StaticError):
    def __init__(self, instruction):
        super().__init__(f"Undeclared: {instruction}")


class Redeclared(StaticError):
    def __init__(self, instruction):
        super().__init__(f"Redeclared: {instruction}")


class InvalidDeclaration(StaticError):
    def __init__(self, instruction):
        super().__init__(f"InvalidDeclaration: {instruction}")


class UnclosedBlock(StaticError):
    def __init__(self, level):
        super().__init__(f"UnclosedBlock: {level}")


class UnknownBlock(StaticError):
    def __init__(self):
        super().__init__("UnknownBlock")


class Overflow(StaticError):
    def __init__(self, instruction):
        super().__init__(f"Overflow: {instruction}")


class TypeCannotBeInferred(StaticError):
    def __init__(self, instruction):
        super().__init__(f"TypeCannotBeInferred: {instruction}")
