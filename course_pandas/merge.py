"""     Метод MERGE() """

import pandas as pd
import numpy as np

df_1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3'],
                     'C': ['C0', 'C1', 'C2', 'C3'],
                     'D': ['D0', 'D1', 'D2', 'D3']},
                    index=[0, 1, 2, 3])
df_2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                     'B': ['B4', 'B5', 'B6', 'B7'],
                     'C': ['C4', 'C5', 'C6', 'C7'],
                     'D': ['D4', 'D5', 'D6', 'D7']},
                    index=[1, 2, 3, 4])

df_3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                     'B': ['B8', 'B9', 'B10', 'B11'],
                     'C': ['C8', 'C9', 'C10', 'C11'],
                     'D': ['D8', 'D9', 'D10', 'D11']},
                    index=[2, 3, 4, 5])

"""     Метод concat()  """
for_p_1 = pd.concat([df_1, df_2, df_3]) # столбцы, сохранились исходные индексы
for_p_2 = pd.concat([df_1, df_2, df_3], ignore_index=True)
for_p_3 = pd.concat([df_1, df_2, df_3], axis=1) # объединение строк с одинаковыми индексами

"""     Метод merge()  
pd.merge(left_df, right_df, ...)  --- функция
left_df.merge(right_df, ...)  ---  метод
"""

df_4 = pd.DataFrame({'client_id': [100103, 21990, 455323, 100103, 21990, 455323, 455323, 21990, 455323],
                     'product': ['product_2', 'product_2', 'product_1', 'product_1', 'product_1', 'product_3', 'product_3', 'product_3', 'product_6']})



df_5 = pd.DataFrame({'product': ['product_1', 'product_2', 'product_3', 'product_4', 'product_5'],
                     'price': [1000, 2000, 3000, 4000, 5000]})


"""     Аргумент how=   
левый - тот, к которому вызывается метод
правый - аргумент который передаем в метод
"""
for_p_4 = df_4.merge(df_5, how='left')    #   только то, что есть слева
for_p_5 = df_4.merge(df_5, how='right')    #   только то, что есть  справа
for_p_6 = df_4.merge(df_5, how='inner')    #   только то, что есть в обоих (по умолчанию)
for_p_7 = df_4.merge(df_5, how='outer')    #   все элементы из обоих

"""     Аргумент on=   
"""

df_6 = pd.DataFrame({'client_id': [100103, 21990, 455323, 100103, 21990, 455323, 455323, 21990, 455323],
                     'product': ['product_2', 'product_2', 'product_1', 'product_1', 'product_1', 'product_3', 'product_3', 'product_3', 'product_6'],
                     'color_prod': ['black', 'white', 'white', 'white', 'white', 'black', 'black', 'white', 'white']})



df_7 = pd.DataFrame({'product': ['product_1', 'product_2', 'product_3', 'product_4', 'product_5'],
                     'price': [1000, 2000, 3000, 4000, 5000],
                     'color_prod': ['black', 'black', 'black', 'white', 'white']})


for_p_8 = df_6.merge(df_7, how='inner', on='product')   # когда есть одинаковое имя в обоих DF

for_p_9 = df_6.merge(df_7, how='left', on=['product', 'color_prod'])   # когда есть одинаковое имя в обоих DF


""" Если столбцы имеют разные имена  """
df_6.rename(columns={'product': 'prod'}, inplace=True)
df_7.rename(columns={'color_prod': 'color'}, inplace=True)

for_p_10 = df_6.merge(df_7,
                      how='left',
                      left_on=['prod', 'color_prod'],
                      right_on=['product', 'color'])



"""     Аргумент suffixes=...."""


df_8 = pd.DataFrame({'product': ['product_1', 'product_2', 'product_3', 'product_4', 'product_5'],
                     'count': [10, 20, 30, 40, 50]})

df_9 = pd.DataFrame({'product': ['product_3', 'product_4', 'product_5', 'product_6', 'product_7'],
                     'count': [100, 200, 300, 400, 500]})

for_p_11 = df_8.merge(df_9, how='outer', on='product')
for_p_12 = df_8.merge(df_9, how='outer', on='product', suffixes=('_shop_left', '_shop_right'))  # свои названия


# print(df_8, end='\n'*2)
# print(df_9, end='\n'*2)
#
#
# print(for_p_12, end='\n'*2)



"""     ЗАДАЧИ      """
N_client = 10
N_product = 15

client_1 = {i: f'client_{i}' for i in range(N_client)}
client_2 = {i: f'client_{i}' for i in range(3, N_client+3)}

data_product = {i: f'product_{i}' for i in range(N_product )}
price_1 = {i: (i+1)*1000 for i in range(15)}
price_2 = {i: (i+1)*900 for i in range(15)}

client_list_1 = np.random.randint(0, N_client, 100)
client_list_2 = np.random.randint(3, N_client+3, 100)

product_list = np.random.randint(0, N_product , 100)

shop_1 = pd.DataFrame({'client': client_list_1,
                       'product': product_list,
                       'price': product_list}).replace({'client': client_1, 'product': data_product, 'price': price_1})
shop_2 = pd.DataFrame({'client': client_list_2,
                       'product': product_list,
                       'price': product_list}).replace({'client': client_2, 'product': data_product, 'price': price_2})
product = pd.DataFrame({'product': data_product.values(),
                        'color': np.random.choice(['black', 'red', 'green', 'white', 'blue'], 15),
                        'weight': np.random.randint(10, 20, 15)*10})


df_11 = pd.DataFrame({'client': ['client_8', 'client_4', 'client_3', 'client_6', 'client_6'],
                     'product': ['product_7', 'product_10', 'product_1', 'product_3', 'product_5']})

df_12 = pd.DataFrame({'client': ['client_8', 'client_4', 'client_3', 'client_6', 'client_6'],
                     'product': ['product_4', 'product_8', 'product_11', 'product_8', 'product_14']} )


df_11 = df_11.set_index('client')
df_12 = df_12.set_index('client')


# new_df_11 = pd.concat([df_11, df_12], axis=1)
# new_df_12 = pd.concat([df_11, df_12])
# Упражнение 4
shop_11 = pd.DataFrame({'client': ['client_6', 'client_8', 'client_2', 'client_1', 'client_7'],
                       'product': ['product_12', 'product_14', 'product_5', 'product_8', 'product_6'],
                       'price': [13000, 15000, 6000, 9000, 7000]})

product_11 = pd.DataFrame({'product': ['product_0', 'product_1', 'product_2', 'product_3', 'product_4', 'product_5', 'product_6', 'product_7', 'product_8', 'product_9', 'product_10', 'product_11', 'product_12', 'product_13', 'product_14'],
                           'color': ['green', 'blue', 'black', 'blue', 'white', 'green', 'blue', 'black', 'blue', 'white', 'green', 'green', 'black', 'black', 'green'],
                           'weight': [190, 170, 100, 160, 180, 170, 170, 120, 140, 180, 190, 110, 120, 170, 100]})

new_df_13 = shop_11.merge(product_11, how='left', on='product')

# Упражнение 5
shop_21 = pd.DataFrame({'client': ['client_6', 'client_8', 'client_2', 'client_1', 'client_7'],
                       'product': ['product_12', 'product_12', 'product_5', 'product_8', 'product_6'],
                       'price': [13000, 15000, 6000, 9000, 7000]})

shop_22 = pd.DataFrame({'client': ['client_6', 'client_8', 'client_2', 'client_1', 'client_7'],
                       'product': ['product_12', 'product_14', 'product_5', 'product_8', 'product_8'],
                       'price': [13, 15, 6, 9, 7]})

new_df_22 = shop_21.merge(shop_22.groupby(['product'], as_index=False)['price'].mean(), how='left', on=['product'])

# Упражнение 6

shop_61 = pd.DataFrame({'client': ['client_1', 'client_1', 'client_22', 'client_1', 'client_1'],
                       'product': ['product_5', 'product_5', 'product_14', 'product_8', 'product_7'],
                       'price': [13000, 15000, 6000, 9000, 7000]})

shop_62 = pd.DataFrame({'client': ['client_6', 'client_6', 'client_2', 'client_9', 'client_1'],
                       'product': ['product_12', 'product_5', 'product_5', 'product_8', 'product_7'],
                       'price': [13, 15, 6, 9, 7]})

new_df_6 = shop_61.groupby(['product'], as_index=False)['price'].mean().merge(shop_62.groupby(['product'])['price'].mean(), how='left', on='product', suffixes=('_shop_1', '_shop_2'))


# Упражнение 7
# shop_61_gr = shop_61.groupby(['client']).agg(sum=('price', np.sum))
# shop_62_gr = shop_62.groupby(['client']).agg(sum=('price', np.sum))
# new_df_7 = shop_61_gr.merge(shop_62_gr, how='outer', on='client', suffixes=('_shop_1', '_shop_2')).reset_index()
new_df_7 = shop_61.groupby(['client']).agg(sum=('price', np.sum)).merge(shop_62.groupby(['client']).agg(sum=('price', np.sum)), how='outer', on='client', suffixes=('_shop_1', '_shop_2')).reset_index()

# Упражнение 8

# Подробный вариант
# shop_81_for_1 = shop_61[shop_61['client'] == 'client_1']    # выборка из 1 магазина только покупки клиента_1
# shop_82_gr = shop_62.groupby(['product'])['price'].mean()   # справочник средняя цена товаров по 2 магазину
#
# new_df_8 = shop_81_for_1.merge(shop_82_gr, how='left', on='product')    # сопаставили
# sale = new_df_8['price_x'].sum() - new_df_8['price_y'].sum()
# Схлопнули

new_df_8 = shop_61[shop_61['client'] == 'client_1'].merge(shop_62.groupby(['product'])['price'].mean(), how='left', on='product')    # сопаставили
sale = new_df_8['price_x'].sum() - new_df_8['price_y'].sum()




# Упражнение 9
# Развернутый
df_device = pd.read_csv('devices__1_.csv', usecols=['id', 'device'])
df_users = pd.read_csv('user_merge__1_.csv', usecols=['user', 'id_device', 'action'])

new_df_9 = df_users.merge(df_device, how='left', left_on='id_device', right_on='id')
user_list_t = new_df_9[new_df_9['device']=='PC']
user_list = user_list_t['user'].unique()

# Схлопнуть


# Упражнение 10
# Получите список\массив устройств, с которыx пользователи заходили в приложение.

df_device = pd.read_csv('devices__1_.csv', usecols=['id', 'device'])
df_users = pd.read_csv('user_merge__1_.csv', usecols=['id_device'])

df_user_dev = df_users.merge(df_device, how='left', left_on='id_device', right_on='id')['device'].unique()


# Упражнение 11
# Получите список\массив пользователей из Санкт-Петербурга, заходивших в приложение через телефон.

df_device = pd.read_csv('devices__1_.csv', usecols=['id', 'device'])
df_users = pd.read_csv('user_merge__1_.csv', usecols=['user', 'id_device', 'id_region'])
df_region = pd.read_csv('region__1_.csv', usecols=['id', 'region'])

df_user_dev_11 = df_users.merge(df_device, how='left', left_on='id_device', right_on='id')
df_user_dev_reg_11 = df_user_dev_11.merge(df_region, how='left', left_on='id_region', right_on='id')
user_list_11 = df_user_dev_reg_11[(df_user_dev_reg_11['device'] == 'phone') & (df_user_dev_reg_11['region'] == 'Санкт-Петербург')]['user'].unique()



# Упржнение 12
# Получите список\массив с уникальными пользователями из Санкт-Петербурга и Москвы,
# заходивших в приложение с трех устройств - 'PC', 'laptop' и 'phone'.
df_device = pd.read_csv('devices__1_.csv', usecols=['id', 'device'])
df_users = pd.read_csv('user_merge__1_.csv', usecols=['user', 'id_device', 'id_region'])
df_region = pd.read_csv('region__1_.csv', usecols=['id', 'region'])

df_user_dev_12 = df_users.merge(df_device, how='left', left_on='id_device', right_on='id')
df_user_dev_reg_12 = df_user_dev_12.merge(df_region, how='left', left_on='id_region', right_on='id')

# Вариант 1
# user_list_12 = df_user_dev_reg_12[df_user_dev_reg_12['region'].isin(['Москва', 'Санкт-Петербург'])]
# user_list_12_gr = user_list_12.groupby(['user'])['device'].unique()
#
# def my_func_12(ser):
#     if np.array_equal(ser, ['PC', 'laptop', 'phone']):
#         return ser
#
# user_list_12_gr_itog = user_list_12_gr.apply(my_func_12).dropna().index.to_list()
#

# Вариант 2
user_list_12_gr = df_user_dev_reg_12[df_user_dev_reg_12['region'].isin(['Москва', 'Санкт-Петербург'])].groupby(['user'])['device'].unique()

user_list_12_gr_itog = user_list_12_gr.apply(lambda x: x if np.array_equal(x, ['PC', 'laptop', 'phone']) else np.nan).dropna().index.to_list()

# print(user_list_12_gr_itog)

