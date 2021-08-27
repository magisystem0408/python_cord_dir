import tkinter as tk

def click():
    print("テスト")

canvas =tk.Tk()
canvas.title("テストキャンパス")


# 画面内にテキスト作成
label =tk.Label(canvas,text="テスト用")
label.place(x=20,y=20)


button =tk.Button(canvas,text='click me',command=click)
button.place(x=20,y=100)


canvas.mainloop()

