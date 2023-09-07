import pandas as pd


my_series = pd.Series([5, 6, 7, 8, 9, 10])
#print(my_series)

my_series2 = pd.Series([5, 6, 7, 8], index=['a', 'b', 'c', 'd'])
#print(my_series2)

my_series2[['a', 'b']] = 0  # обращение к элементу, присваивание значения
#print(my_series2)
#print(my_series2[['a', 'c']])

pd.read_excel('pd_test.xls')

""" Создание таблиц с заголовком """
my_series3 = pd.DataFrame({'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'], 'population': [17.04, 143.5, 9.5, 45.5], 'square': [2724902, 17125191, 207600, 603628]})

#print(my_series3['country'])

"""  Вычисление и запись нового столбца"""
my_series3['density'] = my_series3['population'] / my_series3['square'] * 1000000
# print(my_series3)

"""  Выборка по условию """
# print(my_series3[my_series3['country'] == 'Russia'])

""" Kоличество значений по каждому столбцу  """
# print(my_series3.count())

# print(my_series3['population'].max())  #  медиана
# print(my_series3['population'].mean())  #  среднее
# print(my_series3['population'].median())  #  медиана


"""   Агрегация отфильтрованных данных"""

count_country = my_series3[my_series3['country'] == 'Russia']['population'].count()
#  print(count_country)



