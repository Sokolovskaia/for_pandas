""" ТЕТРАДЬ++++++"""

"""         УДАЛЕНИЕ СТРОК И СТОЛБЦОВ И МЕТОД ASTYPE()  """
import pandas as pd
import numpy as np

df_d = pd.DataFrame(
    {
        'col_1': [5, 6, np.nan, 3, 7],
        'col_2': [27, 6, 7, 40, 70],
        'col_3': [1, 45, 6, 62, 7]
         },
        index=['row_1', 'row_2', 'row_3', 'row_4', 'row_5'])


"""     Удаление строк и столбцов. Метод Drop()     

Метод Drop() имеет след. аргументы:
- labels  ---> передаем имена строк или столбцов, к-ые нужно удалить. Принимает один элемент или список
- axis
- index   ---> Принимает один элемент или список (какие строки удалить)
- columns ---> Принимает один элемент или список (какие столбцы удалить)
- inplace

"""

"""     аргументы labels и axis     """

for_print_1 = df_d.drop('row_2')
for_print_2 = df_d.drop(['row_1', 'row_3'])
for_print_3 = df_d.drop(['col_1', 'col_2'], axis=1)


"""     аргументы index и columns   """

for_print_4 = df_d.drop(index='row_1')
for_print_5 = df_d.drop(index=['row_1', 'row_2'])

for_print_6 = df_d.drop(columns='col_1')
for_print_7 = df_d.drop(columns=['col_1', 'col_2'])
for_print_8 = df_d.drop(index=['row_1', 'row_2'], columns=['col_1', 'col_2'])

"""     аргумент   inplace=     """

# df_d.drop(index='row_1', columns='col_1', inplace=True)


"""     МЕТОД  astype() """


category_list = ['a', 'b', 'c', 'd', 'e']
df_d_1 = pd.DataFrame(
    {
        'col_1': [i for i in range(1000)],
        'col_2': [float(i) for i in range(1000)],
        'col_3': [category_list[i%5] for i in range(1000)],
        'col_4': [*pd.date_range(start='01-01-2000', periods=1000).strftime("%m-%d-%y")]
    },
    index=[f'row_{i}' for i in range(1000)])


# print(df_d_1, end='\n'*2)
# print(df_d_1.dtypes, end='\n'*2)
# print(df_d_1.memory_usage(), 'ПАМЯТЬ', end='\n'*2) # какой объем память выделен под каждый столбце (выделяется по 8 байт)

for_print_9 = df_d_1.astype({'col_1': np.int8})     # произошла потеря значений ;(
for_print_10 = df_d_1.astype({'col_3': 'category'})
# for_print_11 = df_d_1.astype({'col_4': 'datetime64[ns]'})
#
# print(for_print_9.memory_usage(), 'ПАМЯТЬ  NEW') # уменьшили объем выделяемой память
# print(for_print_10.memory_usage(), 'ПАМЯТЬ  NEW') # уменьшили объем выделяемой память


for_print_12 = df_d_1.astype(
    {
        'col_1': np.int16,
        'col_2': np.float16,
        'col_3': 'category',
        # 'col_4': 'datetime64[ns]'     # Почему-то ошибка :(((((
    })

for_print_12.reset_index(drop=True, inplace=True)


# print(for_print_12)
# print(for_print_12.dtypes)
print(for_print_12.memory_usage(), 'ПАМЯТЬ NEW')

"""%%time
for i in range(1000):
    df_d_1['col_3'].str.upper()"""



"""         ЗАДАЧИ      """

df = pd.DataFrame(
    {
        'col_1': [5, 6, np.nan, 3, 7],
        'col_2': [27, 6, 7, 40, 70],
        'col_3': [1, 45, 6, 62, 7]
         })
        # index=['row_1', 'row_2', 'row_3', 'row_4', 'row_5'])

# new_df = df.drop(index=[], columns=['id', 'product'])

new_df = df.astype({'col_2': 'int'})


# print(df, end='\n'*2)
print(new_df.dtypes)