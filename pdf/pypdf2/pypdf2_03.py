# あるpdfに別のpdfを重ねる
import PyPDF2
import glob

pdf_path = 'out_pdf/'

file_1 = pdf_path + 'page00.pdf'
file_2 = pdf_path + 'page04.pdf'
output_file ='output.pdf'




#ココカラ合成処理。

# 大元指定
pdf_file_1 =PyPDF2.PdfFileReader(file_1)
pdf1_page =pdf_file_1.getPage(0)

pdf_file_2 =PyPDF2.PdfFileReader(file_2)

#ここでマージする
pdf1_page.mergePage(pdf_file_2.getPage(0))


output =PyPDF2.PdfFileWriter()
output.addPage(pdf1_page)


# 出力処理
out_pdf =open(output_file,'wb')
output.write(out_pdf)
out_pdf.close()



