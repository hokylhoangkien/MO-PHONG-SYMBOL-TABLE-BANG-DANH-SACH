import unittest
from TestUtils import TestUtils


class TestSymbolTable(unittest.TestCase):
    # test_0 → test_3: Tên biến hợp lệ — "success"
    def test_0(self):
        input = ["INSERT a_1 number"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 10000))

    def test_1(self):
        input = ["INSERT nK_9 string"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 10001))

    def test_2(self):
        input = ["INSERT Z string"]
        expected = ["Invalid: INSERT Z string"]
        self.assertTrue(TestUtils.check(input, expected, 10002))

    def test_3(self):
        input = ["INSERT abC_8 string"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 10003))

    # test_4 → test_7: Tên biến không hợp lệ — "Invalid"
    def test_4(self):
        input = ["INSERT aa@b number"]
        expected = ["Invalid: INSERT aa@b number"]
        self.assertTrue(TestUtils.check(input, expected, 10004))

    def test_5(self):
        input = ["INSERT  number"]
        expected = ["Invalid: INSERT  number"]
        self.assertTrue(TestUtils.check(input, expected, 10005))

    def test_6(self):
        input = ["INSERT  "]
        expected = ["Invalid: INSERT  "]
        self.assertTrue(TestUtils.check(input, expected, 10006))

    def test_7(self):
        input = ["INSERT "]
        expected = ["Invalid: INSERT "]
        self.assertTrue(TestUtils.check(input, expected, 10007))

    # test_8: Trùng tên trong cùng scope — "Redeclared"
    def test_8(self):
        input = [
            "INSERT alpha number",
            "INSERT beta number",
            "INSERT gamma number",
            "INSERT delta number",
            "INSERT beta number",
            "INSERT alpha number",
        ]
        expected = ["Redeclared: INSERT beta number"]
        self.assertTrue(TestUtils.check(input, expected, 10008))

    # test_9: Gán số cho number — hợp lệ
    def test_9(self):
        input = ["INSERT c number", "ASSIGN c 123"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10009))

    # test_10: Gán float — "Invalid"
    def test_10(self):
        input = ["INSERT d number", "ASSIGN d 45.7"]
        expected = ["Invalid: ASSIGN d 45.7"]
        self.assertTrue(TestUtils.check(input, expected, 10010))

    # test_11 → test_13: Gán chuỗi hợp lệ cho string
    def test_11(self):
        input = ["INSERT name string", "ASSIGN name 'abc'"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10011))

    def test_12(self):
        input = ["INSERT text string", "ASSIGN text 'Hi09'"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10012))

    def test_13(self):
        input = ["INSERT msg string", "ASSIGN msg 'helloWORLD1'"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10013))

    # test_14 → test_15: Chuỗi không hợp lệ — "Invalid"
    def test_14(self):
        input = ["INSERT x string", "ASSIGN x 'a~a'"]
        expected = ["Invalid: ASSIGN x 'a~a'"]
        self.assertTrue(TestUtils.check(input, expected, 10014))

    def test_15(self):
        input = ["INSERT y string", "ASSIGN y 'bad name'"]
        expected = ["Invalid: ASSIGN y 'bad name'"]
        self.assertTrue(TestUtils.check(input, expected, 10015))

    # test_16 → test_20: Tên biến không hợp lệ khi gán
    def test_16(self):
        input = ["ASSIGN _temp 5"]
        expected = ["Invalid: ASSIGN _temp 5"]
        self.assertTrue(TestUtils.check(input, expected, 10016))

    def test_17(self):
        input = ["ASSIGN inv@lid 10"]
        expected = ["Invalid: ASSIGN inv@lid 10"]
        self.assertTrue(TestUtils.check(input, expected, 10017))

    def test_18(self):
        input = ["INSERT str string", "ASSIGN str V"]
        expected = ["Invalid: ASSIGN str V"]
        self.assertTrue(TestUtils.check(input, expected, 10018))

    def test_19(self):
        input = ["INSERT num number", "ASSIGN num X"]
        expected = ["Invalid: ASSIGN num X"]
        self.assertTrue(TestUtils.check(input, expected, 10019))

    def test_20(self):
        input = ["INSERT h string", "ASSIGN h _"]
        expected = ["Invalid: ASSIGN h _"]
        self.assertTrue(TestUtils.check(input, expected, 10020))

    # test_21 → test_22: Biến chưa khai báo — "Undeclared"
    def test_21(self):
        input = ["ASSIGN value 9"]
        expected = ["Undeclared: ASSIGN value 9"]
        self.assertTrue(TestUtils.check(input, expected, 10021))

    def test_22(self):
        input = ["INSERT s string", "ASSIGN s not_exist"]
        expected = ["Undeclared: ASSIGN s not_exist"]
        self.assertTrue(TestUtils.check(input, expected, 10022))

    # test_23 → test_25: Lệnh gán thiếu đối số — "Invalid"
    def test_23(self):
        input = ["INSERT a number", "INSERT b string", "ASSIGN c 2 "]
        expected = ["Invalid: ASSIGN c 2 "]
        self.assertTrue(TestUtils.check(input, expected, 10023))

    def test_24(self):
        input = ["INSERT a number", "INSERT b string", "ASSIGN c"]
        expected = ["Invalid: ASSIGN c"]
        self.assertTrue(TestUtils.check(input, expected, 10024))

    def test_25(self):
        input = ["INSERT a number", "INSERT b string", "ASSIGN"]
        expected = ["Invalid: ASSIGN"]
        self.assertTrue(TestUtils.check(input, expected, 10025))

    # test_26 → test_30: BEGIN/END logic
    def test_26(self):
        input = ["BEGIN", "END"]
        expected = []
        self.assertTrue(TestUtils.check(input, expected, 10026))

    def test_27(self):
        input = ["END"]
        expected = ["UnknownBlock"]
        self.assertTrue(TestUtils.check(input, expected, 10027))

    def test_28(self):
        input = ["BEGIN", "INSERT a number", "BEGIN", "INSERT b number", "END", "END", "END"]
        expected = ["UnknownBlock"]
        self.assertTrue(TestUtils.check(input, expected, 10028))

    def test_29(self):
        input = ["BEGIN", "INSERT n number", "END", "END", "BEGIN"]
        expected = ["UnknownBlock"]
        self.assertTrue(TestUtils.check(input, expected, 10029))

    def test_30(self):
        input = ["BEGIN", "INSERT x number", "BEGIN", "END", "END", "END"]
        expected = ["UnknownBlock"]
        self.assertTrue(TestUtils.check(input, expected, 10030))

    # test_31: Gán biến chưa khai báo trong scope
    def test_31(self):
        input = ["BEGIN", "INSERT a number", "ASSIGN z 10", "INSERT z number", "END"]
        expected = ["Undeclared: ASSIGN z 10"]
        self.assertTrue(TestUtils.check(input, expected, 10031))

    # test_32 → test_33: LOOKUP biến chưa khai báo
    def test_32(self):
        input = ["LOOKUP notfound1"]
        expected = ["Undeclared: LOOKUP notfound1"]
        self.assertTrue(TestUtils.check(input, expected, 10032))

    def test_33(self):
        input = ["LOOKUP notfound_2"]
        expected = ["Undeclared: LOOKUP notfound_2"]
        self.assertTrue(TestUtils.check(input, expected, 10033))

    # test_34: LOOKUP thiếu đối số
    def test_34(self):
        input = ["LOOKUP "]
        expected = ["Invalid: LOOKUP "]
        self.assertTrue(TestUtils.check(input, expected, 10034))

    # test_35: LOOKUP sau END
    def test_35(self):
        input = ["BEGIN", "INSERT var number", "END", "INSERT var number", "BEGIN", "INSERT var number", "END", "LOOKUP var"]
        expected = ["success", "success", "success", "0"]
        self.assertTrue(TestUtils.check(input, expected, 10035))

    # test_36 → test_40: PRINT
    def test_36(self):
        input = ["PRINT"]
        expected = [""]
        self.assertTrue(TestUtils.check(input, expected, 10036))

    def test_37(self):
        input = ["PRINT "]
        expected = ["Invalid: PRINT "]
        self.assertTrue(TestUtils.check(input, expected, 10037))

    def test_38(self):
        input = ["INSERT a string", "INSERT b string", "BEGIN", "INSERT a string", "INSERT b string", "PRINT", "END"]
        expected = ["success", "success", "success", "success", "a//1 b//1"]
        self.assertTrue(TestUtils.check(input, expected, 10038))

    def test_39(self):
        input = ["INSERT o string", "INSERT m string", "INSERT n string", "BEGIN", "INSERT m string", "BEGIN", "PRINT", "INSERT o string", "END", "END"]
        expected = ["success", "success", "success", "success", "o//0 n//0 m//1", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10039))

    def test_40(self):
        input = ["INSERT m string", "INSERT n string", "INSERT o string", "BEGIN", "INSERT n string", "BEGIN", "INSERT o string", "INSERT m string", "PRINT", "END", "END"]
        expected = ["success", "success", "success", "success", "success", "success", "n//1 o//2 m//2"]
        self.assertTrue(TestUtils.check(input, expected, 10040))

    # test_41 → test_45: RPRINT
    def test_41(self):
        input = ["RPRINT"]
        expected = [""]
        self.assertTrue(TestUtils.check(input, expected, 10041))

    def test_42(self):
        input = ["INSERT a string", "INSERT b string", "BEGIN", "INSERT a string", "INSERT b string", "RPRINT", "END"]
        expected = ["success", "success", "success", "success", "b//1 a//1"]
        self.assertTrue(TestUtils.check(input, expected, 10042))

    def test_43(self):
        input = ["RPRINT", "INSERT c string", "INSERT d string", "BEGIN", "INSERT c string", "INSERT d string", "END"]
        expected = ["", "success", "success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10043))

    def test_44(self):
        input = ["RPRINT", "INSERT e string", "INSERT f string", "BEGIN", "INSERT e string", "INSERT f string", "END"]
        expected = ["", "success", "success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10044))

    def test_45(self):
        input = ["INSERT g string", "INSERT h string", "INSERT i string", "BEGIN", "INSERT h string", "BEGIN", "INSERT i string", "INSERT g string", "RPRINT", "END", "END"]
        expected = ["success", "success", "success", "success", "success", "success", "g//2 i//2 h//1"]
        self.assertTrue(TestUtils.check(input, expected, 10045))

    # test_46 → test_49: Lệnh rỗng — "Invalid"
    def test_46(self):
        input = [""]
        expected = ["Invalid: "]
        self.assertTrue(TestUtils.check(input, expected, 10046))

    def test_47(self):
        input = [" "]
        expected = ["Invalid:  "]
        self.assertTrue(TestUtils.check(input, expected, 10047))

    def test_48(self):
        input = ["INSERT a number", "  "]
        expected = ["Invalid:   "]
        self.assertTrue(TestUtils.check(input, expected, 10048))

    def test_49(self):
        input = ["INSERT b number", "   "]
        expected = ["Invalid:    "]
        self.assertTrue(TestUtils.check(input, expected, 10049))
