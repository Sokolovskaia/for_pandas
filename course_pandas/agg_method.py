""" ТЕТРАДЬ++++++"""


"""     Метод agg()
"""

import pandas as pd
import numpy as np

df_a_1 = pd.DataFrame([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9],
                       [np.nan, np.nan, np.nan]], columns=['col_1', 'col_2', 'col_3'])

"""
Функции агрегации:
- min()
- max()
- mean()    Не учитывается Nan
- sum()
- std()
- count()   Не учитывается Nan
- first()
- last()
"""

for_print_1 = df_a_1.min()
for_print_2 = df_a_1.mean()

# for_print_3 = df_a_1['col_3'].sum()
for_print_3 = df_a_1.col_3.sum()


"""     Метод agg()
Позволяет применить одну или более функцию агрегации по указанной оси
Принимает два аргумента - функцию и ось (по умолчанию axis=0)
"""

for_print_4 = df_a_1.agg('mean')
for_print_5 = df_a_1.agg(np.mean)
for_print_6 = df_a_1.agg([np.max, np.sum, np.mean])
for_print_7 = df_a_1.agg(np.max, axis=1)
for_print_8 = df_a_1['col_3'].agg([np.min, np.max, np.mean])


def my_func_a(series):
    return series.min() + 100

for_print_9 = df_a_1.agg(my_func_a)



"""     Агрегация отдельно для каждого столбца """

for_print_10 = df_a_1.agg({'col_1': [np.min, np.sum], 'col_3': 'mean'})


"""     Именованная агрегация 
 навзание=(столбец, функция))"""

for_print_11 = df_a_1.agg(min_col_1=('col_1', 'min'), max_col_2=('col_2', np.max))
for_print_12 = df_a_1.agg(min_col_1=('col_1', 'min'), my_func=('col_2', my_func_a))

# print(df_a_1, end='\n'*2)

# print(for_print_12)




"""     ЗАДАЧИ 2.4  """
# Упражнение 2
# print(df_a_1, end='\n'*2)

new_ser = df_a_1.agg(np.sum)

# print(new_ser)

# Упражнение 3

df = pd.DataFrame([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9],
                       [np.nan, np.nan, np.nan]], columns=['col_1', 'age', 'col_3'])

mean_age = df.age.agg('mean')

# Упражнение 3
# Подсчитайте количество элементов в каждом столбце df без учета пропусков.

new_ser_3 = df.agg('count')

# Упражнение 4
# Подсчитайте сумму в каждой строке df. Воспользуйтесь методом agg() и функцией Numpy - np.sum().

new_ser_4 = df.agg(np.sum, axis=1)

# Упражнение 6

new_ser_6 = df.col_1.agg([np.min, np.max, np.sum])



# Упражнение 7

new_ser_7 = df.agg({'col_1': [np.sum, np.mean], 'col_3': np.mean})



# Упражнение 8

"""
В столбце 'name' указано имя студента, 
столбцы с 1 до 50 - это номера задач. 
Если значение в DF равно 1, то есть верное решение задачи, 
если 0, то есть только неверные решения, 
если Nan, то нет отправленных решений. 

Импортируйте файл и подсчитайте сколько правильных решений у каждого студента?
"""



df_8 = pd.read_csv('stud.csv', index_col=['name'])

new_ser_8 = df_8.agg(np.sum, axis=1)



"""
Если значение в DF равно 1 - это значит, есть верное решение задачи, 
если 0, есть только неверное решения, 
если Nan, то нет отправленных решений. 

Импортируйте файл и подсчитайте сколько не правильных решений у каждого студента?
"""

# Упражнение 9

new_ser_9 = pd.read_csv('stud.csv', index_col=['name']).isin([0]).sum(axis=1)

# Упражнение 10
# Импортируйте файл и подсчитайте сколько задач с неотправленными решениями у каждого студента?
new_ser_10 = pd.read_csv('stud.csv', index_col=['name']).isna().sum(axis=1)

# Упражнение 11

new_df_11 = pd.read_csv('stud.csv', index_col=['name']).isin([1]).agg([np.sum, np.mean])


# Упражнение 12
new_df_12 = pd.read_csv('stud.csv', index_col=['name']).isin([0, np.nan]).agg([np.sum, np.mean])

# Упражнение 13
new_df_13 = pd.read_csv('stud.csv', index_col=['name']).isin([1]).agg(sum_solved=('5', np.sum), mean_solved=('5', np.mean))


# print(df_9, end='\n'*2)
print(new_df_13)
