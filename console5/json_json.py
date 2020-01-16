import json
print('..............////сериализация//////')
data = {"income": {"salary": 50000, "bonus": 2000}}
with open('t4.json', 'w') as ff:
    json.dump(data, ff)
print('///Если требуется продолжить работу с сериализованными данными'
      ', то с ними можно работать, как со строкой/////')
str_json = json.dumps(data)
print(str_json)
print(type(str_json))

