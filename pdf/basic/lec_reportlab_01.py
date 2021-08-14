
from reportlab.pdfgen import canvas

# ページサイズを図るやつ
# m単位指定
from reportlab.lib.units import mm
# ピクセル単位
from reportlab.lib.pagesizes import A4

# フォントを登録するためのモジュール
from reportlab.pdfbase import pdfmetrics
# どのフォントを使用するか
from reportlab.pdfbase.cidfonts import UnicodeCIDFont


# 作るページ文
NUM_PAGE = 5
for i in range(NUM_PAGE):
    file_path ='basic/out_pdf/'+ 'page0' + str(i) + '.pdf'

    # pdfの作成
    pdf_canvas = canvas.Canvas(file_path)

    # メタ情報
    pdf_canvas.setTitle('ドキュメントファイル')

    # ページサイズの指定

    # ミリ単位の指定
    # width = 210 * mm
    # height = 297 * mm
    # pdf_canvas.setPageSize((width,height))


    # ピクセル単位の指定
    width, height = A4
    pdf_canvas.setPageSize((width, height))

    # フォントの指定
    pdfmetrics.registerFont(UnicodeCIDFont('HeiseiKakuGo-W5'))
    font_size = 20
    pdf_canvas.setFont('HeiseiKakuGo-W5', font_size)

    # 書き込み
    # 第一引数と第二引数は左下を原点に座標が入る
    posi_x=10
    posi_y =10
    if i ==4:
        posi_x +=20
        posi_y +=30
    pdf_canvas.drawString(posi_x, posi_y, "TestPage"+str(i))
    pdf_canvas.save()
