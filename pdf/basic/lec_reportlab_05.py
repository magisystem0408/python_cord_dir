from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

from reportlab.platypus import Table, TableStyle

# 色の指定
from reportlab.lib import colors

##表の作成
pdf_canvas = canvas.Canvas('sample.pdf')
pdf_canvas.setTitle('Document title')
width, height = A4
pdf_canvas.setPageSize((width, height))

pdfmetrics.registerFont(UnicodeCIDFont('HeiseiKakuGo-W5'))
font_size = 10

data = [
    ['マムシ', 'ねこ', 'ちみ'],
    ['ねこ', 'マムシ', 'ゼミ'],
    ['ねこ', 'みんみん', 'そうゆう'],
]

table = Table(data, colWidths=30 * mm, rowHeights=30 * mm)

# テーブルの書式設定
# -1は一番最後という意味
table.setStyle(TableStyle([
    ('FONT',(0,0),(-1,-1),'HeiseiKakuGo-W5',font_size),

    # 第二引数は罫線の太さ
    ('BOX',(0,0),(-1,-1),3,colors.black),
    ('INNERGRID',(0,0),(-1,-1),0.5,colors.red),

    #セルのなかの位置
    #  TOP MIDDLE BUTTOM (y軸方向)
    ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
    # LEFT CENTER RIGHT (x軸方向)
    ('ALIGN',(0,0),(-1,-1),"CENTER"),

    # セルの合体
    # ("SPAN",(0,0),(1,1)),

    #表の背景色の設定
    ('BACKGROUND',(0,0),(1,1),colors.lightgreen)

]))

#テーブルの書き込み
table.wrapOn(pdf_canvas,10*mm,10*mm)
table.drawOn(pdf_canvas,10*mm,10*mm)



pdf_canvas.save()