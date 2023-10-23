""" ТЕТРАДЬ++++++"""

import pandas as pd
import numpy as np


df_1 = pd.DataFrame({'col_1': [16, 5, 40, 3, 2, 1],
                     'col_2': [6, 54, 4, 3, 28, 1],
                     'col_3': [6, 5, 4, 3, 2, 1],
                     'col_4': [63, 5, 45, 3, 2, 12]})
df_1.set_index(['col_1', 'col_4'],   #    Определить столбец или столбцы (мультииндекс, который будет индексом
                      # append=True, #   сохранить столбец с первоначальными индексами
                      inplace=True)
# print(df_1)

df_1.reset_index(['col_4'])  #   вернуть столбец из индекса в обычный столбец

df_1.reset_index(inplace=True)  # все уровни индексов были переведены в столбцы


df_2 = pd.DataFrame({'col_1': [16, 5, 40, 3, 2, 1],
                     'столбец_2': [6, 54, 4, 3, 28, 1],
                     'col 3': [6, 5, 4, 3, 2, 1],
                     'col_4': [63, 5, 45, 3, 2, 12]})

"""     Можно обратиться по имени столбцы в ДФ   """

col_to_series = df_2['col 3']    #  возвращает серию
col_to_df = df_2[['col 3']]      #   возвращает дата фрейм (можно несколько столбцов выбрать

# print(col_to_series, type(col_to_series))
# print(col_to_df, type(col_to_df))

df_2[['col_1', 'столбец_2']] = 1    #   заменить значения для текущих столбцов
df_2['new_col_5'] = 2     #   новый столбец
df_2['new_col_6'] = df_2[['col 3']]    #   создать новый столбец и передать туда данные из серии
del df_2['new_col_6']   #   удаление столбца

# print(df_2[[False, False, True, True, False, False]])  #  True - строка, котрую вернуть, не больше количества столбцов (?)

df_2[[False, False, True, True, False, False]] = 100  #  присвоить значение выбранным строкам
df_3 = df_2[[False, False, True, True, False, False]][['столбец_2']]    # вернуть в выбранном столбцу определенные строки

""" Можно обратиться к столбцу, если название соответствует условиям верного написания имен """
# print(df_2.new_col_5)
# print(pd.DataFrame(df_2.new_col_5))
# print(df_2)

df_11 = df_2[['col_1']]
print(type(df_11))