from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont



pdf_canvas =canvas.Canvas('sample.pdf')
pdf_canvas.setTitle('Document title')
width,height =A4
pdf_canvas.setPageSize((width,height))


# 画像の挿入
# pdf_canvas.drawImage('image.jpeg',0,0)

#　線の描画
pdf_canvas.setStrokeColorRGB(0,0,0)
pdf_canvas.setLineWidth(3)

#中心座標

cent_x =int(width/2)
cent_y =int(height/2)

#描画
pdf_canvas.line(0,0,cent_x,cent_y)


# 波線定義
pdf_canvas.setDash([5,5,5])
pdf_canvas.line(cent_x,cent_y,width,height)


pdf_canvas.save()

