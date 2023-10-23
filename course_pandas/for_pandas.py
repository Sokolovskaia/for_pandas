import pandas as pd
import numpy as np

series_from_list = pd.Series(
    [5, 6, 9.8, 1, 7],
    index=['row_1', 'row_2', 'row_3', 'row_4', 'row_5'],
    dtype=str,
    name='pd_Series'
)

empty_series = pd.Series()

dict_array = {
    'row_1': 2,
    'row_2': 3,
    'row_3': 4,
    'row_4': 5,
    'row_5': 6
}

series_from_dict = pd.Series(dict_array)

np_array = np.array([5, 6, 6, 8, 7])
series_from_nparray = pd.Series(np_array,
                                copy=False)  # если False - не копирует данные, использует массив, вносит изменения

series_from_nparray.iloc[3] = 111
# print(series_from_nparray)
# print(np_array)

dict_array2 = {
    'col_1': [1, 2, 3, 4, 5],
    'col_2': [6, 7, 8, 9, 10],
    'col_3': [11, 12, 13, 14, 15],
    'col_4': [16, 17, 18, 19, 20],
    'col_5': [21, 22, 23, 24, 25]
}

df_from_dict = pd.DataFrame(dict_array2,
                            index=['row_1', 'row_2', 'row_3', 'row_4', 'row_5'],
                            columns=['col_1', 'col_4', '5'],
                            dtype=float)

df_array2 = ([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]])
df_from_array2 = pd.DataFrame(df_array2, copy=False)

df_from_array2.loc[:, 3:5] = 111


"""     Выравнивание индексов       """
series_1_sum = pd.Series([55, 55, 55, 55, 55],
                         index=['1', '3', '5', '7', '9'])

series_2_sum = pd.Series([77, 77, 77, 77, 77],
                         index=['2', '3', '4', '6', '8'])

df_from_2_series = pd.DataFrame({'column_1': series_1_sum,
                                 'column_2': series_2_sum})

series_4_sum = [1, 2, 3, 4, 5]
df_from_3_series = pd.DataFrame({'col_1': pd.Series(series_4_sum),
                                 'col_2': pd.Series([5, 6, 6, np.nan, 7],
                                                    index=['row_3', 'row_4', 'row_5', 'row_6', 'row_9'])}
                                )


# series = pd.Series([1, 2, 3, 4, 5], index=['row_1', 'row_2', 'row_3', 'row_4', 'row_5'], name='test_1')
dict_in1 = {'row_1': 1, 'row_2': 2, 'row_3': 3, 'row_4': 4}
series = pd.Series(dict_in1, index=['row_2', 'row_4'])


df_2 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=['row_1', 'row_2', 'row_3'])

dict_in = {'col_1': [1, 2, 3],
           'col_2': [4, 5, 6],
           'col_3': [7, 8, 9],
           'col_4': [10, 11, 12]}

#   На основе данного словаря создайте DataFrame состоящий только из col_2 и col_3,
#   индексы строк должны иметь следующие имена: row_1, row_2, row_3.

df = pd.DataFrame(dict_in,
                  index=['row_1', 'row_2', 'row_3'],
                  columns=['col_2', 'col_3']
                  )
