"""カプセル化の書き方"""

class Human:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        print("getterを呼び出しました")
        return self.__name

    @property
    def age(self):
        return self.__age

    @name.setter
    def name(self, value):
        print("settterを呼び出しました")
        self.__name = value

    @age.setter
    def age(self, value):
        print("setterを呼び出しました")
        self.__age = value


human = Human("mamushi", 18)

human.name = "nekomamushi"
human.age = 40

print(human.name,human.age)