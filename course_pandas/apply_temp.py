"""    Разобраться с методом apply   """
import pandas as pd
import numpy as np


"""
def my_func_3(series, *args):
    if not isinstance(series, pd.Series):   # Проверка
        raise Exception('Что-то не то передаешь?')
    if len(args) == 0:          #   МОЖНО ИСПОЛЬЗОВАТЬ ДЛЯ ЗАДАЧИ
        return '___'
    if len(args) > 3:
        raise Exception('Не многовато ли аргументов в args?')

"""


""""
Для задачи со студентами Через Словарь
Но для серии

arg_dict_m = {'товар_0': 'product_0',
              'товар_1': 'product_1',
              'товар_2': 'product_2',
              'товар_3': 'product_3',
              'товар_4': 'product_4'}
# Пример 1
new_ser_m_1 = ser_m.map(arg_dict_m)



"""
# import matplotlib.pyplot as plt
# plt.style.use('ggplot')  # Красивые графики
# plt.rcParams['figure.figsize'] = (15, 5)  # Размер картинок
#
# dict_plot = {'days': [1, 2, 3, 4, 5, 6, 7], 'berri': [200, 100, 300, 500, 700, 1500, 50]}
# df_plot = pd.DataFrame(dict_plot)
# # print(df_plot)
# df_plot.berri.plot(figsize=(15, 10))
# print(df_plot.berri.plot(figsize=(15, 10)))



""" РАЗНОЕ """
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

print(df)

for_pr_1 = df.shape #  возвращает количество строк и столбцов
for_pr_2 = df.columns

print(for_pr_2)