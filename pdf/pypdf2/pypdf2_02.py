# ファイルの途中挿入


import PyPDF2
import glob

pdf_path = 'out_pdf/'

merger = PyPDF2.PdfFileMerger()

# 大元のファイル指定
merger.append('merge1.pdf')


# 第一引数：どこの位置に差し込むか
#　第二引数：なんのファイルを差し込むか
#　第三引数：なんのファイルのどのページを差し込むか
merger.merge(3, pdf_path + 'page01.pdf',pages=(3,5))

merger.write('insert.pdf')
merger.close()
