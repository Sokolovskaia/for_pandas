""" ТЕТРАДЬ++++++"""

import pandas as pd
import numpy  as np

df_1_a = pd.DataFrame({
    'col_1': [5, 6, np.nan, 3, 7],
    'col_2': [27, 6, 7, 40, 70],
    'col_3': [1, 45, 6, 62, 7]},
    index=['row_1', 'row_2', 'row_3', 'row_4', 'row_5'])

df_2_a = pd.DataFrame({
    'col_1': [5, 6, 7, np.nan, 3],
    'col_2': [27, 6, 7, 4, 7],
    'col_3': [1, 45, 6, 62, 7]},
    index=['row_1', 'row_2', 'row_3', 'row_4', 'row_5'])

series_a = pd.Series([5, 6, np.nan, 1, 7], index=['row_10', 'col_2', 'row_3', 'row_4', 'row_5'])

"""     Арифметические операции с СЕРИЕЙ    """

"""     К серии прибавить значение, то прибавляется ко всем элементам серии. Исходная серия не меняется"""
# print(series_a)
#
# print(series_a + 5) # прибавление к Nan всегда возвращает Nan
# print(series_a + np.nan)    #   вернет Nan

# print(series_a + [1, 2, 3, 4, 5])   # список должен содержать такое же количество элементов, как и серия

# print(df_1_a['col_1'])

series_df_summ = series_a + df_1_a['col_1']     #   если индекса нет (нет одинаковых), то считается сложением с Nan и возвращает Nan
# print(series_df_summ)



"""     Арифметические операции с ДАТА ФРЕЙМОМ (DF)      """

""" прибавление к каждому элементу """

# print(df_1_a + 10)

""" Прибавление списка. Количество элементов в списке должно соответствовать кол-во СТОЛБЦОВ    """

# print(df_1_a + [100, 200, 300])


"""     Арифметические операции между двумя DF"""

df_3_a = df_1_a.head(3)
df_4_a = df_1_a[['col_1', 'col_2']]

# print(df_3_a, end='\n'*2)
# print(df_4_a)
# print(df_3_a + df_4_a)      # выравнивание индексов


"""
add() - операция сложения
sub() - операция вычетания
div() - операция деления
mul() - операция умножения
pow() - операция возведения в степень
mod() - операция вычисления остатка от деления

"""


add_df_1 = df_1_a.add(100)
add_df_2 = df_1_a.add([100, 200, 300])
add_df_3 = df_1_a.add(df_2_a)
add_series_1 = series_a.add(1000)
add_series_2 = series_a.add(df_1_a['col_1'])

"""     Выбрать ось (axis) 1 или 0. По умолчанию 1 (столбцы)   """

add_df_4 = df_1_a.add([100, 200, 300], axis=1)      #   по столбцам
add_df_5 = df_1_a.add([100, 200, 300, 400, 500], axis=0)    # по строкам

add_series_3 = df_1_a.add(series_a, axis=0)

# print(df_1_a, end='\n'*2)
# print(series_a, end='\n'*2)
# print(add_series_3)


"""   Аргумент fill_value=....  Заполняет пропуски указанным значением"""

df_5_a = df_1_a.head(3)
df_6_a = df_2_a[['col_1', 'col_2']]

# print(df_5_a, end='\n'*2)
# print(df_6_a, end='\n'*2)


add_df_6 = df_5_a.add(df_6_a, fill_value=99999)

# print(add_df_6)

"""     ЗАДАЧИ      """
df = pd.DataFrame({'год рождения': [88, 89, 90, 91], 'стаж работы': [3.25, 4.5, 5.75, 6.25], 'зарплата': [60, 70, 80, 90]})


# print(df, end='\n'*2)

# new_df = df * [12, 1000]
new_df = df.mul([1, 12, 1000])
new_df['год рождения'] = new_df['год рождения'] + 1900
# print(new_df)

ser = pd.Series([10, 20, 30, 40, 50, 60, 70, 80])

new_ser = ser - ser.mean()

# print(new_ser)


df_11 = pd.DataFrame({'age': [19, 20, 23, 24], 'стаж работы': [3, 4, 5, 6], 'зарплата': [60000, 70000, 80000, 90000]})
ser_11 = pd.Series([5, 22.2, 80000], index=['средний стаж работы', 'средний возраст', 'средняя зарплата'])



# new_ser_11 = ser_11.to_list()
# new_ser_11[0], new_ser_11[1] = new_ser_11[1], new_ser_11[0]
#
# print(df_11, end='\n'*2)
# print(new_ser_11, end='\n'*2)
# new_df_11 = df_11.sub(new_ser_11)
# print(new_df_11)


new_df = df_11.sub([ser_11[1], ser_11[0], ser_11[2]])

ser_22 = pd.Series([10000, 20000, 30000, 40000])
df_22 = pd.DataFrame({'год рождения': [88, 89, 90, 91], 'стаж работы': [3.25, 4.5, 5.75, 6.25], 'зарплата': [60, 70, 80, 90]})

# print(df_22, end='\n'*2)
# print(ser_22, end='\n'*2)

new_df_22 = df_22.add(ser_22, axis=0)

# print(new_df_22)

