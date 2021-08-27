　"""
XMLとJsonの読み込み
"""

# XML
# <? xml version="1" encoding="UTF-8">
# <root>
#     <employee>
#         <employ>
#             <id>111</id>
#             <name>Mike>
#         </employ>
#     <employee>
# </root>

# json
# {
#     "employ":
#         [
#             {"id":111,"name":"Mike"},
#             {"id":111,"name":"Mike"},
#         ]
# }

# XMLによるアプローチ

import  xml.etree.ElementTree as ET
root = ET.Element('root')
tree =ET.ElementTree(element=root)

# 各種書き込み内容を定義
employee =ET.SubElement(root,'employee')
employ =ET.SubElement(employee,'employ')


employ_id =ET.SubElement(employ,'id')
employ_id.text ='111'

employ_id=ET.SubElement(employ,'name')
employ_id.text ='Mike'

# 書き込みファイル生成
tree.write('test.xml',encoding='utf-8',xml_declaration=True)

# 読み込みたい時
tree =ET.ElementTree(file='test.xml')
root=tree.getroot()


for employee in root:
    for employ in employee:
        for person in employ:
            print(person.tag,person.text)


# JSON

import json
j={
    "employee":
        [
            {"id":111,"name":"Mike"},
            {"id":122,"name":"Nancy"}
        ]
}

print(json.dumps(j))

# 実行結果
# ダブルクォーとになる

# {"employee": [{"id": 111, "name": "Mike"}, {"id": 122, "name": "Nancy"}]}


# ファイルに書き込む場合
with open('test.json','w') as f:
    json.dump(j,f)
    
# 読み込み
with open('test.json','r') as f:
    json.load(f)

# たたしpythonのなかだけで読み込みたい場合

a=json.loads(j)
json.loads(a)