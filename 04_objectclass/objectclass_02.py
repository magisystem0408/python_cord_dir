# classの中身を勝手に書き換えたくない時
# アンダースコアつけて書き換えられないようにする
#
# 使用用途
# ある条件が会った時だけ書き換えてok
# 完全に隠したい場合はアンダースコアを二つつける
# するとclassのなかからしかアクセスができなくなる

class Car(object):
    def __init__(self,model =None):
        self.model =model

    def run(self):
        print('run')

class ToyotaCar(Car):
    def __init__(self,model ='mamushi',enable_auto_run=False):
        # 親クラスのinitを呼び出し
        super().__init__(model)

        # アンダースコアで外から書き換えられたりできないようにする
        self._enable_auto_run =enable_auto_run

        # 読み込みはできるけど設定はできないようにする
        @property
        # これをプロパティのゲッター(読み込み)と呼ぶ
        def enable_auto_run(self):
            return self._enable_auto_run

        # ↑を書き換える場合
        @enable_auto_run.setter
        def enable_auto_run(self,is_enable):
            self._enable_auto_run =is_enable

    def run(self):
        print('superfirst')


toyota_car =ToyotaCar('mamushi')
toyota_car.enable_auto_run = True
print(toyota_car.enable_auto_run)

# 実行結果
# true

# 抽象クラス
# わかりにくくなるので非推奨
# 継承先で必ず実装しないといけない

import abc

# metaclassを入れる
class Person(metaclass=abc.ABCMeta):
    def __init__(self,age=1):
        self.age = age

    def drive(self):
      pass

class Baby(Person):
    def __init__(self,age=1):
        if age <18:
            # 親クラス継承
            super().__init__(age)
        else:
            raise ValueError
    def drive(self):
        print('ok')


# 多重継承

class Person(object):
    def talk(self):
        print('taik')

class Car(object):
    def run(self):
        print('run')

    # 多重継承させる
    #ただし左側(Person)で見つけた物が先に実行されるので
    # 関数が同じ時には注意が必要
class PersonCarRobot(Person,Car):
    def fly(self):
        print('fly')

person_car_robot =PersonCarRobot()
person_car_robot.talk()
person_car_robot.run()
person_car_robot.fly()

# 実行結果
# taik
# run
# fly

# クラス変数
class Person(object):
    # クラス変数定義
    kind ='human'

    def __init__(self,name):
        self.name =name

    def who_are_you(self):
        print(self.name,self.kind)


a =Person('A')
a.who_are_you()

# 実行結果
# A human

# ただし、リストの時は継承されてしまうので注意

class T(object):

    words =[]
    def add__word(self,word):
        self.words.append(word)

c =T()
c.add__word("timi")
c.add__word("mamushi")

d=T()
d.add__word('migya')

print(c.words)
print(d.words)

# 実行結果
# ['timi', 'mamushi', 'migya']
# ['timi', 'mamushi', 'migya']