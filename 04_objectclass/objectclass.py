# クラス
#記述ルールでobjectを入れる

class Person(object):
    def say_something(self):
        print('hello')

# オブジェクト生成
person = Person()
person.say_something()


# __init__について
# classが起動した時に最初に呼ばれるもの(コンストラクタ)
# classは自分自身に値を保持させられないので
# 毎回selfをつけて値を保持する

class Person(object):

    def __init__(self,name):
        # 自分自身の名前
        self.name = name
        print('First')

    def  say_something(self):
        print('私は{} hello'.format(self.name))

person = Person('Mike')
person.say_something()

# 実行結果
# 私はMike hello


class Person(object):

    def __init__(self,name):
        # 自分自身の名前
        self.name = name
        print('First')

    def  say_something(self):
        print('私は{} hello'.format(self.name))

        # 自分自身のメソッドにアクセスすることも可能
        self.run()

    def run(self):
        print('run')

person = Person('Mike')
person.say_something()

# 実行結果
# First
# 私はMike hello
# run


# デストラクタ

class Person(object):

    def __init__(self,name):
        # 自分自身の名前
        self.name = name
        print('First')

    def  say_something(self):
        print('私は{} hello'.format(self.name))

        # 自分自身のメソッドにアクセスすることも可能
        self.run()

    def run(self):
        print('run')

    #classが終了するときにできる
    def __del__(self):
        print('デストラクタ')

person = Person('Mike')
person.say_something()


# クラスの継承

class Car(object):
    def run(self):
        print('run')

class ToyotaCar(Car):
    pass

class TeslaCar(Car):
    def auto_run(self):
        print('auto run')

toyota_car =ToyotaCar()
toyota_car.run()

tesla_car = TeslaCar()
tesla_car.run()
tesla_car.auto_run()


# 実行結果
# run
# run
# auto run


# メソッドのオーバーライド

class Car(object):
    def run(self):
        print('run')

class ToyotaCar(Car):
    # メソッドを再度書くと上書きできる
    def run(self):
        print('superfirst')


toyota_car =ToyotaCar()
toyota_car.run()

# 実行結果
# superfirst


class Car(object):
    # 引数をここで定義
    def __init__(self,model =None):
        self.model =model

    def run(self):
        print('run')

class ToyotaCar(Car):
    def run(self):
        print('superfirst')


toyota_car =ToyotaCar('mamushi')
print(toyota_car.model)
toyota_car.run()

# 実行結果
# mamushi
# superfirst



# __init__の継承関連について
# 継承先で親クラスのinitを呼び出す方法
class Car(object):
    def __init__(self,model =None):
        self.model =model

    def run(self):
        print('run')

class ToyotaCar(Car):
    def __init__(self,model ='mamushi',enable_auto_run=False):
        # 親クラスのinitを呼び出し
        super().__init__(model)
        self.enable_auto_run =enable_auto_run

    def run(self):
        print('superfirst')


toyota_car =ToyotaCar('mamushi')
print(toyota_car.model)
toyota_car.run()


