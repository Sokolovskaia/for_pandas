""" ТЕТРАДЬ++++++"""

"""     РАБОТА С ПРОПУСКАМИ В ДАННЫХ"""

import pandas as pd
import numpy as np

dict_array_g = {
    'age': [53, np.nan, 11, 18, 7],
    'name': ['Сергей', 'Маша', 'Ксюша', 'Аритарх', 'Соня'],
    'наличие авто': [1, 8, 6, 5, 9], # True, True, False, np,nan, False
    'марка авто': [np.nan, np.nan, np.nan, np.nan, np.nan]
    }

df_g = pd.DataFrame(dict_array_g)


""""    Метод    dropna()  Удаляет ВСЕ строки с пропусками """

for_print_df_1 = df_g.dropna()  #   метод не меняет сам DF

for_print_df_2 = df_g[['age', 'name', 'наличие авто']].dropna() # Удаляет те строки, где в выбранных столбцах есть пропуски в строке

"""     Аргумент axis   По умолчанию - 0 (удаляет строки с пропусками),  1 - удаляет СТОЛБЦЫ с пропусками"""
df_g.dropna(axis=0)
for_print_df_3 = df_g.dropna(axis=1)


"""     Аргумент how='all' ('any')  По умолчанию - any (хотя бы один пропуск),  all - все строка состоит из пропусков"""


for_print_df_4 = df_g.dropna(how='all')
for_print_df_5 = df_g.dropna(how='all', axis=1)
# print(for_print_df_5)


"""     Аргумент    subset=['имя_столбца', 'имя столбца']
указывает столбцы, где искать пропуски

Если удаляем строки - указываем название столбцов,
Если удаляем столбцы - указываем индекс строки

"""

for_print_df_6 = df_g.dropna(subset=['age', 'name'])
for_print_df_7 = df_g.dropna(subset=[1], axis=1)    # удалить столбцы, у к-ых есть пропуски в строке с индексом 1


"""     Аргумент   inplace=...."""

# df_g.dropna(subset=['age', 'name'], inplace=True)



"""             МЕТОД fillna()  """

""" Аргумент value=  (число или словарь)    """

for_print_df_8 = df_g.fillna(value=999) #   Заполняет пропуски указанным значением
for_print_df_9 = df_g.fillna(value={'age': 100, 'наличие авто': 'еще думает', 'марка авто': 'такая беленькая'})



"""         МЕТОД       isna() 
isna() ----   вернет True, если пропуск
"""

for_print_df_10 = df_g.isna()
for_print_df_11 = df_g['age'].isna()

for_print_df_12 = df_g[~ df_g['age'].isna()]    #   Получим только те строки, где в столбца age нет пропусков

"""         МЕТОД       notna() 
notna() ----   вернет Fale, если пропуск
"""


for_print_df_13 = df_g.notna()
for_print_df_14 = df_g[df_g['age'].notna()]

# print(df_g, end='\n'*2)
# print(for_print_df_14)


"""     ЗАДАЧИ      """

df = df_g
# new_df = df.dropna(how='all', axis=1)
# new_df = df.dropna(subset=['name', 'age'])
# new_df = df.dropna(subset=[2, 3, 4], axis=1)
# print(df, end='\n'*2)

# df.dropna(subset=['name', 'age'], inplace=True)

# df.fillna(value={'name': 'No_name', 'марка авто': 10}, inplace=True)

# new_df = df[df['name'].isna()]

new_df = df[df['age'].notna() & df['наличие авто'].le(5)]



dict_array_students = {
    'Упр_1': [np.nan, 1, 1, np.nan, 1],
    'Упр_2': [np.nan, 1, 1, np.nan, 1],
    'Упр_3': [1, np.nan, 1, np.nan, 1],
    'Упр_4': [1, 1, np.nan, np.nan, 1],
    'Упр_5': [1, np.nan, 1, np.nan, 1]
    }

df_test = pd.DataFrame(dict_array_students, index=['Имя_0', 'Имя_1', 'Имя_2', 'Имя_3', 'Имя_4'])

print(df_test, end='\n'*2)

# new_df_test = df_test.dropna() # список студентов со всеми решенными задачами (1)

#   студенты, у к-ых нет решенных задач

# new_df_test = df_test.replace(np.nan, 0)
# new_df_test = new_df_test.replace(1, np.nan)

# new_df_test = df_test.replace([np.nan, 1], [1, np.nan])
# new_df_test =df_test.replace([np.nan, 1], [1, np.nan]).dropna().index.to_list()
new_df_test = df_test[df_test.isna().all(axis=1)].index.to_list()

# print(df, end='\n'*2)
print(new_df_test)
