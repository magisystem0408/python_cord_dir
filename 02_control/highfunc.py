""" 高階関数"""
def print_hello():
    print('hello')

def print_goodbye():
    print('goodby')

var =['AA','BB',print_hello,print_goodbye]

# ここで呼び出す
var[2]()
var[3]()


# !関数を引数に渡す
def print_world(msg):
    print('{}world'.format(msg))

def print_konnitiwa():
    print('こんにちは')

def print_hello(func):
    func('hello')
    return print_konnitiwa


var = print_hello(print_world)
var()

# 実行結果
# hello world
# こんにちは
