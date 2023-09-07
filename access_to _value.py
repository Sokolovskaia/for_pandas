"""     Методы at и iat. Методы loc и iloc
at и iat для одного элемента
loc и iloc для нескольких

"""

import pandas as pd
import numpy as np

dict_array_a = {
    'age': ['Сергей', 'Маша', 'Ксюша', 'Аристарх', 'Соня'],
    'name': [53, 37, 11, 18, 7],
    'наличие авто': [True, True, False, True, False]
                }

df_a = pd.DataFrame(dict_array_a, index=[f'row_{i}' for i in range(len(dict_array_a['age']))])


"""     Доступ к одному элементу
через индексы строк и столбцов
df.iat['индекс строки', 'индекс столбца']
"""

for_print_1 = df_a.iat[2, 1]
for_print_2 = df_a['age'].iat[3]    # применение к серии
df_a.iat[4, 0] = 'Новое имя'    # меняем значение в df   строка с индексом 5 и столбец - 0

"""     Доступ к одному элементу через метки('имена') строк/столбцов 
df.at['метка строки', 'метка стобца']
"""

for_print_3 = df_a.at['row_3', 'age']
for_print_4 = df_a['age'].at['row_2'] # применение к серии
df_a.at['row_4', 'age'] = 'Соня'

"""     Доступ к ГРУППЕ строк/столбцов"""

"""     Доступ к группе строк/столбцов через индексы

df.iloc[индекс строки, индекс столбца]

df.iloc[[список индексов строк], [список индексов столбцов]]

df.iloc[срезы:индексов, срезы: столбцов]

df.iloc[[список, булевых, значений],[список, булевых, значений]]

"""

for_print_5 = df_a.iloc[1, 1]

for_print_6 = df_a['наличие авто'].to_list()
# нельзя передавать серию, поэтому в начале создаем список и потом передаем уже его
for_print_7 = df_a.iloc[df_a['наличие авто'].to_list(), [True, False, True]]

for_print_8 = df_a.iloc[1:3, 0] # так вернет серию
for_print_9 = df_a.iloc[1:3, [0]] # так вернет DF

df_a.iloc[1:3, 1] = 99     # меняет значение в df


"""     Доступ к группе строк/столбцов через метки  
df.loc['метки строк', 'метки столбцов']
"""

for_print_10 = df_a.loc['row_1', 'age']     # можно указывать ТОЛЬКО метки строк и столбцов
for_print_11 = df_a.loc[['row_1', 'row_2']]
for_print_12 = df_a.loc[:, ['age', 'name']]
for_print_13 = df_a.loc['row_0':'row_3', 'name']
for_print_14 = df_a.loc['row_0':'row_3', 'age':'name']
for_print_15 = df_a.loc['row_0':'row_3', ['name']]

"""     Доступ к группе строк/столбцов по логическому условию   """

for_print_16 = df_a.loc[df_a['name'] == 99]

df_a.loc['row_0':'row_2', 'name'] = 1
df_a.loc['row_0':'row_2', 'name'] = [10, 20, 30]

# print(df_a, end='\n'*2)

df_a.loc['row_0':'row_2', 'age'] = pd.Series(['йегреС', 'ашаМ', 'ашюсК'], index=['row_0', 'row_1', 'row_2'])
# print(df_a, end='\n'*2)

df_a.loc['row_0':'row_2', ['age', 'name']] = pd.DataFrame({
    'age': ['Сергей', 'Маша', 'Ксюша'],
    'name': [22, 33, 44]},
    index=['row_0', 'row_1', 'row_2'])

# print(df_a, end='\n'*2)

"""     Замена данных в двух столбцах местами   """
# df_a.loc[:, ['age', 'name']] = df_a[['name', 'age']] #  так НЕЛЬЗЯ делать, не сработает

df_a.loc[:, ['age', 'name']] = df_a[['name', 'age']].to_numpy()

# print(df_a, end='\n'*2)
# print(for_print_16, end='\n'*2)


"""     ЗАДАЧИ  """
df = pd.DataFrame(dict_array_a, index=[f'row_{i}' for i in range(len(dict_array_a['age']))])

# value = df.iat[2, 1]
# value = df['name'].iloc[1]
# value = df.at['row_3', 'age']
# print(df, end='\n'*2)

# df.at['row_2', 'name'] = 'new_name'
# new_ser = df.iloc[[2, 4], 1]
# new_ser = df.iloc[1:4, 1]
# new_ser = df['name'].iloc[[1, 2, 4]].to_list()
# new_ser = df.loc[['row_1', 'row_3'], 'name']
# new_ser = df[df['name'].isin([53, 37, 1])]

df_1 = pd.DataFrame({
    'год рождения': [np.nan, 89, 90, 91, 92],
    'стаж работы': [3.25, 4.5, 5.75, 6.25, 7.5],
    'зарплата': [20, np.nan, 20, 40, 40]},
    index=[i for i in range(3, 8)])

# new_df = df_1.loc[df_1['год рождения'].gt(89), ['стаж работы', 'зарплата']]
# new_ser = df_1.loc[[3, 5], 'год рождения']

# new_ser = df_1[~ df_1['зарплата'].isna()]['зарплата']
# new_ser = df_1.loc[~df_1['зарплата'].isna(), 'зарплата']

print(df_1)
df_1.loc[:, 'зарплата'].fillna(value=df_1['зарплата'].mean(), inplace=True)





# print(df_1['зарплата'].dtypes)

# df_1 = df_1.astype({'зарплата': np.int64})
# print(df_1['зарплата'].dtypes)


# print(df_1, end='\n'*2)
print(df_1, end='\n'*2)
