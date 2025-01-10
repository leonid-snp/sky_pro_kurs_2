#!/usr/bin/python3

"""
Формат заказчика:
{"skolko": 5.0, "poroda": "тунец", "sred_razmer": 300}

Наш формат:
{"count": 5, "specie": "Тунец" , "avg_size": 30 }

Заказчик называет ключи транслитом, хранит количество рыб в типе с точкой,
размер рыбы в миллиметрах, а породу пишет с маленькой буквы. Просто катастрофа, а не заказчик!
Придется писать конвертер.
"""

# Задача
"""
order = [
 {"skolko": 5.0, "poroda": "тунец", "sred_razmer": 300},
 {"skolko": 15.0, "poroda": "окунь", "sred_razmer": 250},
 {"skolko": 20.0, "poroda": "щука", "sred_razmer": 460},
]
order_converted = []

# Не удаляйте текст ниже, он нужен для проверки

for item in order_converted:
  for key, value in item.items():
      print(key, value)
"""

# Решение
order = [
    {"skolko": 5.0, "poroda": "тунец", "sred_razmer": 300},
    {"skolko": 15.0, "poroda": "окунь", "sred_razmer": 250},
    {"skolko": 20.0, "poroda": "щука", "sred_razmer": 460},
]
order_converted = []

for i in order:
    new_dict = {
        "count": int(i['skolko']), "specie": i['poroda'].capitalize(), "avg_size": i['sred_razmer'] // 10
    }
    order_converted.append(new_dict)

# Не удаляйте текст ниже, он нужен для проверки

for item in order_converted:
    for key, value in item.items():
        print(key, value)
