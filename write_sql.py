import sqlite3 as sq

import pandas as pd

sql_request = '''SELECT * FROM sales'''

with sq.connect('test_df.db') as con:
    df_sql = pd.read_sql(sql_request, con)

"""     Аргумент if_exist=...   """

with sq.connect('test_df.db') as con:
    df_sql.to_sql('sales_0',
                  con,
                  # if_exists='fail',  #   Вернет ошибку при повторной записи данных в существующую таблицу
                  if_exists='replace', #    Перезапишет данные в таблице на новые
                  # if_exists='append',  #   Добавит значения в существующую таблицу
                  index=True,    #   Записывать ли индекс в таблицу
                  index_label='номер_индекс'    #   название строки с индексом
    )

with sq.connect('test_df.db') as con:
    df_sql_read = pd.read_sql("""SELECT * FROM sales_0""", con)

print(df_sql_read)
