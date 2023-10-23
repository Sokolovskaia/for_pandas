import pandas as pd
import numpy as np


"""2.3 Методы apply()"""
# Упражнение 12
# В DF содержится 'product' - имя товара,
# 'product_price' - цена товара,
# 'count' - количество товаров в корзине,
# 'buy' - произведена покупка или нет.
# Добавьте еще один столбец 'price', который содержит сумму всей покупки,
# если она совершена, и np.nan, если покупка не совершена.
#
# Реализуйте функционал,
# при котором можно выбирать товар для которого будет подсчитываться значение в столбце 'price'.
# Если товар не указывать , значения в столбце 'price' будет посчитано как указано выше.
# def func(...):
#     ...
#     ...
#     ...
#
# df['price'] = df.apply(func, ..., prod='товар_1')
# В переменную prod запишите df дополнительно не указывая товар.
# В переменную prod_3 запишите df дополнительно указав 'товар_3'.




df_12 = pd.DataFrame({'product': ['товар_3', 'товар_2', 'товар_3', 'товар_1', 'товар_0', 'товар_2', 'товар_1', 'товар_3', 'товар_2', 'товар_3'],
                     'product_price': [5000, 3000, 5000, 2000, 1000, 3000, 2000, 5000, 3000, 4000],
                     'count': [4, 2, 4, 2, 1, 2, 2, 1, 2, 3],
                     'buy': [False, True, True, True, True, False, True, True, False, False]})

# Вариант_1
def func(x, prod=None):
    if prod:
        if x['product'] == prod and x['buy']:
            price = x['product_price'] * x['count']
        else:
            price = np.nan
    else:
        if x['buy']:
            price = x['product_price'] * x['count']
        else:
            price = np.nan
    return price

# Вариант 2
def func_2(x, prod=None):
    if (prod == None or x['product'] == prod) and x['buy']:
        price = x['product_price'] * x['count']
    else:
        price = np.nan
    return price

# Вариант 3
def func_3(x, prod=None):
    if (prod == None or x['product'] == prod) and x['buy']:
        return x['product_price'] * x['count']
    else:
        return np.nan


prod = df_12.copy()
prod_3 = df_12.copy()


prod['price'] = prod.apply(func_3, axis=1)
prod_3['price'] = prod_3.apply(func_3, axis=1, prod='товар_3')



"""     2.5 Группировка данных. Метод groupby()     """
# Упражнение 9.
# В программе создан файл с данными - "users.csv".
# Файл содержит три столбца:
# 'user' - содержит имена пользователей приложения,
# 'device' - устройство, с которого пользователи заходили в приложение
# ('PC' - компьютер, 'laptop' - ноутбук, 'phone' - смартфон),
# 'date' - дата когда пользователи заходили в приложение.
# Получите список\массив пользователей, которые заходили в приложение только с персонального компьютера('PC').
# Результат запишите в переменную user_list.

df_9 = pd.read_csv('users.csv', usecols=['user', 'device', 'date'])

df_9_gr = df_9.groupby('user')['device'].unique()
user_list_9 = df_9_gr[df_9_gr.isin(['PC'])].index.to_list()



# Упражнение 10.
# Получите список\массив пользователей, которые заходили в приложение со всех устройств.
df_10 = pd.read_csv('users.csv', usecols=['user', 'device', 'date'])
df_10_gr = df_10.groupby(['user']).agg(u_dev=('device', 'nunique'))
user_list_10 = df_10_gr[df_10_gr['u_dev']==3].index.to_list()




"""     3.1 Тип данных Datetime."""
# Упражнение 13.
# Получите DataFrame в котором есть столбцы 'user', 'date',
# а также столбец 'flag_reg'. В столбце 'flag_reg' стоит True,
# если user в этот день зарегистрировался и False, если нет.
# Первый заход
# Результат запишите в переменную new_df.


df_visits = pd.read_csv('users_3_1_16.csv', sep=':')
df_reg = pd.read_csv('date_reg_3_1_16.csv', sep=';')
df_merg = df_visits.merge(df_reg, how='left', on=['user'])
df_merg['dupl'] = df_merg.duplicated()

def func_13(x):
    if x['date_reg'] == np.nan:
        return False
    if x['date'] != x['date_reg'] or x['dupl']:
        return False
    else:
        return True

df_merg['flag_reg'] = df_merg.apply(func_13, axis=1)

new_df = df_merg[['user', 'date', 'flag_reg']].copy()



name = str(input())
print(f'Hello, {name}')

