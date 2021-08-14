"""
socket通信について

socket通信== TCP/IP通信のこと

AF_INET6
IPv6 と IPv4 用のインターネットファミリ

AF_INET
IPv4 専用のインターネットファミリ

"""

import socket


#サーバー側の実装

# AF_INETは(host,port)ペアがアドレスとして利用される
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind(('127.0.0.1',50007))
    s.listen(1)
    while True:
        conn, addr =s.accept()
        with conn:
            data =conn.recv(1024)
            if not data:
                break
            print('data:{},addr:{}'.format(data,addr))
            conn.sendall(b'Received: '+data)



# UDPの場合
with socket.socket(socket.AF_INET,socket.SOCK_DGRAM)as s:
    s.bind(('127.0.0.1',50007))

    while True:
        data,addr =s.recv(1024)
        print("data: {},addr: {}".format(data,addr))