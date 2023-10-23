""" ТЕТРАДЬ++++++"""


import pandas as pd
import numpy as np


list_index = list('qwqityui')
# list_index = [0, 1, 2, 3, 4, 5, 6, 7]


index_data = pd.Index(list_index,
                      # dtype=np.float32,
                      name='rows'
                      )

# print(index_data)

columns_data = pd.Index(['col_1', 'col_2', 'col_3'],
                        name='cols'
                        )

df_data = pd.DataFrame({'col_1': [1, 2, 3, 4, 5, 6, 7, 8],
                        'col_2': [3, 4, 5, 6, 7, 8, 9, 10],
                        'col_3': [6, 7, 8, 9, 10, 11, 12, 13]},
                       index=index_data,
                       columns=columns_data)    # Но! проще создавать сразу внутри название индексов

df_5 = pd.DataFrame({f'c_{i}': np.arange(1000)*i for i in range(100)})
# print(df_5)

index_5 = df_5.index     #  получение индекса строк

columns_5 = df_5.columns    #   получение индексов столбцов

""""    Индексы можно преобразовать в список    """

index_5.to_list()
columns_5.to_list()


""""    Индексы можно преобразовать в массив Numpy    """

index_5.to_numpy()
columns_5.to_numpy()


"""     Уникальные значение и дубликаты в индексах      """

# print(f'Индексы строк = > {index_data}')
# print(f'Индексы столбцов = > {columns_data}')
index_data.unique() #   вернуь только уникальные значения

# print(f'Индексы строк УНИКАЛЬНЫЕ = > {index_data.unique()}')

# print(f'Количество значений: {len(index_data)}')
# print(f'Количество уникальных значений: {index_data.nunique()}')
#
# print(index_data.is_unique)  #   Уникальные ли значения

# print(index_data.duplicated())  #   False - если элемент встречается впервые и True - если уже встречался

# print(index_data.name)  #   имя
#   можно переименовать
index_data.name = 'rows_new'
columns_data.name = 'cols_new'


"""     Переименовать столбцы   """

df_data.rename(columns={'col_1': 'c_1',
                        'col_2': 'c_2',
                        'col_3': 'c_3', 'col_4': 'c_4'
                        }, inplace=True)

df_data.rename(str.upper,
               axis=0,  #   определяет ОСЬ ( 1 или 0)
               inplace=True)        # изменения применяются сразу к дата фрейму

# print(df_data)


"""     Если в индексах встречаются пропуски    """

index_6 = pd.Index([1, np.nan, 3, np.nan, 5])
# print(index_6)

"""     Проверить наличие пропусков в индексах  """

# print(index_6.hasnans)       #   True - есть пропуски

index_6.isna()  #  Возвращает список, где True - на этом месте пропуск (nan)
# print(index_6.isna())


"""     Удаление пропусков в индексах   """

index_6 = index_6.dropna()  #   метод не меняет исходные значения
# print(index_6.isna())
# print(index_6)

dict_in = {'col_1': [1, 2, 3, 4, 5],
           'col_2': [1, 2, 3, 4, 5],
           'col_3': [1, 2, 3, 4, 5]}

# df_7 = pd.DataFrame(dict_in)
# print(df_7)

df_7_index = pd.Index(['row_1', 'row_2', 'row_3', 'row_4', 'row_5'])
df_7 = pd.DataFrame(dict_in, index=df_7_index)


#
# nunique_ind = df_7.index.nunique()
#
# nunique_cols = df_7.columns.nunique()


df_7.rename(columns={'col_2': 'new_col_2',
           'col_3': 'new_col_3'}, inplace=True)


