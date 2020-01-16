import json
print('////Десериализация//////')
with open('t4.json', 'r') as ff:
    deser_data = json.load(ff)
    print(deser_data)
    print(type(deser_data))
print('////////Данные в JSON-формате могут быть получены различными способами'
      ' и быть представлены, например, в виде строки.'
      'Строку можно десериализировать с помощью функции loads)')
json_str = '{"income": {"salary": 50000, "bonus": 2000}}'# загружаем в  виде строки
data = json.loads(json_str)
print(data)
print(type(data))