"""     Метод GROUPBY() """

import pandas as pd
import numpy as np


df_g = pd.DataFrame({
    'Имя': ['name_1', 'name_2', 'name_3', 'name_3', 'name_3', 'name_2', 'name_4'],
    'Город_работы': ['city_1', 'city_2', 'city_3', 'city_3', 'city_4', 'city_1', np.nan],
    'Как_долго_работал': [12, 24, 36, 12, 48, 5, np.nan]})

# print(df_g, end='\n'*2)

for_p_1 = df_g.groupby('Имя')   # врзвращает объект, с помощью к-го можно получить все группы
for_p_2 = df_g.groupby(['Имя', 'Город_работы'])

"""     В ЦИКЛЕ """
# for name, group in for_p_1:
#     print(name)
#     print(group)

# обычно используют группировку. чтобы далее использовать агрегирующие функции
"""     Агрегирующие функции """
for_p_3 = df_g.groupby('Город_работы').sum()


"""     аргуемнт dropna= (по умол. True)   Чтобы учитывались пропуски - указать False """
for_p_4 = df_g.groupby('Город_работы', dropna=False).sum()


"""     аргуемнт as_index= (по умол. True)   Сохранить идекс """
for_p_5 = df_g.groupby('Имя', as_index=False).sum()


"""     df.groupby(колонка/колонки для группировки, ....)[столбец/столбцы].метод_агрегации()    """
for_p_6 = df_g.groupby('Имя')['Как_долго_работал'].sum()
for_p_7 = df_g.groupby(['Имя', 'Город_работы']).count()
for_p_8 = df_g.groupby(['Имя', 'Город_работы'], dropna=False).count()
for_p_9 = df_g.groupby(['Имя', 'Город_работы'], dropna=False).count().rename(columns={'Как_долго_работал':'count'})
for_p_10 = df_g.groupby('Имя')['Город_работы'].nunique()



""" К разеным столбцам применять разную агрегацияю """

for_p_11 = df_g.groupby('Имя').agg({'Как_долго_работал': np.sum})

for_p_12 = df_g.groupby('Имя').agg({'Город_работы': 'count', 'Как_долго_работал': [np.sum, np.max]})

for_p_13 = df_g.groupby('Имя', as_index=False).agg(count_jobs=('Город_работы', 'count'), experience=('Как_долго_работал', np.sum))


# print(df_g, end='\n'*2)
#
# print(for_p_13)


"""
Как было сказано в видео метод groupby() является генератором. 
Это значит, что он последовательно будет возвращать новую группу при каждом обращении к нему. 

В уроке про метод apply() говорилось, что в функцию, которая используется в методе, 
передается либо серия, либо массив Numpy, либо значения серии. 
При использовании apply() совместно с groupby() в функцию будет целиком передаваться тот объект, 
который возвращает groupby().

К примеру, df.groupby(...)["col_2"].apply( my_func ) 
при такой записи в my_func будет поочереди из каждой группы передан столбец "col_2" в виде серии. 
Если записать так df.groupby(...)[["col_2"]].apply( my_func ), 
обратите внимание на двойные квадратные скобки, 
в my_func будет поочереди из каждой группы передан столбец "col_2" уже в виде DataFrame. 

"""



"""     ЗАДАЧИ  """

N_client = 10
N_product = 15

client = {i: f'client_{i}' for i in range(N_client)}
product = {i: f'product_{i}' for i in range(N_product )}
price = {i: (i+1)*1000 for i in range(N_product)}

client_list = np.random.randint(0, N_client, 100)
product_list = np.random.randint(0, N_product, 100)

df = pd.DataFrame({'client': client_list,
                   'product': product_list,
                   'price': product_list}).replace({'client': client, 'product': product, 'price': price})


"""     Не из курса """
df_nn = pd.DataFrame({'team': ['A', 'B', 'B', 'B', 'B', 'M', 'M', 'M'],
 'position': ['G', 'G', 'F', 'G', 'F', 'F', 'C', 'C'],
 'assists': [5, 7, 7, 8, 5, 7, 6, 9],
 'rebounds': [11, 8, 10, 6, 6, 9, 6, 10]})

# print(df_nn)
# 1) сгруппировать по столбцам «команда» и «позиция» и найти средние передачи:

df_nn_1 = df_nn.groupby(['team', 'position']).agg({'assists': ['mean']}).reset_index()


# 2) переименования столбцов в результирующем DataFrame
df_nn_2 = df_nn.groupby(['team', 'position']).agg({'assists': ['mean']}).reset_index()
df_nn_2.columns = ['team', 'pos', 'mean_assists']



# 3) найти медиану и максимальное количество подборов, сгруппированных по столбцам «команда» и «позиция»:
df_nn_3 = df_nn.groupby(['team', 'position']).agg({'rebounds': ['median', 'max']}).reset_index()


# print(df_nn_3)

# print(df, end='\n'*2)

# Упражнение 1
# Подсчитайте сумму которую потратил каждый клиент.
# Результат запишите в переменную new_ser, он должен быть представлен в виде серии данных.

new_ser_1 = df.groupby('client')['price'].sum()


# Упражнение 2
# Подсчитайте сколько товаров купил каждый клиент.
# Результат запишите в переменную new_ser, он должен быть представлен в виде серии данных.

new_ser_2 = df.groupby('client')['product'].count()

# Упражнение 3
# Подсчитайте какое количество разных товаров купил каждый клиент.
# Результат запишите в переменную new_ser.

new_ser_3 = df.groupby('client')['product'].nunique()

# Упражнение 4
# Подсчитайте для каждого клиента какие товары и сколько раз он их покупал.
# Столбец с количеством покупок назовите "count". Результат запишите в переменную new_df.

new_df_4 = df.groupby(['client', 'product'], as_index=False).agg(count=('product', 'count'))


# Упражнение 5
# Подсчитайте сколько раз покупали и сколько было потрачено на каждый товар всеми клиентами.
# Столбец с количеством покупок назовите "count",
# а столбец с суммой потраченных денег "sum_price". Результат запишите в переменную new_df.

new_df_5 = df.groupby('product').agg(count=('product', 'count'), sum_price=('price', np.sum) )


# Упражнение 6
# Каждому продукту сопоставьте массив содержащий клиентов (массив с уникальными значениями),
# которые этот товар покупали.
# Результат запишите в переменную new_ser.




new_ser_6 = df.groupby('product')['client'].unique()


# Упражнение 7.
#
# Подсчитайте сколько раз каждый клиент покупал "product_2" .
# Данные представьте в виде DF.
# Столбец с количеством покупок назовите "product_2".
# Результат запишите в переменную new_df.


# Вариант 1
# df['product'] = df['product'].apply(lambda series: series if series == 'product_2' else np.nan)
new_df_7 = df.groupby(['client']).agg(product_2=('product', 'count'))


# Вариант 2

new_df_7_2 = df.groupby('client')[['product']].apply(lambda x: (x =='product_2').sum()).rename(columns={'product': 'product_2'})



# Упражнение 8
# Подсчитайте сколько раз каждый клиент покупал "product_3"
# и сколько он потратил денег на этот товар.
# Данные представьте в виде DF. Столбец с количеством покупок назовите "product_3",
# а столбец с суммой потраченных денег "sum_price".
# Результат запишите в переменную new_df.
df_88 = pd.DataFrame({'client': client_list,
                   'product': product_list,
                   'price': product_list}).replace({'client': client, 'product': product, 'price': price})

def my_f(ser):
    if ser['product'] == 'product_3':
        ser['product'] = 1
        ser['price'] = ser['price']
    else:
        ser['product'] = 0
        ser['price'] = 0
    return ser
new_df_88 = df_88.apply(my_f, axis=1).groupby(['client']).agg(product_3=('product', np.sum), sum_price=('price', np.sum))


# Упражнение 9
# В программе создан файл с данными - "users.csv".
# Файл содержит три столбца: 'user' - содержит имена пользователей приложения,
# 'device' - устройство, с которого пользователи заходили в приложение
# ('PC' - компьютер, 'laptop' - ноутбук, 'phone' - смартфон),
# 'date' - дата когда пользователи заходили в приложение.
# Получите список\массив пользователей, которые заходили в приложение только с персонального компьютера('PC').
# Результат запишите в переменную user_list.
# Скачайте файл users.csv, чтобы решить упражнение локально, перед отправкой его на проверку.

df_9 = pd.read_csv('users.csv', usecols=['user', 'device'])
"""     НАЧАЛО       """
print(df_9)

# df_9_new = df_9.groupby(['user'])['device'].unique()











"""     КОНЕЦ       """

# Упражнение 11.
# В программе создан файл с данными - "users_action.csv".
# Файл содержит четыре столбца: 'user' - содержит имена пользователей приложения,
# 'device' - устройство, с которого пользователи заходили в приложение
# ('PC' - компьютер, 'laptop' - ноутбук, 'phone' - смартфон),
# 'action' - совершил пользователь целевое действие или нет(True - совершил, False - не совершил),
# 'date' - дата когда пользователи заходили в приложение.
# Получите DF, показывающий, сколько раз пользователи заходившие в приложение со смартфона
# совершали целевое действие.

df_11 = pd.read_csv('users_action.csv', usecols=['user', 'device', 'action'])

new_df_11 = df_11[df_11.device == 'phone'].groupby('user')[['action']].apply(lambda x: (x==True).sum()).rename(columns={'action':'action_True'})
# print(new_df_11)




