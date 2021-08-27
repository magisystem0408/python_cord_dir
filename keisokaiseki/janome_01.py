"""
形態素解析をしてみる
"""
# トークン解析を行うやち
from janome.tokenizer import Tokenizer


token =Tokenizer()


# ここで解析する
tokens =token.tokenize("解析する文章を入れる。これは完全にマムシになってしまった")

# ここで取り出す
for token in tokens:
    print(token)