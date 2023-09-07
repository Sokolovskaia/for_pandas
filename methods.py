"""     Методы value_counts(), sort_value(), unique(), nunique() """
import pandas as pd
import numpy as np
from time import time

dict_array = {
    'age': [53, 53, 11, 18, 18, np.nan],
    'name': ['Сергей', 'Сергей', 'Ксюша', 'Аристарх', 'Соня', 'Соня'],
    'наличие авто': [True, True, False, True, False, True]}

df_m = pd.DataFrame(dict_array, index=[f'row_{i}' for i in range(0, 6)])

"""     Метод uniqe() применяется только к сериям и индексам  
Врзвращает массив с уникальными значениями  
"""

for_print_1 = df_m['age'].unique()

"""     Метод nuniqe() применяется к сериям и DF 
Врзвращает количество уникальных значений  
"""

for_print_2 = df_m['age'].nunique()
for_print_3 = df_m.index.nunique()

for_print_4 = df_m.nunique()    # возвращает серию по каждому столбцу (кол-во уникальных значений)


"""     Метод value_counts()   
 подсчитываем количество одинаковых строк
 
 Строки с пропусками в подсчетах не учавствуют
 
 """

for_print_5 = df_m.value_counts()

for_print_6 = df_m['наличие авто'].value_counts()   # Для серии

for_print_7 = df_m.value_counts(['age', 'name'])        # ТОлько исходя из информации в указанных столбцах
for_print_8 = df_m.value_counts(['age', 'name'], dropna=False)  # Чтобы учитывались Nan

for_print_9 = df_m.value_counts('name', normalize=True)     #   Пропорции, как часто встречаются


"""     Метод sort_values()     СОРТИРОВКА  """

for_print_10 = df_m.sort_values('age')
for_print_11 = df_m.sort_values(['age', 'name'])    #   ПРопуски в конце
for_print_12 = df_m.sort_values('age', na_position='first')  # Пропуски наверху списка (по умолчанию - в конце)
# df_m.sort_values('age', na_position='first', inplace=True)


# print(df_m, end='\n'*2)
# print(for_print_12)




"""     ЗАДАЧИ      """
df = df_m
# count = df['name'].nunique()
# value = df['age'].unique()
#
# print(count)
# print(value)


df.sort_values('name', inplace=True)
new_ser = df['name'].value_counts()
# print(df)



"""     МЕТОД apply()   """

dct_a = {f'col_{i}': [i*1, i*2, i*3, i*4, i*5] if i !=3 else [i, i, i, i, i] for i in range(5)}
df_a = pd.DataFrame(dct_a)

""" 
Для DF:
DataFrame.apply(func, axis=0, raw=False, result_type=None, args=(), **kwargs)

Для Серии:
Series.apply(func, args=(), **kwargs)
"""

"""     apply для DF    """

# Можно использовать любые функции Python, Pandas и других библиотек
for_print_13 = df_a.apply(np.min)   #   Минимальное значение в каждом столбце


def my_func(series):
    return (series + 100) if series.name != 'col_2' else series * 0


for_print_14 = df_a.apply(my_func)

for_print_15 = df_a.apply(lambda series: (series + 100) if series.name != 'col_2' else series * 0)

"""     аргумент  axis=(по умолчанию 0/'index')"""
for_print_16 = df_a.apply(np.mean, axis=1)

"""     аргумент  raw=(по умолчанию False) False - будут переданы данные в виде серии, True - в виде массива NumPy"""
for_print_17 = df_a.apply(np.mean, axis=0, raw=True)


"""сколько времени затрачивается на выполнение функции"""

start = time()
df_a.apply(np.sum, axis=0, raw=False)
finich = time()

# print((finich - start)*1000, 3)

# start = time()
# df_a.apply(np.sum, axis=0, raw=True)
# finich = time()

# print((finich - start)*1000, 3)

"""     """

dct_a_2 = {'age': [53, 25, 11, 18, 7],
           'name': ['Фамилия_1 Имя_1', 'Фамилия_2 Имя_2 Отчество_2', 'Фамилия_3 Имя_3', 'Фамилия_4 Имя_4', 'Фамилия_5 Имя_5'],
           'наличие авто': [True, True, False,  True, False]}

df_a_2 = pd.DataFrame(dct_a_2)

'Фамилия_2 Имя_2 Отчество_2'.split(' ')

def my_func_2(series):
    name_split = series.str.split(' ')[0]

    if len(name_split) == 2:
        name_split.append(np.nan)

    # print(name_split)
    return name_split

# for_print_18 = df_a_2[['name']].apply(my_func_2, axis=1)

# df_a_2[['name']].apply(my_func_2, axis=1, result_type='expand')
df_a_2[['last_name', 'first_name', 'patronymic']] = df_a_2[['name']].apply(my_func_2, axis=1, result_type='expand')


"""     apply для Series    """

df_a_3 = pd.DataFrame(dct_a_2)

def get_patronymic(name):
    name_split = name.split(' ')

    return name_split[-1] if len(name_split) != 2 else np.nan

for_print_20 = df_a_3['name'].apply(get_patronymic)
df_a_3['first_name'] = df_a_3['name'].apply(lambda name: name.split(' ')[1])



"""     Передача дополнительных параметров в функцию, используемую в методе apply   """

""" 
def my_func(series, a , b, c, ..., q=True, w=False, e=None, ... ) 

df.apply(my_func, args=(a, b, c, ...), q=True, w=False, e=5, ... )
"""

def my_func_3(series, *args):
    if not isinstance(series, pd.Series):   # Проверка
        raise Exception('Что-то не то передаешь?')
    if len(args) == 0:
        return '___'
    if len(args) > 3:
        raise Exception('Не многовато ли аргументов в args?')

    name_split = series.str.split(' ')[0]
    if len(name_split) == 0:
        name_split.append(np.nan)

    N = {'Ф': 0, 'И': 1, 'О': 2}
    name = [name_split[N[arg]] for arg in args if arg in N]

    return name


# df_a_3['name'].apply(my_func_3) #   Сработает первая проверка
# for_print_21 = df_a_3[['name']].apply(my_func_3, axis=1, result_type='expand', args=()) #   '___'
# for_print_22 = df_a_3[['name']].apply(my_func_3, axis=1, result_type='expand', args=('Ф', 3, 'О', 2, 'dddd')) #  Лишние аргументы

#   НЕ РАБОТАЕТ!!!!
# for_print_23 = df_a_3[['name']].apply(my_func_3, axis=1, result_type='expand', args=('О', 111, 'И'))


# print(df_a_3, end='\n'*2)
# print(for_print_23)


"""
МЕТОД  map(arg, na_action=None):
используется для замены каждого значения в Series или Index другим значением, 
которое может быть получено из функции, словаря или Series. 
Аргумент arg может быть или серией, или словарем, или функцией. 
Аргумент na_action по умолчанию None, 
если принимает значение 'ignore', то значения Nan не будут преобразовываться.

"""
ser_m = pd.Series(['товар_0', 'товар_1', 'товар_2', 'товар_3', 'товар_4'])

arg_dict_m = {'товар_0': 'product_0',
              'товар_1': 'product_1',
              'товар_2': 'product_2',
              'товар_3': 'product_3',
              'товар_4': 'product_4'}
# Пример 1
new_ser_m_1 = ser_m.map(arg_dict_m)

# Пример 2
def func_m_2(str_in):
    return str_in.replace('товар', 'product')

new_ser_m_2 = ser_m.map(func_m_2)

# Пример 3
ser_m_3 = pd.Series(['товар_0', 'товар_1', 'товар_2', 'товар_3', 'товар_4', np.nan])
# определить тип данных каждого элемента в серии
new_ser_m_3 = ser_m_3.map(type) # не верно использовать, если есть пропуски, т.к. происходит преобразование

new_ser_m_4 = ser_m_3.map(type, na_action='ignore') # ф-ия применена ко всем элементам, кроме Nan

""" 
Метод isin(values):
метод показывает содержится ли переданный в него элемент в DataFrame-е, Series или Index-е. 
В метод передается один аргумент values, который содержит список с элементом 
или элементами для проверки. 
Метод возвращает DataFrame, Series или Index с логическими значениями, 
показывающие,содержится ли переданный в метод элемент. 
"""

# Пример 1
df_m_5 = pd.DataFrame({
    'год рождения': [88, 89, 90, 91, 92],
    'стаж работы': [3.25, 4.5, 5.75, 6.25, 7.5],
    'зарплата': [60000, 70000, 80000, 90000, 10000]})

new_df_51 = df_m_5.isin([5.75]) #   Встречается ли значение 5.75 в DF
# print(new_df_51)

# сколько раз значение 5.75 встречается в DF
new_df_52 = df_m_5.isin([5.75]).sum()
# print(new_df_52)

# Пример 2
# В метод isin() можно передавать несколько значений
new_df_53 = df_m_5.isin([88, 5.75, 70000])
# print(new_df_53)

# Пример 3
new_ser_m_5 = ser_m_3.isin(['товар_3', np.nan])
# print(new_ser_m_5)

"""     ЗАДАЧИ  """
# Упражнение 4
df_zadacha_1 = pd.DataFrame({
    'product': ['товар_0', 'товар_1', 'товар_4', 'товар_3', 'товар_0'],
    'product_price': [1000, 2000, 5000, 4000, 1000],
    'count': [1, 4, 2, 1, 2],
    'buy': ['куплено', 'не куплено', 'куплено', 'не куплено', 'куплено']})


arg_dict = {'куплено': True, 'не куплено': False}

df_zadacha_1['buy'] = df_zadacha_1['buy'].map(arg_dict)

# Упражнение 5
df_zadacha_2 = pd.DataFrame({
    'product': ['товар_1', 'товар_2', 'товар_0', 'товар_0', 'товар_2'],
    'product_price': ['2000 руб', '3000 руб', '1000 руб', '1000 руб', '3000 руб'],
    'count': [4, 2, 1, 4, 4],
    'buy': [False, True, True, False, False]})

# df_zadacha_2['product_price'] = df_zadacha_2['product_price'].map(lambda x: int(x[0:-4]))
df_zadacha_2['product_price'] = df_zadacha_2['product_price'].map(lambda x: int(x.strip(' руб')))


# Упражнение 6
df_zadacha_6 = pd.DataFrame({
    'product': ['товар_2', 'товар_1', 'товар_0', 'товар_0', 'товар_2'],
    'product_price': [np.nan, np.nan, 2000, np.nan, np.nan],
    'count': [2, 4, 4, 1, 1],
    'buy': ['куплено', 'не куплено', 'куплено', 'не куплено', 'куплено']})

# df_zadacha_6['product_price'] = df_zadacha_6['product_price'].map(lambda x: (str(x) + ' руб'), na_action='ignore')
df_zadacha_6['product_price'] = df_zadacha_6['product_price'].map(lambda x: f'{x} руб', na_action='ignore')

# Упражнение 7
df_zadacha_7 = pd.DataFrame({
    'name': [f'Имя_{i}' for i in range(9)],
    '1': [1.0, 1.0, 1.0, 1.0, 1.0, 0.0, np.nan, 1.0, 0.0],
    '2': [1.0, np.nan, 1.0, 1.0, 1.0, 0.0, 0.00, 1.0, 0.0],
    '3': [0.0, 1.0, 1.0, 1.0, np.nan, 0.0, 1.0, 0.0, 0.0],
    '4': [1.0, 0.0, 1.0, 0.0, 0.0, 0.0, np.nan, 1.0, 0.0]
})

print(df_zadacha_7, end='\n'*2)

def func_zadacha_7(series):
    if series == 1:
        series = series.replace(1, True)
    else:
        series = series.replace(1, True)
    return series


new_df_77 = df_zadacha_7.apply(func_zadacha_7, axis=1)
print(new_df_77, end='\n'*2)







"""     ЗАДАЧИ      """

df_4 = pd.DataFrame({'city': ['city_1', 'city_2', 'city_1', 'city_1', 'city_2']})
# print(df_4, end='\n'*2)

# def my_func_4(series):
#     if series == 'city_1':
#         series = 0
#     else:
#         series = 1
#
#     return series
#
# df_4['city'] = df_4['city'].apply(my_func_4)
# print(df_4)

# new_ser_4 = df_4['city'].apply(lambda series: 0 if series=='city_1' else 1)


df_5 = pd.DataFrame({'кол-во жителей': [100000, 200000, 20000, 30000, 31000], 'city': ['Name_1', 'Name_2', 'Name_3', 'Name_4', 'Name_5']})
"""
город > 30 000
поселок городского типа <= 30000
"""

# Вариант 1
def my_func_5(name_5):
    if name_5 > 30000:
        new_name_5 = 'город '
    else:
        new_name_5 = 'поселок городского типа '
    return new_name_5


# df_5['city'] = df_5['кол-во жителей'].apply(my_func_5) + df_5['city']

# Вариант 2
def my_func_6(ser):
    if ser['кол-во жителей'] > 30000:
        ser['city'] = 'город' + ' ' + ser['city']
    else:
        ser['city'] = 'поселок городского типа' + ' ' + ser['city']

    return ser

# df_5 = df_5.apply(my_func_6, axis=1)

# Вариант 3
df_5['city'] = df_5.apply(lambda x: f'город {x[1]}' if x[0] > 30000 else f'поселок городского типа {x[1]}', axis=1)

# print(df_5, end='\n'*2)
# print(for_print_25)

""" В столбцах с типом данных 'int64' измените тип данных на 'int32'  """

df_6 = pd.DataFrame({'col_0': [0, 69, 25, 9, 4],
                     'col_1': [10.0, 87.0, 82.0, 99.0, 44.0],
                     'col_2': [62, 47, 15, 86, 31],
                     'col_3': [80.0, 7.0, 0.0, 55.0, 19.0]})


# print(df_6.dtypes, end='\n'*2)

# Вариант 1
new_df_6 = df_6.apply(lambda x: x if x.dtype != 'int64' else x.astype('int32'), axis=0)

# Вариант 2
new_df_7 = df_6.apply(lambda s: df_6[s.name].astype('int32') if s.dtype == 'int64' else s)

# print(new_df_6.dtypes, end='\n'*2)

"""К значениям в столбцах ['year_1', 'year_2', 'year_3', 'year_4', 'year_5', 'year_6', 'year_7', 'year_8']
 прибавьте 2000.
Результат запишите в переменную new_df.
В DF могут быть не все указанные столбцы.  """

df_8 = pd.DataFrame({'col_0': [0, 69, 25, 9, 4],
                     'col_1': [10.0, 87.0, 82.0, 99.0, 44.0],
                     'col_2': [62, 47, 15, 86, 31],
                     'year_3': [1, 2, 3, 4, 5],
                     'year_7': [7, 7, 7, 7, 7],
                     'col_3': [80.0, 7.0, 0.0, 55.0, 19.0]})

# Вариант 1
slipt = ['year_1', 'year_2', 'year_3', 'year_4', 'year_5', 'year_6', 'year_7', 'year_8']
new_df_8 = df_8.apply(lambda x: (x+2000) if x.name in ['year_1', 'year_2', 'year_3', 'year_4', 'year_5', 'year_6', 'year_7', 'year_8'] else x)




"""
В DF содержится 
'product' - имя товара, 
'product_price' - цена товара,  
'count' - количество товаров в корзине, 
'buy' - произведена покупка или нет. 
Добавьте еще один столбец 'price', 
который содержит сумму всей покупки, если она совершена, и np.nan, если покупка не совершена.
"""
df_9 = pd.DataFrame({'product': ['товар_1', 'товар_3', 'товар_0', 'товар_3', 'товар_1'],
                     'product_price': [2000, 4000, 1000, 4000, 2000],
                     'count': [1, 1, 1, 4, 3],
                     'buy': [True, False, True, False, False]})

# print(df_9, end='\n'*2)

# Вариант 1
def my_func_9(series):
    if series.buy == True:
        price = series['product_price'] * series['count']
    else:
        price = np.nan

    return price

# df_9['price'] = df_9.apply(my_func_9, axis=1)

# Вариант 2
df_9['price'] = df_9.apply(lambda x: x['product_price'] * x['count'] if x['buy'] == True else np.nan, axis=1)



"""           # 10  
В DF содержится 
'product' - имя товара, 
'product_price' - цена товара,  
'count' - количество товаров в корзине, 
'buy' - произведена покупка или нет. Е
сли цена товара меньше 1500, то в 'count' записать 5, 
если от 1500 до 3000 включительно, то в 'count' записать 3, 
а если больше 3000, то в 'count' записать 1.
"""

df_10 = pd.DataFrame({'product': ['товар_4', 'товар_0', 'товар_1', 'товар_3', 'товар_2'],
                     'product_price': [5000, 1000, 2000, 4000, 3000],
                     'count': [np.nan, np.nan, np.nan, np.nan, np.nan],
                     'buy': [np.nan, np.nan, np.nan, np.nan, np.nan]})

# print(df_10, end='\n'*2)

# Вариант 1
# df_10['count'] = df_10.apply(lambda x: 5 if x['product_price'] < 1500 else (3 if 1500 <= x['product_price'] <= 3000 else 1),  axis=1)


# Вариант 2
def my_func_10(ser):
    if ser < 1500:
        count = 5
    elif 1500 <= ser <= 3000:
        count = 3
    else:
        count = 1
    return count

# df_10['count'] = df_10['product_price'].apply(my_func_10)


"""
В DF содержится 
'product' - имя товара, 
'product_price' - цена товара,  
'count' - количество товаров в корзине, 
'buy' - произведена покупка или нет. 
Если цена товара меньше 1500, то заменить ее на строку 'Покупать', 
если от 1500 до 3000 включительно, то заменить на строку 'Есть над чем подумать', 
а если больше 3000, то заменить на строку 'И думать нечего, не брать'.

"""

df_11 = pd.DataFrame({'product': ['товар_2', 'товар_1', 'товар_2', 'товар_4', 'товар_4'],
                     'product_price': [3000, 2000, 3000, 5000, 5000],
                     'count': [np.nan, np.nan, np.nan, np.nan, np.nan],
                     'buy': [np.nan, np.nan, np.nan, np.nan, np.nan]})

# print(df_11, end='\n'*2)


"""
'Покупать' 5
'Есть над чем подумать' 3
'И думать нечего, не брать' 0
"""

df_11['product_price'] = df_11['product_price'].apply(lambda x: 'Покупать' if x < 1500 else ('Есть над чем подумать' if 1500 <= x <= 3000 else 'И думать нечего, не брать'))

# print(df_11, end='\n'*2)

"""
В DF содержится 
'product' - имя товара, 
'product_price' - цена товара,  
'count' - количество товаров в корзине, 
'buy' - произведена покупка или нет. 
В столбце 'buy' значение False замените на 'Не оплачено', а значение True на 'Оплачено'.  
"""

df_12 = pd.DataFrame({'product': ['товар_4', 'товар_0', 'товар_2', 'товар_4', 'товар_4'],
                     'product_price': [5000, 1000, 5000, 1000, 4000],
                     'count': [2, 3, 2, 4, 3],
                     'buy': [False, True, False, False, False]})

df_12['buy'] = df_12['buy'].apply(lambda x: 'Не оплачено' if x == False else 'Оплачено')

# print(df_12, end='\n'*2)


"""     

"""

df_13 = pd.DataFrame({'product': ['товар_1', 'товар_2', 'товар_4', 'товар_1', 'товар_3'],
                     'product_price': [5000, 3000, 5000, 2000, 1000],
                     'count': [4, 2, 4, 2, 1], 'buy': [False, True, False, False, False]})

# print(df_13, end='\n'*2)


"""
В переменную prod запишите df дополнительно не указывая товар.
 В переменную prod_3 запишите df дополнительно указав 'товар_3'.
"""

# def func(series, prod=np.nan):
#     if series['buy'] or series['product'] == prod:
#         price = series['product_price'] * series['count']
#     else:
#         price = np.nan
#
#     return price

# def func(series, prod=np.nan):
#     if series['product'] == np.nan:
#         if series['buy']:
#             price = series['product_price'] * series['count']
#         else:
#             price = np.nan
#         return price
#     elif series['buy'] or series['product'] == prod:
#         price = series['product_price'] * series['count']
#     else:
#         price = np.nan
#
#     return price

# def func(series, prod=np.nan):
#     if prod != np.nan and series['product'] == prod:
#         ###
#         price = series['product_price'] * series['count']
#     else:
#         if series['buy']:
#             price = series['product_price'] * series['count']
#         else:
#             price = np.nan
#         return price
#     return price

# def func(series, **prod):
#     if prod:
#         if series['buy'] == True:
#             price_1 = series['product_price'] * series['count']
#         else:
#             price_1 = np.nan
#         price = price_1
#         return price
#     else:
#         if series['product'] == prod:
#             price_2 = series['product_price'] * series['count']
#         else:
#             price_2 = np.nan
#         price = price_2
#         return price
#     return price

#
# def func(series, prod=np.nan):
#     if prod is not np.nan:
#         if series['product'] == prod:
#             price = series['product_price'] * series['count']
#         else:
#             price = np.nan
#     else:
#         if series['buy'] == True:
#             price = series['product_price'] * series['count']
#         else:
#             price = np.nan
#     return price
#
# prod = df_13.copy()
# prod_3 = df_13.copy()
#
#
# prod['price'] = prod.apply(func, axis=1)
# # prod = df_13.copy()
# prod_3['price'] = prod_3.apply(func, axis=1, prod='товар_1')
# # prod_3 = df_13.copy()
#
#
# print(prod, end='\n'*2)
# print(prod_3, end='\n'*2)

# df_13['price'] = df_13.apply(lambda x: x['product_price']*x['count'] if x['buy'] else np.nan, axis=1)


# print(df_13, end='\n'*2)

def func(series, prod=None):
    if prod:
        if series['product'] == prod:
            price = series['product_price'] * series['count']
        else:
            price = np.nan

    else:
        if series['buy']:
            price = series['product_price'] * series['count']
        else:
            price = np.nan
    return price

prod = df_13.copy()
prod_3 = df_13.copy()


prod['price'] = prod.apply(func, axis=1)
# prod = df_13.copy()
prod_3['price'] = prod_3.apply(func, axis=1, prod='товар_1')
# prod_3 = df_13.copy()

# df_13['price'] = df_13.apply(func, axis=1, prod='товар_4')
# print(df_13)

# print(prod, end='\n'*2)
# print(prod_3, end='\n'*2)
