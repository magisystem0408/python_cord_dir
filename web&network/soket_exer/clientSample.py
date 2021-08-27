import socket

# ソケットを作成
# TCP通信を行う
so =socket.socket(socket.AF_INET,socket.SOCK_STREAM)


# サーバーに接続する
so.connect(('127.0.0.1',5555))

while True:
    msg =input("メッセージを送る")

    so.send(bytes(msg,encoding="utf-8"))

    data =so.recv(1024)
    if msg=='exit':
        break