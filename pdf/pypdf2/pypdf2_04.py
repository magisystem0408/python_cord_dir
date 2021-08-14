import PyPDF2
import glob

# ファイルを分割する

src_path = 'merge1.pdf'

merger1 =PyPDF2.PdfFileMerger()
merger2 =PyPDF2.PdfFileMerger()



merger1.append(src_path,pages=(0,2))
merger2.append(src_path,pages=(2,5))


merger1.write('splite1.pdf')
merger2.write('splite2.pdf')

merger1.close()
merger2.close()