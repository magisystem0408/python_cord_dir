# クラスメソッドとスタティックメソッドについて
class Person(object):
    kind='human'

    def __init__(self):
        self.x =100

    # クラスメソッド
    @classmethod
    def what_is_your_kind(cls):
        return cls.kind
    
    # スタティックメソッド==外務関数と一緒
    @staticmethod
    def about(year):
        print('mamushi{}'.format(year))
        
# ここで()でオブジェクト生成していなくても実行できるようになる
b=Person
print(b.what_is_your_kind())

# 実行結果
# human
Person.about(1999)

# 実行結果
# mamushi1999


# 特殊メソッド

class word(object):
    def __init__(self,text):
        self.text =text

    def  __str__(self):
        return '文字列として読み込まれた時'
    def  __len__(self):
        return len(self.text)
    def  __add__(self, word):
        return self.text.lower() +word.text.lower()
    # 判定文
    def __eq__(self, word):
        return self.text.lower() == word.text.lower()

w=word('text')
print(w)
# 実行結果
# 文字列として読み込まれた時

print(len(w))
# 実行結果
# 4

w =word('text')
w2= word('timi')
print(w+w2)

# 実行結果
# texttimi


# 本来であれば
# w.text()+w2.text()とやらなければならないがショートカットできる

print(w==w2)