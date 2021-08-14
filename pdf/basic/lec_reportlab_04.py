from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont


##改行ページ

pdf_canvas =canvas.Canvas('sample.pdf')
pdf_canvas.setTitle('Document title')
width,height =A4
pdf_canvas.setPageSize((width,height))

pdfmetrics.registerFont(UnicodeCIDFont('HeiseiKakuGo-W5'))
font_size = 20

cent_x =int(width/2)
cent_y =int(height/2)

pdf_canvas.setFont('HeiseiKakuGo-W5', font_size)
pdf_canvas.drawString(cent_x,cent_y,"Hello ReportLab")

# これで次のページになる
pdf_canvas.showPage()
# ここから新しい2ページ目になる

pdf_canvas.setFont('HeiseiKakuGo-W5', font_size)
pdf_canvas.drawString(cent_x,cent_y,"完全なマムシに近い存在になったよん")


pdf_canvas.save()