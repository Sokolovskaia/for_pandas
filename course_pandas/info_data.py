""" ТЕТРАДЬ++++++"""

"""     Методы head(), info(), describe() """
import pandas as pd
import numpy as np

df_i = pd.DataFrame({
    'col_1': [5, 6, 7, np.nan, 3],
    'col_2': [27, 6, 7, 4, 7],
    'col_3': ['a', 'b', 'c', 'd', 'i']},
    index=['row_1', 'row_2', 'row_3', 'row_4', 'row_5'])

series_i = pd.Series(
    [5, 6, np.nan, 1, 7],
    index=['row_10', 'col_2', 'row_3', 'row_4', 'row_5'])

"""         МЕТОД info()
 
- Класс объекта.
- Сведения об индексе: класс, количество строк, с какого индекса начинается и каким кончается.
- Количество столбцов.
- Сведения о столбцах: имена столбцов, количество строк без пропусков, тип данных в столбцах.
- Типы данных и их количество.
- Объем памяти, который занимает DF или Series.
"""

# print(df_i.info(), end='\n'*2)
# series_i.info()




"""     Метод head().
С помощью данного метода вы получите первые строки DF или серии для того, 
чтобы понять структуру импортированных данных. 
По умолчанию выводится 5 строк, но если в метод передать число, к примеру 10, 
то получите соответствующее количество строк. """

for_print_1 = df_i.head(2)
for_print_2 = series_i.head(4)



"""
Метод tail().
С помощью данного метода вы получите последние строки DF или серии для того, 
чтобы понять структуру импортированных данных. 
По умолчанию выводится 5 строк, но если в метод передать число, к примеру 10, 
то получите соответствующее количество строк. 
"""

for_print_3 = df_i.tail(1)
for_print_4 = series_i.tail(3)



"""
Метод describe().
помогает получить некоторые статистические данные из числовых столбцов.

count - количество элементов, значения Nan не учитываются.
mean - среднее значение в столбце.
std - стандартное отклонение.
min - минимальное значение в столбце.
20%, 50%, 75% - соответствующие процентили.
max - максимальное значение в столбце.

"""

for_print_5 = df_i.describe()
for_print_6 = series_i.describe()
#
# print(for_print_5, end='\n'*2)
# print(for_print_6, end='\n'*2)





df = pd.DataFrame({'name': ['Имя_1', 'Имя_2', 'Имя_3', 'Имя_4', 'Имя_5'],
                   1: [True, True, True, True, False],
                   2: [False, True, True, False, True],
                   3: [True, False, True, True, True],
                   4: [True, True, True, False, False],
                   5: [True, False, True, True, False]})

print(df)
# DataFrame.all(axis=0, bool_only=False, skipna=True, **kwargs)
# flag_ser = df.all(axis=1,  bool_only=True)
flag = df.all(axis=1, bool_only=True).isin([True]).any()
print(flag)



# ВАРИАНТ 1
# df = df.set_index('name')

# df['sum'] = df.agg(np.sum, axis=1)
# # print(df)
# flag_count = df['sum'].isin([5]).sum()
# if flag_count > 0:
#     flag = True
# else:
#     flag = False


