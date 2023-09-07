import pandas as pd

df = pd.DataFrame([
    ['user_1', 'female', '2022-12-12', 12],
    ['user_2', 'male', '2021-07-07', 100],
    ['user_3', 'male', '2023-01-01', 0],
    ['user_4', 'female', '2000-11-09', 12000],
    ['user_5', 'male', '2009-03-08', 99000]],
                  # index=['row_1', 'row_2', 'row_3'],
                  columns=['user_id', 'sex', 'date', 'sale']
                  )
df.to_csv('test_df_1.csv',
          sep=',',
          columns=['user_id', 'sale', 'date'],       # какие столбцы из dataframe записать в csv
          #header=True,       #   сохранять заголовкиб иначе бере первую строку в качестве заголовков
          header=['пользователь', 'продажи', 'дата'],        #   присвоить имена столбцам
          index=True,       # записывать ли в файл индексы строк
          index_label='индекс строки',       #   назвать столбец с индексом
          encoding='utf8'
          )
df_1 = pd.read_csv('test_df_1.csv', sep=',')
print(df_1)


