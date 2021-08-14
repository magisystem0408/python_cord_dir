from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle


def set_canvas(file_path):
    pdf_canvas = canvas.Canvas(file_path)
    width, height = A4
    pdf_canvas.setPageSize((width, height))
    return pdf_canvas


def make_quotation_layout(pdf_canvas):
    #見積書のタイトル
    font_size = 26
    pdf_canvas.setFont('HeiseiKakuGo-W5', font_size)
    pdf_canvas.drawString(210, 790, '御　見　積　書')

    #発行日・文書番号の表
    font_size = 10
    ISSUE_DATE = '2021/3/1'
    DOC_NUM = '01234'
    data = [
    ['発行日 : '+ISSUE_DATE],
    ['No. '+DOC_NUM]]
    table = Table(data, colWidths=50*mm, rowHeights=7*mm)
    table.setStyle(TableStyle([
            ('FONT', (0, 0), (-1, -1), 'HeiseiKakuGo-W5', font_size),
            ('BOX', (0, 0), (-1, -1), 1, colors.black),
            ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.black),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ("ALIGN", (0,0), (-1,-1), "CENTER")
        ]))
    # tableを描き出す位置を指定
    table.wrapOn(pdf_canvas, 150*mm, 260*mm)
    table.drawOn(pdf_canvas, 150*mm, 260*mm)

    # 宛先
    font_size = 13
    ADDRESS = '◯◯△△株式会社'
    pdf_canvas.setFont('HeiseiKakuGo-W5', font_size)
    pdf_canvas.drawString(100, 720, ADDRESS+'　　御中')
    pdf_canvas.line(60, 710, 280, 710)

    # 自社情報
    font_size = 11
    COMPANY_INFO_1 = '株式会社 □□'
    COMPANY_INFO_2 = '東京都中央区△-△-△　◯◯ビル3階'
    COMPANY_INFO_3 = 'TEL : 03-1234-5678'
    COMPANY_INFO_4 = 'Email : aaabbb@abc.com'
    COMPANY_INFO_5 = '担当 : やじろべえ'
    data = [
    [COMPANY_INFO_1],
    [COMPANY_INFO_2],
    [COMPANY_INFO_3],
    [COMPANY_INFO_4],
    [COMPANY_INFO_5]
    ]
    table = Table(data, colWidths=80*mm, rowHeights=8*mm)
    table.setStyle(TableStyle([
            ('FONT', (0, 0), (-1, -1), 'HeiseiKakuGo-W5', font_size),
            ('BOX', (0, 0), (-1, -1), 1, colors.black),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ("ALIGN", (0,0), (-1,-1), 'LEFT')
        ]))
    # tableを描き出す位置を指定
    table.wrapOn(pdf_canvas, 120*mm, 210*mm)
    table.drawOn(pdf_canvas, 120*mm, 210*mm)

    # お見積り金額・件名・有効期限
    font_size = 16
    ESTIMATE_AMOUNT_TITLE='御見積金額（税込）　　'
    ESTIMATE_AMOUNT='¥330,000'
    SUBJECT_TITLE='件名：　'
    SUBJECT='Webアプリ開発'
    EXPIRATION_DATE_TITLE='有効期限：　'
    EXPIRATION_DATE='2021/04/01'
    pdf_canvas.setFont('HeiseiKakuGo-W5', font_size)
    pdf_canvas.drawString(60, 550, ESTIMATE_AMOUNT_TITLE+ESTIMATE_AMOUNT)
    pdf_canvas.line(40, 545, 570, 545)
    font_size = 13
    pdf_canvas.setFont('HeiseiKakuGo-W5', font_size)
    pdf_canvas.drawString(60, 520, SUBJECT_TITLE+SUBJECT)
    pdf_canvas.line(40, 515, 570, 515)
    pdf_canvas.drawString(60, 490, EXPIRATION_DATE_TITLE+EXPIRATION_DATE)
    pdf_canvas.line(40, 485, 570, 485)

    # 品名などを記載する表の作成
    font_size=10
    pdf_canvas.setFont('HeiseiKakuGo-W5', font_size)
    CONTENT_LIST = ['1', 'アプリ開発', '1', '300,000', '300,000', '']
    data = [
    ['No.', '項目', '数量', '単価（税抜）', '金額（税抜）', '備考'],
    CONTENT_LIST,
    ['　', '　', '　', '　', '　', '　'],
    ['　', '　', '　', '　', '　', '　'],
    ['　', '　', '　', '　', '　', '　'],
    ['　', '　', '　', '　', '　', '　'],
    ['　', '　', '　', '　', '　', '　'],
    ['　', '　', '　', '　', '　', '　'],
    ['　', '　', '　', '　', '　', '　'],
    ['　', '　', '　', '　', '　', '　'],
    ['　', '　', '　', '　', '　', '　'],
    ['税抜合計', '　', '　', '　', '300,000', '　']
    ]
    #tableの大きさの指定（行と列ごとの指定）
    table = Table(data, colWidths=(10*mm, 60*mm, 15*mm, 25*mm, 25*mm, 50*mm), rowHeights=(7*mm))
    table.setStyle(TableStyle([
            ('FONT', (0, 0), (-1, -1), 'HeiseiKakuGo-W5', font_size),
            ('BOX', (0, 0), (-1, -1), 1, colors.black),
            ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.black),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ("ALIGN", (0,0), (-1,-1), "RIGHT"),
            ('SPAN', (0, 11), (3, 11))
        ]))
    # tableを描き出す位置を指定
    table.wrapOn(pdf_canvas, 15*mm, 80*mm)
    table.drawOn(pdf_canvas, 15*mm, 80*mm)

    # 小計・消費税・合計表示
    font_size = 9
    pdf_canvas.setFont('HeiseiKakuGo-W5', font_size)
    SUBTOTAL_AMOUNT_TITLE = '小計：　　　'
    TAX_TITLE = '消費税：　　'
    TOTAL_AMOUNT_TITLE = '税込合計：　'
    SUBTOTAL_AMOUNT = '300,000'
    TAX = '30,000'
    TOTAL_AMOUNT = '330,000'
    pdf_canvas.drawString(360, 200, SUBTOTAL_AMOUNT_TITLE+SUBTOTAL_AMOUNT)
    pdf_canvas.line(350, 195, 550, 195)
    pdf_canvas.drawString(360, 180, TAX_TITLE+TAX)
    pdf_canvas.line(350, 175, 550, 175)
    pdf_canvas.drawString(360, 160, TOTAL_AMOUNT_TITLE+TOTAL_AMOUNT)
    pdf_canvas.line(350, 155, 550, 155)

    # 備考欄
    font_size = 12
    REMARKS_TITLE='備考'
    pdf_canvas.setFont('HeiseiKakuGo-W5', font_size)
    pdf_canvas.drawString(60, 120, REMARKS_TITLE) 
    data = [
    ['　'],
    ]
    table = Table(data, colWidths=185*mm, rowHeights=30*mm)
    table.setStyle(TableStyle([
            ('FONT', (0, 0), (-1, -1), 'HeiseiKakuGo-W5', font_size),
            ('BOX', (0, 0), (-1, -1), 1, colors.black),
        ]))
    # tableを描き出す位置を指定
    table.wrapOn(pdf_canvas, 15*mm, 10*mm)
    table.drawOn(pdf_canvas, 15*mm, 10*mm)

    return pdf_canvas




if __name__ == '__main__':
    # ファイルとフォントの設定
    file_path = 'quotation.pdf'
    pdfmetrics.registerFont(UnicodeCIDFont('HeiseiKakuGo-W5'))

    pdf_canvas = set_canvas(file_path)

    pdf_canvas = make_quotation_layout(pdf_canvas)

    pdf_canvas.save()