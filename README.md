# Symbol Table Simulation

Phiên bản: 1.0

---

## 📝 Mô tả dự án

Dự án này mô phỏng một **bảng ghi đối tượng (Symbol Table)**, cấu trúc dữ liệu quan trọng trong các trình biên dịch, dùng để lưu thông tin về biến (identifier), kiểu dữ liệu, và phạm vi (scope).

Hỗ trợ các thao tác:

- **INSERT**: Thêm biến mới.
- **ASSIGN**: Gán giá trị cho biến.
- **LOOKUP**: Tra cứu mức scope của biến.
- **PRINT / RPRINT**: In danh sách biến theo thứ tự khai báo hoặc ngược lại.
- **BEGIN / END**: Mở và đóng block (scope) tương tự `{}` trong C/C++.

Chương trình viết **hoàn toàn theo lập trình hàm (functional programming)**, dùng danh sách và hàm bậc cao.

---

## ⚡ Các lỗi ngữ nghĩa

- `Undeclared`: Biến chưa khai báo.
- `Redeclared`: Biến khai báo lại trong cùng scope.
- `TypeMismatch`: Gán giá trị không phù hợp kiểu.
- `UnclosedBlock`: Khối chưa đóng.
- `UnknownBlock`: Đóng block không tồn tại.
- `InvalidInstruction`: Lệnh sai định dạng.

---

## 🛠 Công nghệ

- Python 3
- Module: `functools`
- Module tự viết: `StaticError`, `Symbol`

Không sử dụng thư viện nào khác.

---

## 🌱 Mục tiêu học tập

- Thực hành lập trình hàm (functional programming).
- Sử dụng **hàm bậc cao** và thao tác với danh sách.
- Quản lý **symbol table** và kiểm tra lỗi ngữ nghĩa.

---

## 🛠 Cài đặt và chạy

1. **Tải mã nguồn**: Lấy toàn bộ các file Python (`main.py`, `SymbolTable.py`, `Symbol.py`, `StaticError.py`, `TestSuite.py`, `TestUtils.py`) và đặt vào cùng một thư mục.

2. **Chuẩn bị môi trường**:

   - Cài Python 3 ([https://www.python.org/downloads/](https://www.python.org/downloads/))
   - Không cần cài thêm thư viện ngoài.

3. **Chạy chương trình chính**:

```bash
py main.py
```

**Lưu ý:** Kể từ lần chạy đầu tiên, muốn chạy lại thì phải xóa các thư mục: (`testcase`, `_pycache_`) trước mỗi lần chạy sau đó.
