import pandas as pd
import numpy as np

""" Скользящие окна
Метод rolling()
"""

df_date = pd.DataFrame({'col_1': [0, 1, 2, 3, 4], 'col_2': [90, 91, 92, 93, 94]})

# print(df_date, end='\n'*2)

for_p_1 = df_date.rolling(3)
# Ширина строки - 3. Берется первая строка (0) и еще 2 строки выше нее (поэтому выводится только 1 строка),
# потом 2 строка и две строки выше (1, 0),поэтому выводится только три строки

# for window in df_date.rolling(3):
#     print(window, end='\n\n')

for_p_2 = df_date.rolling(3).sum()

"""     Аргумент min_periods=...    """
for_p_3 = df_date.rolling(3).mean()
for_p_4 = df_date.rolling(3, min_periods=1).mean()


"""     Аргумент step=...    Шаг, с которым будут браться окна"""
for_p_5 = df_date.rolling(3).mean()
for_p_6 = df_date.rolling(3, step=2).mean()


for_p_7 = df_date.rolling(2).agg({'col_1': 'sum', 'col_2': 'mean'})
for_p_8 = df_date.rolling(2).agg({'col_1': ['sum', 'mean', 'max', 'min'], 'col_2': 'mean'})

#   Пример
df = pd.DataFrame({'sales': np.random.randint(0, 50, 100)}, index=pd.date_range('2023', periods=100))

# print(df.head(10))

df_rolling = df.rolling(7, min_periods=1).agg([np.sum, np.mean, np.max, np.min])

df_rolling.reset_index(inplace=True)

df_rolling['weekday'] = df_rolling['index'].dt.dayofweek


df_rolling = df_rolling.loc[df_rolling['weekday'] == 6] # 6 - вс, 0 - пн

# print(df_rolling.head(10))
#   Проверка
# print(df['sales'][:'2023-04-09'].sum() == df_rolling.loc[df_rolling['weekday'] == 6][('sales', 'sum')].sum())


"""     Задачи      """
# Упржанение 1
df_1 = pd.DataFrame({'weekday': [0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 0, 1],
                     'sum': [22.0, 54.0, 75.0, 89.0, 101.0, 155.0, 170.0, 190.0, 211.0, 224.0, 232.0, 245.0, 253.0, 231.0, 273.0, 228.0]})
df_1.set_index('weekday', inplace=True)
#   Решение
new_df_1 = df_1.rolling(7, min_periods=1).mean()


# Упржанение 2
# В индексах строк "weekday" дни недели идут по порядку, 0 - Пн, 6 - Вс. Получите среднее значение в каждых выходных (Сб + Вс).
df_2 = pd.DataFrame({'weekday': [0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, 0, 1],
                     'sum': [7.0, 54.0, 89.0, 126.0, 172.0, 155.0, 170.0, 190.0, 176, 195.0, 201.0, 215.0, 195.0, 186.0, 177.0, 180.0]})
df_2.set_index('weekday', inplace=True)

#   Решение
print(df_2, end='\n'*2)

# df_rolling_2 = df_2.rolling(2, min_periods=1).sum()
# df_rolling_2 = df_rolling_2.loc[df_rolling_2.index == 6]


df_rolling_2 = df_2.rolling(2, min_periods=1).mean()
new_df_2 = df_rolling_2[df_rolling_2.index == 6]

print(new_df_2)
