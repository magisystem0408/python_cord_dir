# getter setter
# setter：クラスの変数を書き換えたい時に使用する
# getter：インスタンスしたものから値を取得する

"""カプセル化"""
""" 使用ケース01：変数を隠したい時に使用する """


class Human:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        print("getter nam　を呼びました")
        return self.__name

    def get_age(self):
        print("getter ageを呼び出しました")
        return self.__age

    def set_name(self, name):
        print("setter nameを呼びました")
        self.__name = name

    def set_age(self, age):
        print("setter ageを呼びました")
        self.__age = age

    # nameをセットするとget_nameとset_nameが呼び出される
    name = property(get_name, set_name)
    age = property(get_age, set_age)

    def print_msg(self):
        print(self.name, self.age)


human = Human("Tarp", 15)

human.name = 'Jiro'
human.age = 18

name = human.name
age = human.age

print(name, age)


human.print_msg()