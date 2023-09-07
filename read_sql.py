import sqlite3 as sq

import pandas as pd


def create_table(db='test_df.db', path='test_df_1.csv', name_table='sales'):
    con = sq.connect(db)

    df = pd.read_csv(path)
    df.to_sql(name_table, con, if_exists='replace', index=False)
    con.close()

create_table()

sql_request = '''SELECT * FROM sales'''

with sq.connect('test_df.db') as con:
    df_sql = pd.read_sql(sql_request, con)

# print(df_sql)

"""     Аргумент index_col=...  """

with sq.connect('test_df.db') as con:
    df_sql_index_col = pd.read_sql(sql_request,
                                   con,
                                   index_col='пользователь'     #   назначение строки индексом
                                   # , index_col = ['пользователь', 'продажи']  #   мультииндекс

    )

# print(df_sql_index_col)

"""     Аргумент parse_dates=...    """

with sq.connect('test_df.db') as con:
    df_sql_parse_dates = pd.read_sql(
        sql_request,
        con,
        parse_dates='дата')

print(df_sql_parse_dates)
