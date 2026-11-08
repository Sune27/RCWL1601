import sys, copy
sys.stdout.reconfigure(encoding="utf-8")
from docx import Document
from docx.shared import Cm
from docx.enum.table import WD_ROW_HEIGHT_RULE, WD_ALIGN_VERTICAL
from docx.text.run import Run

p = r"c:\Users\ADMIN\Documents\Tài liệu học tập slide hoặc sách tài liệu\Phần chữa bài tập của nhiều môn\Đo lường & cảm biến\RCWL1601\Bao_Cao_Thuc_Nghiem_RCWL1601.docx"
doc = Document(p)
t = doc.tables[0]
cell = t.cell(0, 0)
para = cell.paragraphs[7]
runs = para.runs
idx = [i for i, r in enumerate(runs) if r.text == "\tMSSV: [Điền MSSV 3]"][0]
anchor = runs[idx]._r
for k in (4, 5):
    new = copy.deepcopy(runs[idx]._r)
    anchor.addnext(new)
    anchor = new
    Run(new, para).text = f"\n  {k}. [Họ và tên Sinh viên {k}]\t-\tMSSV: [Điền MSSV {k}]"

row = t.rows[0]
row.height = Cm(24.8)
row.height_rule = WD_ROW_HEIGHT_RULE.EXACTLY
cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
doc.save(p)
print("saved")
