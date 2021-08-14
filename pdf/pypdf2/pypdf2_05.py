import PyPDF2
import glob


src_path ='merge1.pdf'
out_path ='rotate.pdf'


# 回転角度
rotate_angle =180

# 対象ファイル取得
reader =PyPDF2.PdfFileReader(src_path)
writer =PyPDF2.PdfFileWriter()


for i in range(reader.getNumPages()):
    page =reader.getPage(i)
    # 回転処理
    page.rotateCLockwise(rotate_angle)
    writer.addPage(page)

with open(out_path,mode="wb")as f:
    writer.write(f)
