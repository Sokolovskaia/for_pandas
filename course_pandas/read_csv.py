import pandas as pd

df_1 = pd.read_csv('/Users/sokolovskaamarina/Documents/Data analyst/sales2.csv',
                   sep=',',     # определить разделитель
                   index_col=['input'],     # назначить столбец индексом
                   usecols=['input', 'output', 'ulperrortol']       # фильтр, какие столбцы импортировать
                   )

df_squeeze = pd.read_csv('/Users/sokolovskaamarina/Documents/Data analyst/sales2.csv',
                         sep=',',
                         usecols=['input'],
                         # squeeze=True     # поменять на серию, если может
                         )



df_2 = pd.read_csv('/Users/sokolovskaamarina/Documents/Data analyst/sales2.csv',
                   sep=',',
                   usecols=['input', 'output', 'ulperrortol'],
                   dtype={'ulperrortol': 'float'}       # определить тип данных для стобца или нескольких
                   )

# df_2.info()      # функция показывает информацию по дата-фрейму

df_nrow = pd.read_csv('/Users/sokolovskaamarina/Documents/Data analyst/sales2.csv',
                   sep=',',
                   nrows=3      # кол-во импортируемых строк
                      )

df_parse_dates = pd.read_csv('/Users/sokolovskaamarina/Documents/Data analyst/sales2.csv'
                             , sep=','
                             # , parse_dates=[['year', 'month', 'day'], 'ac_date', 'output']      # три стобца схлопнули в дату
                             , parse_dates={'date_0': ['ac_date'],
                                            'new_name': ['year', 'month', 'day']}       # задали имя для столбца с датой
                             )

"""     infer_datetime_gormat=...    (ускоряет отработку)   """
df_parse_dates2 = pd.read_csv('/Users/sokolovskaamarina/Documents/Data analyst/sales2.csv'
                             , sep=','
                             , parse_dates=['ac_date']
                             # , infer_datetime_format=True
                             )

"""     keep_date_col=...  """

df_parse_dates3 = pd.read_csv('/Users/sokolovskaamarina/Documents/Data analyst/sales2.csv'
                             , sep=','
                             , parse_dates=[['year', 'month', 'day'], 'ac_date']
                             , keep_date_col=True       # не удаляются столбы, из которых собирается столбец с датой
                            )

"""         encoding=...       """""
df_encoding = pd.read_csv('/Users/sokolovskaamarina/Documents/Data analyst/sales2.csv'
                          , sep=','
                          , encoding='utf8')



