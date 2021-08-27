import socket

so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 何もしないと
so.bind(('', 5555))

so.listen(10)
c, addr = so.accept()

while True:
    data = c.recv(1024)
    dataStr = str(data, encoding='utf-8')
    if dataStr == 'exit':
        break

    # 受け取ったデータを表示
    print(dataStr)
    # 受け取ったデータをclient側におうむ返し
    c.send(bytes('I recv your msg'+dataStr,encoding='utf8'))
    so.close()