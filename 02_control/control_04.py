"""
・関数内関数
・クロージャー
・デコレーター
・ラムダ
"""



# 関数内関数
def outer(a,b):

    def plus(c,d):
        return c+d

    r1 =plus(a,b)
    r2 =plus(b,a)
    print(r1+r2)

outer(1,2)

# 実行結果
# 3

#クロージャー
#内部関数をすぐに実行したくない時に使用する

def outer(a,b):
    # ここで実行はまだされない
    def inner():
        return a+b
    return inner

f=outer(1,2)
# ここで実行される
r=f()
print(r)

# 実行結果
# 3

# 実行例
def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius
    return circle_area

# 先にpiの値を決めてしまう
cal1 = circle_area_func(3.14)
cal2 = circle_area_func(3.1415192)

print(cal1(10))
print(cal2(10))


# デコレーター
def  print_info(func):
    def  wrapper(*args,**kwargs):
        print('start')
        result = func(*args,**kwargs)
        print('end')
        return result
    return wrapper

# デコレーターだとわかるように@で目印つけるて呼び出せる
@print_info
def add_num(a,b):
    return a+b
r = add_num(10,20)

print(r)

# 時刻結果
# start
# end
# 30


# デコレーターは順序が重要になってくる
def print_more(func):
    def wrapper(*args,**kwargs):
        print('func：',func.__name__)
        print('args：',args)
        print('kwargs',kwargs)
        result =func(*args,**kwargs)
        print('result',result)
        return result
    return wrapper

def  print_info(func):
    def  wrapper(*args,**kwargs):
        print('start')
        result = func(*args,**kwargs)
        print('end')
        return result
    return wrapper

# ここの順序が重要
@print_info
@print_more

def add_num(a,b):
    return a+b

r = add_num(10,20)
print(r)


# 実行結果
# start
# func： add_num
# args： (10, 20)
# kwargs {}
# result 30
# end
# 30

#ラムダ

#ラムダで書いた場合
l=['Mon','tue','wed','Thu','fri','sat','sun']

def change_words(words,func):
    for word in words:
        print(func(word))

# lambdaで一行でかける
change_words(l,lambda word:word.capitalize())



# 通常で書いた場合
l=['Mon','tue','wed','Thu','fri','sat','sun']

def change_words(words,func):
    for word in words:
        print(func(word))

def sample_func(word):
    # 文字の最初を大文字にする
    return word.capitalize()

# オブジェクトでsample_funcは渡す
change_words(l,sample_func)

# 実行結果
# Mon
# Tue
# Wed
# Thu
# Fri
# Sat
# Sun