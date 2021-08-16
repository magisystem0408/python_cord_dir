import re

s = '<html><head><title>tilte</title></head></html>'

# これをやると思い通りに抜き出せない
print(re.match('<.*>',s))


# ?は0か1かいマッチするか
print(re.match('<.*?>',s))
