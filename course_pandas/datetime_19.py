import pandas as pd
import numpy as np

"""     Типы данных datetime    """
df_date = pd.read_csv('df_date.csv')

print(df_date)
"""     Изменение типа данных при импорте   """
pd.read_csv('df_date.csv', parse_dates=['date']).info()


# df_date.astype({'date': 'datetime[ns]'})    # ключ - название столбца, значение - тип данных

"""     Изменение типа данных после импорта   (применяется к строке или Серии"""
pd.to_datetime('2017-02-19')

pd.to_datetime(df_date['date'])
#
print(pd.to_datetime('2017-02-19'))
print(pd.to_datetime('17-02-19'))   # Будут разные результаты


"""
%a - Sun, Mon, ...(en_US)
%A - Sunday, Monday, ...(en_US)
%w - 0, 1, ..., 6
%d - 01, 02, ... 31
%b - Jan, Feb, ..., Dec(en_US)
%B - January, February, ..., December (en_US)
%m - 01, 02, ..., 12
%y - 00, 01, ..., 99
%Y - 0001, 0002, ..., 2013, 2014, ..., 9998, 9999

"""

# Важно при парсинге верно указывать формат

# pd.to_datetime('2017-02-19', format='%Y-%m-%d')
# pd.to_datetime('17-02-19', format='%y-%m-%d')
# pd.to_datetime('February/19/17 Monday', format='%B/%d/%y %A')

print(pd.to_datetime('February/19/17 Monday', format='%B/%d/%y %A'))
"""     Столбец с датой 
Доступ через dt - аксессор
"""
# df_date['day_name'] = df_date['date'].dt.day_name() #  добавить столбец с Именем дня недели
# df_date['day'] = df_date['date'].dt.day     #   день месяца цифрами
# df_date['month'] = df_date['date'].dt.month     #   месяц цифрами
# df_date['weekday'] = df_date['date'].dt.weekday()     #   день недели цифрами, 0 - пн, 6 -вс

"""     Применительно к дате доступ уже без dt"""
# df_date.loc[2, 'date'].day_name()
# df_date.loc[2, 'date'].day
# df_date.loc[2, 'date'].month
# df_date.loc[2, 'date'].weekday()


"""     Диапазон дат    """
pd.date_range('2023-03-10', periods=10) #  дата или строка в виде даты,  periods - количество эл-ов к-ые нужно получить
# вернет 10 дат начиная с указанной даты с частотой 1

pd.date_range('2023-03-10', periods=10, freq='M')   #    верет 10 дат - каждая дата это дата конца месяца, в том числе и первая дата (будет изменена)

"""     Периодичность:
'D'(по умолч) - календарных дней,
'W' - еженедельная,
'M' - окончания месяца,
'Y' - окончания года                    
    """
pd.date_range('2023-03-10', '2023-05-30', freq='M')
# Начало и конец, 30 Мая - не последний день месяца, поэтому последняя запись будет - конец апреля, май не войдет.
# Он вошел бы, если бы было указано 31 мая

pd.date_range('2023-03-10', '2023-05-01', periods=10)   # разница между периодами одинаковая, разобьет на 10

df_date['new_date'] = pd.date_range('2023-03-10', '2023-05-01', periods=df_date.shape[0])
# df_date['еще один new_date'] = pd.date_range('2023-03-10', '2023-05-01', periods=df_date.shape[0]).day_
# df_date['еще один new_date'] = pd.date_range('2023-03-10', '2023-05-01', periods=df_date.shape[0]).date




for_p_1 = df_date.loc[df_date['date'] == '2016-08-03']
for_p_2 = df_date.loc[df_date['date'] == pd.to_datetime('03-08-2016', format='%d-%m-%Y')] # Лучше так, с конкретным указанием формата даты



"""     Задачи  """

#   Упражнение 1
# Строку "1961-04-12" представьте в виде объекта Timestemp.
# Результат запишите в переменную date.

date_1 = pd.to_datetime('1961-04-12', format='%Y-%m-%d')


#   Упражнение 2
# В программе создана серия со строковыми значениями и записана в переменную ser.
# Представьте эту серию в виде серии с типом данных "datetime".
# Результат запишите в переменную new_ser.

ser_2 = pd.Series(['2018-04-27', '2018-10-10', '2018-08-13', '2017-05-13'])
new_ser_2 = pd.to_datetime(ser_2, format='%Y-%m-%d')


#   Упражнение 3
# В программе создан DataFrame и записан в переменную df.
# Поменяйте тип данных в столбце "date" на "datetime".
df_3 = pd.DataFrame({'id': [10000, 10001, 10002, 10003], 'date': ['2018-04-27', '2018-10-10', '2018-08-13', '2017-05-13']})
# Вариант_1
df_3['date'] = pd.to_datetime(df_3['date'])
# Вариант_2
df_3 = df_3.astype({'date':'datetime64[ns]'})

#   Упражнение 4
# Поменяйте тип данных в столбце "date" на "datetime" и установите его в качестве индексов строк.
df_4 = pd.DataFrame({'id': [10000, 10001, 10002, 10003], 'date': ['2018-04-27', '2018-10-10', '2018-08-13', '2017-05-13']})
df_4 = df_4.astype({'date': 'datetime64[ns]'})
df_4 = df_4.set_index('date')


#   Упражнение 7
# Поменяйте тип данных в столбце "date" на "datetime",
# а также добавьте столбец с годом "year" и столбец с днем недели в виде числа "weekday".
df_7 = pd.DataFrame({'id': [10000, 10001, 10002, 10003], 'date': ['2018-04-27', '2018-10-10', '2018-08-13', '2017-05-13']})
df_7 = df_7.astype({'date': 'datetime64[ns]'})
df_7['year'] = df_7['date'].dt.year
df_7['weekday'] = df_7['date'].dt.weekday


#   Упражнение 8
# Поменяйте тип данных в столбце "date" на "datetime".
# Получите только те строки, которые в столбце "date" содержат конец месяца.
# Результат запишите в переменную new_df.
# Подсказка: воспользуйтесь свойством is_month_end.

df_8 = pd.DataFrame({'id': [10000, 10001, 10002, 10003, 10004], 'date': ['2018-04-27', '2018-10-31', '2018-08-13', '2017-05-13', '2012-12-31']})
df_8['date'] = pd.to_datetime(df_8['date'])
new_df_8 = df_8[df_8['date'].dt.is_month_end]



#   Упражнение 9
# В программе создан DataFrame, содержащий данные о доходах, и записан в переменную df.
# Получите данные о доходах в каждом месяце.
# Результат запишите в переменную new_df.
# Подсказка: добавьте дополнительный столбец, по которому можно будет сгруппировать данные.
df_9 = pd.DataFrame({'date': ['2018-10-27', '2018-10-31', '2018-12-13', '2017-05-13', '2012-12-31'], 'salary': [160, 140, 110, 120, 130]})
df_9['date'] = pd.to_datetime(df_9['date'])
df_9['month'] = df_9['date'].dt.month

new_df_9 = df_9.groupby('month', as_index=False).agg({'salary': np.sum})


#   Упражнение 10
# Создайте объект DatetimeIndex, который содержит 20 элементов,
# начинающихся с "2023-05-05" и частотой в один день.
# Результат запишите в переменную date_range.

date_range = pd.date_range('2023-05-05', periods=20)

#   Упражнение 11
# Расчет продуктовой метрики DAU. DAU - количество уникальных пользователей в день.
# В программе созданы файлы с данными - "user_visit.csv".
# Файл "user_visit.csv" содержит столбцы:
# 'user' - имена пользователей приложения,
# 'date' - дата когда пользователи заходили в приложение.
# Рассчитайте метрику DAU. Результат запишите в переменную dau.

dau = pd.read_csv('user_visit.csv').groupby(['date'], as_index=False)['user'].nunique().rename(columns={'user': 'DAU'})



# Упражнение 12.
# Расчет продуктовой метрики WAU. WAU - количество уникальных пользователей в неделю.
# В программе созданы файлы с данными - "user_visit.csv".
# Файл "user_visit.csv" содержит столбцы:
# 'user' - имена пользователей приложения,
# 'date' - дата когда пользователи заходили в приложение.
# Рассчитайте метрику WAU.
# Результат запишите в переменную wau.
# Элементы индекса строк - это порядковый номер недели в году.
# Начинаются с 52,
# тк первое января 2023 года это конец недели начавшейся в 2022 году.
# Метод groupby() по умолчанию сортирует данные по группируемому столбцу\столбцам,
# тк аргумент sort по умолчанию имеет значение True.
# Иногда нужно сохранить исходный порядок в группируемом столбце\столбцах, для этого в аргумент sort нужно передать False.

df_12 = pd.read_csv('user_visit.csv')
df_12['date'] = pd.to_datetime(df_12['date'])
df_12['week_num'] = df_12['date'].dt.isocalendar().week

wau = df_12.groupby('week_num', sort=False).agg(WAU=('user', 'nunique'))

# Упражнение 13
"""     НЕ РЕШЕНО (НАЧАЛО)"""
# Получите DataFrame в котором есть столбцы 'user', 'date',
# а также столбец 'flag_reg'.
# В столбце 'flag_reg' стоит True, если user в этот день зарегистрировался и False, если нет.

df_user_visit = pd.read_csv('user_visit.csv')
df_date_reg = pd.read_csv('date_reg.csv')

new_df_13 = df_user_visit.merge(df_date_reg, how='left', on='user')
new_df_13['date_reg'] = new_df_13['date'].isin(new_df_13['date_reg'])
new_df_13.rename(columns={'date_reg': 'flag_reg'}, inplace=True)
new_df_13['dupl'] = new_df_13.duplicated()

new_df_13['flag_reg'] = new_df_13.apply(lambda x: x['flag_reg'] if x['dupl']==False else False, axis=1)
new_df_13.drop('dupl', axis=1, inplace=True)




"""     НЕ РЕШЕНО (КОНЕЦ)"""

# Упражнение 14
# Получите DataFrame в котором есть столбцы 'user', 'date', а также столбец 'flag_reg'.
# В столбце 'flag_reg' стоит True, если user в этот день зарегистрировался и False, если нет.
# Пользователь может заходить в приложение без регистрации.

# df_user_visit = pd.read_csv('user_visit.csv')
# df_date_reg = pd.read_csv('date_reg.csv')
#
# df_group = df_user_visit.merge(df_date_reg, how='left', on='user')
# df_group['flag_reg'] = df_group.apply(lambda x: True if x['date']==x['date_reg'] else False, axis=1)
#
# new_df_14 = df_group[['user', 'date', 'flag_reg']].copy()




print('----------------------------------------------------------')
print('Упражнение 14')
print(df_user_visit, end='\n\n')
print(df_date_reg, end='\n\n')
# print(df_group, end='\n\n')
print(new_df_13, end='\n\n')

