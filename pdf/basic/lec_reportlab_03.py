from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont


##図形の描画


pdf_canvas =canvas.Canvas('sample.pdf')
pdf_canvas.setTitle('Document title')
width,height =A4
pdf_canvas.setPageSize((width,height))

rect_x=100
rect_y =100
rect_w =100
rect_h=50
pdf_canvas.rect(rect_x,rect_y,rect_w,rect_h)


# 塗りつぶし
pdf_canvas.setFillColorRGB(0,0,0)
pdf_canvas.rect(rect_x+100,rect_y+100,rect_w,rect_h,fill =True)

# 角を丸くする
rect_r =5
pdf_canvas.roundRect(rect_x-50,rect_y+300,rect_w,rect_h,rect_r)


# 円を書く
c_x=400
c_y =400
c_r =50
pdf_canvas.circle(c_x,c_y,c_r)

pdf_canvas.save()