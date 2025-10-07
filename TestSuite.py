import unittest
from TestUtils import TestUtils


class TestSymbolTable(unittest.TestCase):
    #test_0 → test_3: Ten bien hop le, cac ky tu chu thuong, so, _ — phai "success"
    def test_0(self):
        input = ["INSERT m number"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 10000))

    def test_1(self):
        input = ["INSERT hK_3 string"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 10001))
      
    def test_2(self):
        input = ["INSERT Q string"]
        expected = ["Invalid: INSERT Q string"]
        self.assertTrue(TestUtils.check(input, expected, 10002))

    def test_3(self):
        input = ["INSERT hkM7_ string"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 10003))

    #test_4 → test_7: Ten bien khong hop le (chua @, thieu ten) — "Invalid"

    def test_4(self):
        input = ["INSERT kk@e number"]
        expected = ["Invalid: INSERT kk@e number"]
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

    #test_8: Kiem tra trung ten trong cung scope — "Redeclared"

    def test_8(self):
        input = ["INSERT phanhoang number", "INSERT phan number", "INSERT phanh number", "INSERT phanhoangk number", "INSERT phan number", "INSERT phanhoang number"]
        expected = ["Redeclared: INSERT phan number"]
        self.assertTrue(TestUtils.check(input, expected, 10008))
        
    # test_9: Gan so cho bien kieu number — hop le

    # test_10: Gan float (12.2) — "Invalid"

    # test_11 → test_13: Gan chuoi hop le cho bien kieu string

    # test_14 → test_15: Chuoi khong hop le (ky tu dac biet ~, space) — "Invalid"

    # test_16 → test_20: Gan gia tri tu ten bien khong hop le — "Invalid"


    def test_9(self):
        input = ["INSERT k number", "ASSIGN k 224"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10009))

    def test_10(self):
        input = ["INSERT l number", "ASSIGN l 15.9"]
        expected = ["Invalid: ASSIGN l 15.9"]
        self.assertTrue(TestUtils.check(input, expected, 10010))

    def test_11(self):
        input = ["INSERT u string", "ASSIGN u '8ak'"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10011))

    def test_12(self):
        input = ["INSERT u string", "ASSIGN u '7aP'"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10012))

    def test_13(self):
        input = ["INSERT o string", "ASSIGN o 'abcAB01'"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10013))

    def test_14(self):
        input = ["INSERT i string", "ASSIGN i 'u~u'"]
        expected = ["Invalid: ASSIGN i 'u~u'"]
        self.assertTrue(TestUtils.check(input, expected, 10014))

    def test_15(self):
        input = ["INSERT y string", "ASSIGN y 'p p'"]
        expected = ["Invalid: ASSIGN y 'p p'"]
        self.assertTrue(TestUtils.check(input, expected, 10015))

    def test_16(self):
        input = ["ASSIGN _o 8"]
        expected = ["Invalid: ASSIGN _o 8"]
        self.assertTrue(TestUtils.check(input, expected, 10016))

    def test_17(self):
        input = ["ASSIGN kki~d 7"]
        expected = ["Invalid: ASSIGN kki~d 7"]
        self.assertTrue(TestUtils.check(input, expected, 10017))

    def test_18(self):
        input = ["INSERT v string", "ASSIGN v K"]
        expected = ["Invalid: ASSIGN v K"]
        self.assertTrue(TestUtils.check(input, expected, 10018))

    def test_19(self):
        input = ["INSERT k number", "ASSIGN k B"]
        expected = ["Invalid: ASSIGN k B"]
        self.assertTrue(TestUtils.check(input, expected, 10019))

    def test_20(self):
        input = ["INSERT h string", "ASSIGN h _"]
        expected = ["Invalid: ASSIGN h _"]
        self.assertTrue(TestUtils.check(input, expected, 10020))
    # test_21: Bien number chua khai bao — "Undeclared"

    # test_22: Gan bang 1 bien chua khai bao — "Undeclared"

    def test_21(self):
        input = ["ASSIGN number 'number'"]
        expected = ["Undeclared: ASSIGN number 'number'"]
        self.assertTrue(TestUtils.check(input, expected, 10021))

    def test_22(self):
        input = ["INSERT i string", "ASSIGN i k_"]
        expected = ["Undeclared: ASSIGN i k_"]
        self.assertTrue(TestUtils.check(input, expected, 10022))

    #test_23 → test_25: Lenh gan thieu doi so — "Invalid"

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

    # test_26: BEGIN - END dung — hop le

    # test_27 → test_30: END vo nghia, END thua — "UnknownBlock"

    # test_31: Gan bien chua ton tai trong scope hien tai — "Undeclared"

    def test_26(self):
        input = ["BEGIN", "END"]
        expected = []
        self.assertTrue(TestUtils.check(input, expected, 10026))

    def test_27(self):
        input = ["END"]
        expected = ["UnknownBlock"]
        self.assertTrue(TestUtils.check(input, expected, 10027))

    def test_28(self):
        input = ["BEGIN", "INSERT p number", "BEGIN", "INSERT g number", "END", "END", "END"]
        expected = ["UnknownBlock"]
        self.assertTrue(TestUtils.check(input, expected, 10028))

    def test_29(self):
        input = ["BEGIN", "INSERT m number", "END", "END", "BEGIN"]
        expected = ["UnknownBlock"]
        self.assertTrue(TestUtils.check(input, expected, 10029))

    def test_30(self):
        input = ["BEGIN", "INSERT n number", "BEGIN", "END", "END", "END", "BEGIN"]
        expected = ["UnknownBlock"]
        self.assertTrue(TestUtils.check(input, expected, 10030))

    def test_31(self):
        input = ["BEGIN", "INSERT k number", "ASSIGN z 7", "INSERT k number", "INSERT z number", "END"]
        expected = ["Undeclared: ASSIGN z 7"]
        self.assertTrue(TestUtils.check(input, expected, 10031))

    # test_32 → test_33: Bien chua khai bao — "Undeclared"

    # test_34: Lenh khong co doi so — "Invalid"

    # test_35: Lookup sau END — phai tra ve dung scope — "0"

    def test_32(self):
        input = ["LOOKUP kW7"]
        expected = ["Undeclared: LOOKUP kW7"]
        self.assertTrue(TestUtils.check(input, expected, 10032))

    def test_33(self):
        input = ["LOOKUP kW_8"]
        expected = ["Undeclared: LOOKUP kW_8"]
        self.assertTrue(TestUtils.check(input, expected, 10033))

    def test_34(self):
        input = ["LOOKUP "]
        expected = ["Invalid: LOOKUP "]
        self.assertTrue(TestUtils.check(input, expected, 10034))

    def test_35(self):
        input = ["BEGIN", "INSERT p number", "END", "INSERT p number", "BEGIN", "INSERT p number", "END", "LOOKUP p"]
        expected = ["success", "success", "success", "0"]
        self.assertTrue(TestUtils.check(input, expected, 10035))

    # test_36: PRINT khong co bien — ""

    # test_37: PRINT co them space — "Invalid"

    # test_38 → test_40: In ra bien trong scope — dung format name//level


    def test_36(self):
        input = ["PRINT"]
        expected = [""]
        self.assertTrue(TestUtils.check(input, expected, 10036))

    def test_37(self):
        input = ["PRINT "]
        expected = ["Invalid: PRINT "]
        self.assertTrue(TestUtils.check(input, expected, 10037))

    def test_38(self):
        input = ["INSERT h string", "INSERT j string", "BEGIN", "INSERT h string", "INSERT j string", "PRINT", "END"]
        expected = ["success", "success", "success", "success", "h//1 j//1"]
        self.assertTrue(TestUtils.check(input, expected, 10038))

    def test_39(self):
        input = ["INSERT o string", "INSERT m string", "INSERT n string", "BEGIN", "INSERT m string", "BEGIN", "PRINT", "INSERT o string", "END", "END"]
        expected = ["success", "success", "success", "success", "o//0 n//0 m//1", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10039))

    def test_40(self):
        input = ["INSERT z string", "INSERT x string", "INSERT y string", "BEGIN", "INSERT x string", "BEGIN", "INSERT y string", "INSERT z string", "PRINT", "END", "END"]
        expected = ["success", "success", "success", "success", "success", "success", "x//1 y//2 z//2"]
        self.assertTrue(TestUtils.check(input, expected, 10040))

    #test_41: RPRINT khong co bien — ""

    #test_42 → test_45: RPRINT in bien nguoc thu tu khai bao — dung format

    def test_41(self):
        input = ["RPRINT"]
        expected = [""]
        self.assertTrue(TestUtils.check(input, expected, 10041))

    def test_42(self):
        input = ["INSERT k string", "INSERT m string", "BEGIN", "INSERT k string", "INSERT m string", "RPRINT", "END"]
        expected = ["success", "success", "success", "success", "m//1 k//1"]
        self.assertTrue(TestUtils.check(input, expected, 10042))

    def test_43(self):
        input = ["RPRINT", "INSERT r string", "INSERT s string", "BEGIN", "INSERT r string", "INSERT s string", "END"]
        expected = ["", "success", "success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10043))

    def test_44(self):
        input = ["RPRINT", "INSERT t string", "INSERT u string", "BEGIN", "INSERT t string", "INSERT u string", "END"]
        expected = ["", "success", "success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10044))

    def test_45(self):
        input = ["INSERT g string", "INSERT h string", "INSERT y string", "BEGIN", "INSERT h string", "BEGIN", "INSERT y string", "INSERT g string", "RPRINT", "END", "END"]
        expected = ["success", "success", "success", "success", "success", "success", "g//2 y//2 h//1"]
        self.assertTrue(TestUtils.check(input, expected, 10045))
    
    #test_46 → test_49: Lenh rong / chi co dau cach — "Invalid"

    def test_46(self):
        input = [""]
        expected = ["Invalid: "]
        self.assertTrue(TestUtils.check(input, expected, 10046))

    def test_47(self):
        input = [" "]
        expected = ["Invalid:  "]
        self.assertTrue(TestUtils.check(input, expected, 10047))

    def test_48(self):
        input = ["INSERT k number", "  "]
        expected = ["Invalid:   "]
        self.assertTrue(TestUtils.check(input, expected, 10048))

    def test_49(self):
        input = ["INSERT s number", "   "]
        expected = ["Invalid:    "]
        self.assertTrue(TestUtils.check(input, expected, 10049))