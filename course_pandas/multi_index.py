import pandas as pd
import numpy as np

array_m = [[1, 1, 2, 2], ['row_1', 'row_2', 'row_3', 'row_4']]
multii_array_m = pd.MultiIndex.from_arrays(
    array_m, #  array содержит индексы
    names=['level_0', 'level_1'])   # names - имена уровней

multii_array_m_test = pd.MultiIndex.from_arrays(
    array_m, #  array содержит индексы
    names=['str_0', 'str_1'])   # names - имена уровней

df_index_m = pd.DataFrame([
    [4,  3, 2, 1],
    [4,  3, 2, 1],
    [4,  3, 2, 1],
    [4,  3, 2, 1]],
    index=multii_array_m)

df_columns_m = pd.DataFrame([
    [4,  3, 2, 1],
    [4,  3, 2, 1],
    [4,  3, 2, 1],
    [4,  3, 2, 1]],
    columns=multii_array_m)

df_combo = pd.DataFrame([
    [4,  3, 2, 1],
    [4,  3, 2, 1],
    [4,  3, 2, 1],
    [4,  3, 2, 1]],
    index=multii_array_m_test, columns=multii_array_m)

# print(df_combo)


# print(df_index_m, end='\n\n')
# print(df_columns_m)

"""     Создание мультииндекса с помощью метода from_product    """
level_0 = ['row_1', 'row_2']
level_1 = [1, 2, 3]

multi_product_m = pd.MultiIndex.from_product(
    [level_0, level_1],
    names=['level_0', 'level_1']
)

df_product_m = pd.DataFrame(
    {'col_1': [6, 5, 4, 3, 2, 1],
     'col_2': [6, 5, 4, 3, 2, 1],
     'col_3': [6, 5, 4, 3, 2, 1],
     'col_4': [6, 5, 4, 3, 2, 1]},
    index=multi_product_m)

# print(df_product_m)


"""     Создание мультииндекса из списка кортежей   """

tuples_m = [(1, 'row_1'), (1, 'row_2'), (1, 'row_3'), (2, 'row_1'), (2, 'row_2'), (2, 'row_3')]

multi_tuples = pd.MultiIndex.from_tuples(tuples_m, names=['level_0', 'level_1'])

df_tuples_m = pd.DataFrame(
    {'col_1': [6, 5, 4, 3, 2, 1],
     'col_2': [6, 5, 4, 3, 2, 1],
     'col_3': [6, 5, 4, 3, 2, 1],
     'col_4': [6, 5, 4, 3, 2, 1]},
    index=multi_tuples)

# print(df_tuples_m)

"""     Получение мультииндекса """
# print(df_tuples_m.index)
# print(df_tuples_m.columns)

"""     Число уровней   """
# print(df_tuples_m.index.nlevels)

""" Кортеж с длиной каждого уровня  """
# print(df_tuples_m.index.levshape)   # на 0 уровне 2 элемента, а на 1 уровне - 3 элемента

"""     Имена уровней   """
# print(df_tuples_m.index.names)

"""     Изменение имен уровней  """

df_tuples_m.index.names = ['new_level_0', 'new_level_1']
# print(df_tuples_m.index.names)

df_tuples_m.index.set_names(['level_0', 'level_1'], inplace=True)
# print('Поменяли имя обратно',df_tuples_m.index.names)

df_tuples_m.index.set_names('new_level_0', level=1, inplace=True)      #    поменять название конкретного уровня
# print(df_tuples_m.index.names)


"""        Элементы, содержащиеся в мультииндексе   """

# print(df_tuples_m.index.levels)
df_tuples_m.index = multi_product_m
# print(df_tuples_m.index)

"""     Заменить элементы на конкретном уровне  """
# new_index_m = df_tuples_m.index.set_levels([[4, 5, 6], ['q', 'w', 'r', 't', 'p']])

new_index_m = df_tuples_m.index.set_levels(['q', 'w', 'r', 't'], level=0)
# print(new_index_m)


"""     Сброс уровней мультииндекса """
# print('старый', df_tuples_m)
new_df_tuples_m = df_tuples_m.reset_index()

df_tuples_m.reset_index(['level_0'], inplace=True)

df_tuples_m.index = multi_product_m


# new_index_m_1 = df_tuples_m.index.droplevel() #   возвращает индекс с удаленным нулевым уровнем


# new_index_m_1 = df_tuples_m.index.droplevel(level=1)  #   возвращает индекс с удаленным указанным уровнем

new_index_m_1 = df_tuples_m.index.droplevel(['level_1'])#   возвращает индекс с удаленными уровнями
# print(df_tuples_m.index)
# print(new_index_m_1)


"""     ЗАДАЧИ  """
""" 
Есть две модели мотоциклов "юпитер" и "восход". 
Они могут быть раскрашены в три цвета: черный, оранжевый и красный. 
На основе этих данных создайте мультииндекс. 
Нулевой уровень с именем "модель", а первый уровень с именем "цвет".


"""
ind_m = pd.MultiIndex.from_product([['юпитер', 'восход'], ['черный', 'оранжевый', 'красный']], names=['модель', 'цвет'])

"""
В программе создан DataFrame и записан в переменную df. 
Выполните следующие действия с мультииндексом строк:

получите количество уровней, результат запишите в переменную nlev,
получите кортеж с количеством элементов на каждом уровне, результат запишите в переменную lev_sh,
получите имена уровней, результат запишите в переменную name_lev,
получите объект, содержащий элементы мультииндекса, результат запишите в переменную lev,

"""

nlev = df_tuples_m.index.nlevels
lev_sh = df_tuples_m.index.levshape
name_lev = df_tuples_m.index.names
lev = df_tuples_m.index.levels

# print(f'nlev={nlev}', f'\nlev_sh={lev_sh}\n', f'\nname_lev={name_lev}', f'\nlev={lev}')




# print(df_tuples_m)

df_columns_m.columns = df_columns_m.columns.droplevel(level=0)
df_columns_m.rename(columns={'row_1': 'n_1', 'row_2': 'n_2', 'row_3': 'n_3', 'row_4': 'n_4'}, inplace=True)

print(df_columns_m)

""""
df.columns = df.columns.droplevel(level=0)
df.rename(columns={'max': 'age_max', 'min': 'age_min', 'mean': 'age_mean', 'last_name': 'last_name', 'first_name': 'first_name'}, inplace=True)



"""