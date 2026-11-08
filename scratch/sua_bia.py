import sys
sys.stdout.reconfigure(encoding="utf-8")
p = r"c:\Users\ADMIN\Documents\Tài liệu học tập slide hoặc sách tài liệu\Phần chữa bài tập của nhiều môn\Đo lường & cảm biến\RCWL1601\xuat_word_chuan.py"
s = open(p, encoding="utf-8", newline="").read()
nl = "\r\n" if "\r\n" in s else "\n"

a = "cover_cell.width = Cm(16.0)" + nl
b = a + (
    "# Khung bìa bao toàn bộ vùng in của trang (cao 25.7 cm, trừ phần cho đoạn ngắt trang phía sau)" + nl +
    "cover_row = cover_table.rows[0]" + nl +
    "cover_row.height = Cm(24.8)" + nl +
    "cover_row.height_rule = WD_ROW_HEIGHT_RULE.EXACTLY" + nl +
    "cover_cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER" + nl)
assert s.count(a) == 1
s = s.replace(a, b)

c = 'p_info.add_run("  3. [Họ và tên Sinh viên 3]\\t-\\tMSSV: [Điền MSSV 3]\\n")' + nl
d = c + (
    'p_info.add_run("  4. [Họ và tên Sinh viên 4]\\t-\\tMSSV: [Điền MSSV 4]\\n")' + nl +
    'p_info.add_run("  5. [Họ và tên Sinh viên 5]\\t-\\tMSSV: [Điền MSSV 5]\\n")' + nl)
assert s.count(c) == 1
s = s.replace(c, d)

e = "from docx.enum.table import WD_TABLE_ALIGNMENT"
assert s.count(e) == 1
s = s.replace(e, "from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ROW_HEIGHT_RULE, WD_ALIGN_VERTICAL")
open(p, "w", encoding="utf-8", newline="").write(s)
print("ok")
