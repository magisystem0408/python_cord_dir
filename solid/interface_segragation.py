# インターフェース分離の原則
# いらないコードを書かないようにする

from abc import ABCMeta, abstractmethod


# 下記の書き方だといらないコードが増えてしまう。

# class Athlete(metaclass=ABCMeta):
#     @abstractmethod
#     def swim(self):
#         pass
#
#     @abstractmethod
#     def high_jump(self):
#         pass
#
#     @abstractmethod
#     def long_jamp(self):
#         pass
#
# class Athlete1(Athlete):
#
#     def swim(self):
#         print('I swim')
#
#     def high_jump(self):
#         pass
#
#     def long_jamp(self):
#         pass
#

class Athlete(metaclass=ABCMeta):
    pass

# ここで分けてあげる
class SwimAthlete(Athlete):
    @abstractmethod
    def swim(self):
        pass


class JumpAthlete(Athlete):
    @abstractmethod
    def high_jump(self):
        pass

    @abstractmethod
    def long_jump(self):
        pass


class Athlete1(SwimAthlete):
    def swim(self):
        print("I swim")

# どちらも使いたい時は多重継承を使用する
class Athlete2(SwimAthlete,JumpAthlete):

    def swim(self):
        print("I swim")


    def high_jump(self):
        print("I hign jump")

    def long_jump(self):
        print("I long jump")


john =Athlete1()
john.swim()


yuji =Athlete2()
yuji.high_jump()

