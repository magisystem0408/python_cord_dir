import PyPDF2

# ファイルの連結

# 全てのファイルを参照したい
import glob

pdf_path ='out_pdf/'

merger=PyPDF2.PdfFileMerger()


#全てのファイルを結合する
pdf_list =sorted(glob.glob(pdf_path+'*.pdf'))

for f in pdf_list:
    merger.append(f)


#ファイルの連結
# merger.append(pdf_path+"page01.pdf")
# merger.append(pdf_path+"page02.pdf")


# 出力
merger.write('merge1.pdf')

merger.close()