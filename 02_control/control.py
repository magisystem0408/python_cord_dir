
# if文
x=-10
if x<10:
    print('true')
elif x<20:
    print('mamushi')
else:
    print('false')

y=[1,2,4]
x=1

# yにxが入っているか判定するとき
if x in y:
    print('存在している')

#yにxが入っていないを判定する時
if x not in y:
    print('存在していない')

# 次のようにも記述ができる
a=1
b=2

if not  a==b:
    print('これでもok')

# 普通は以下のように記述する
if a!=b:
    print('こっちで書く')

# ただBoolean型で否定するときに使用するケースがある
is_ok=True

if not is_ok:
    print('hello')

# 値が入ってない時に判定する方法
# 何か文字数字が入ってればtrue
# 0,[],{},set()など何も入ってなかったらfalse

is_ok=1
if is_ok:
    print('hello')

# 空の文字列でも同様になる
is_ok=''
if is_ok:
    print('hello')
else:
    print('No!')

# 実行結果はNOになる

# 何も入ってないのを以下で表現する
is_empty =None

# Noneをifのなかで判定かけるときisを使う
# isを判定で使うときはNoneを判定する時に使用する

if is_empty is None:
    print('何も入ってない状態')

# ifの条件でnoneで無い場合を判定

if is_empty is not None:
    print('何か文字が入ってるよ')


# while文
count =0
while count <5:
    print(count)
    count +=1


#break文の使い方
count=0
while True:
    if count >=5:
        # ここで処理を終了する
        break
    if count ==2:
        count +=1
        # continueがくるとその下は実行されず次の処理が走る
        continue
    print(count)
    count+=1


#elseはwhile文にbreakが無い場合に使う
count =0
while count <5:
    print(count)
    count +=1
else:
    print('done')

#以下のようにbreakが存在するとelseは出力されない

while count <5:
    if count ==1:
        break
    print(count)
    count +=1
else:
    print('ここは出力されない')

