import http.server
import socketserver

# webサーバーを立ててみる
# 自身のポート番号を入れる

with socketserver.TCPServer(('127.0.0.1',8000),
                            http.server.SimpleHTTPRequestHandler) as httpd:
    httpd.serve_forever()