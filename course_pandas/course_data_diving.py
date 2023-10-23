import pandas as pd
""" Lesson 1 """
# создадим таблицу продаж
date = ['01.08.23', '02.08.23', '03.08.23', '04.08.23', '05.08.23']
sale_1 = [1, 2, 3, 4, 5]
sale_2 = [6, 7, 8, 9, 10]

sale_df = pd.DataFrame(
    {'date': date,
     'sale_1': sale_1,
     'sale_2': sale_2}
)

# print(sale_df[['date', 'sale_1']])

sale_df['total_sale'] = sale_df['sale_1'] + sale_df['sale_2']
# print(sale_df)

table_header = 'Базис поставки'
replaced_table_header = table_header.replace('поставки', 'отгрузки')
# print(replaced_table_header)


table_header1 = 'объем договоров в единицах измерения'
table_header1_new = table_header1.replace(' ', '_', 2)
# print(table_header1_new)

# print(table_header1_new.find('р'))

item = 'Бензин (АИ-92-К5)'
station = "Яничкино"
price_per_tone = 37740
sales_per_day = 565.245
revenue_per_day = price_per_tone * sales_per_day
percent_of_sales = sales_per_day / (840 + 565.245 + 1320)
# print(f'Отгрузка {item} за 10 мая со станции {station.upper()} составляет {60*10} тонн')   #  f-строки

"""   Установить определённое количество цифр после точки в вещественных числах (float) 
можно следующим образом: {переменная:.Nf}, где
N – количество знаков после точки."""

# print(f'Отгрузка {item} за 10 мая со станции {station.upper()} составляет {sales_per_day:.2f} тонн')

"""   Для форматирования процентов работает шаблон {переменная:.N%}, 
где N — количество знаков после точки."""

# print(f'Отгрузка {item} за 10 мая со станции {station.upper()} составляет {sales_per_day:.0f} тонн или {percent_of_sales:.1%} общего объема')



"""   List.     Списки   []   Упорядоченный, изменяемый"""
stations = ['Новоярославская', 'Яничкино', 'Комбинатская', 115, 65, 48, 99, 100, 101]
# print(f'Длина списка stations {len(stations)} элемета')
# print(stations[1])
# print(stations[2:6:2])

stations.append('new_item')      # добавление элемента
additional_stations = ['Станция 1', 'Станция 99', 'Станция 3']
stations.extend(additional_stations)  #  добавление другого списка

stations.insert(2, 'Я новенький')       # list.insert(index, element)  Добавление элемента в определенное место в списке
stations.remove('Я новенький')  # удаление объекта по значению
stations.pop(10)    # удаление объекта по индексу
del stations[6:9]  # удаление по индексу  или удаление среза
station_numbers = [1, 9, 8, 6, 2, 4, 5, 3, 7, 9, 9]
# station_numbers.sort()   # сортировка по возрастанию
#station_numbers.sort(reverse=True)   # сортировка по убыванию



"""   sort() изменяет исходный список ,
sorted() не изменяет переданный список и возвращает новый отсортированный список.

"""
# print(sorted(station_numbers))

# индекс элемента по значению   list.index(element, start, end)
# print(station_numbers.index(9))

# print(station_numbers.count(9))     # количество вхождений элемента в список

"""     Преобразование строки в список
string.split(sep, maxsplit)
sep – разделитель  (по умолчанию - пробел).
maxsplit - сколько раз разделить (по умолчанию  -1)
"""
address_onpz = 'г. Омск, просп. Губкина, 1'
address_onpz = address_onpz.split()
address_onpz.remove('г.')
address_onpz.remove('просп.')
#   собрать строку из списка, выбрать разделитель
address_onpz = ' '.join(address_onpz)
# print(len(address_onpz))  # длина списка


"""     Цикл for """
senders = ['Яничкино', 'Стенькино', 'Комбинатская', 'Новоярославская']
# for sender in senders:
#     print('ст.' + sender)

# for i in range(len(senders)):
#     print('ст.', senders[i])

import numpy
shipments = [82.1, 37, 0.95]  # 82.1 - объем отгрузки, 37 - цена, 0.95 - скидка
revenue = numpy.prod(shipments)
#print(f'Выручка за день: {revenue:.2f} рублей')


sales = [
    ['ст. Новоярославская', 'ЯНОС', 840, 821.1, 37780],
    ['ст. Яничкино', 'МНПЗ', 600, 597.523, 37740],
    ['ст. Комбинатская', 'ОНПЗ', 1320, 1321.002, 36690]
]

#  сортировка по 3 элементу во вложенных списках
sorted_sales = sorted(sales, key = lambda row: row[3], reverse = True)  # сортировка по убыванию

"""     Словарь  Dictionary    {ключ : значение}    dict()     """

station_dict = {
    'ОНПЗ': 'Комбинатская',
    'МНПЗ': 'Яничкино',
    'ЯНОС': 'Новоярославская',
    'РНПК': 'Стенькино',
    }
# print(station_dict['ОНПЗ'])

"""     Конструкция try    except"""
# try:
#     print(station_dict['ХХХХ'])
#
# except KeyError as error_msg:
#     print(f'Ключ { error_msg} отсутствует')

"""     метод get       dictionary.get(key_value , default_value)  """
# print(station_dict.get('ОНПЗ', 'ключ отсутствует'))
# print(station_dict.get('ОНПЗ_1', 'ключ отсутствует'))


#   добавление элемента dictionary[key] = value
station_dict['НОРСИ'] = 'Кстово'
station_dict['НОРСИ'] = 'Зелецино'  #   замена элемента

#   удаление элемента
del station_dict['НОРСИ']

#  удаление элемента (возвращает удаленный элемент), вывод по дефолту значения, если не найден элемент
station_dict.pop('ОНПЗ', 'ключ не найден')


"""   Объединение словарей  dictionary_1.update(dictionary_2)   """

day_sales_dict = {
    '10.06.2022': ['Комбинатская', 'АИ-92', 1320, 36690],
    '11.06.2022': ['Комбинатская', 'АИ-92', 820, 36690],
    '12.06.2022': ['Комбинатская', 'АИ-92', 1200, 37100]
    }

day_sales_dict_upd = {
    '12.06.2022': ['Комбинатская', 'АИ-92', 1200, 37200],
    '13.06.2022': ['Комбинатская', 'АИ-92', 960, 37100]
    }

day_sales_dict.update(day_sales_dict_upd)

"""     Цикл для словарей"""
for_dict = {
    'Ключ_1': [1, 2, 3],
    'Ключ_2': [4, 5, 6],
    'Ключ_3': [7, 8, 9]
}

#   перебор ключей
# for item_key in for_dict.keys():
#     print(item_key)

#   Перебор значений
# for item_value in for_dict.values():
#     print(item_value[1])

#   Перебор всех пар «ключ : значение»
# for item in for_dict.items():
#     print(item)

"""     Список словарей     """

sales_list = [
    {
        'station': 'ст. Новоярославская',
        'source': 'ЯНОС',
        'item': 'АИ-92',
        'contract': 840,
        'sale': 821.1,
        'price': 37780
    },

    {
        'station': 'ст. Яничкино',
        'source': 'МНПЗ',
        'item': 'АИ-92',
        'contract': 600,
        'sale': 597.523,
        'price': 37740
    },

    {
        'station': 'ст. Комбинатская',
        'source': 'ОНПЗ',
        'item': 'АИ-92',
        'contract': 1320,
        'sale': 1321.002,
        'price': 36690
    }
]
# print(sales_list[2]['item'])

sales_added = {
    'station': 'ст. Стенькино II',
    'source':'РНПК',
    'item': 'АИ-92',
    'contract':2400,
    'sale': 2396.336,
    'price': 37710
    }

sales_list.append(sales_added)
# print(sales_list[3])

"""     Преобразование списка словарей в таблицу (датафрейм)        """

import pandas as pd
sales_df = pd.DataFrame(sales_list)
# print(sales_df)


test_islower = 'jdjfhkj kshfks kjhkjfd'
test_isnumeric = '123456'
# print(test_islower.islower())  #  Функция-предикат
# print(test_isnumeric.isnumeric())



