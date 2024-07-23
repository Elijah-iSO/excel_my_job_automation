import re

import pandas as pd

from constants import (COLUMN_TITLES_DZ, COLUMN_TITLES_TOP_10, END_PATTERN,
                       FILES, INN_PATTERN, INPUT_DIR, START_PATTERN)
from utils import get_osv_number, save_result


def get_top_10_counterparts(df, osv_number):

    if osv_number == '76':
        return None

    df.drop(df.columns[[1, 2, 5, 6]], axis=1, inplace=True)
    filtered_rows = []
    capture = False

    for index, row in df.iterrows():
        first_cell_value = str(row.iloc[0])  # Значение в первом столбце
        if re.match(END_PATTERN, first_cell_value):
            capture = False
        if capture and not re.match(INN_PATTERN, first_cell_value):  # если в ОСВ ИНН
            filtered_rows.append(row)
        if re.match(START_PATTERN, first_cell_value):
            capture = True

    cleared_df = pd.DataFrame(filtered_rows).fillna(0)

    if osv_number == '60':
        cleared_df.drop(cleared_df.columns[1], axis=1, inplace=True)
    else:
        cleared_df.drop(cleared_df.columns[2], axis=1, inplace=True)
    cleared_df.to_excel('result.xlsx', index=False)

    turnover_sum = cleared_df[cleared_df.columns[1]].sum()
    df_top_10 = cleared_df.sort_values(by=cleared_df.columns[1], ascending=False).head(10)
    df_top_10['any_name'] = df_top_10[cleared_df.columns[1]] / turnover_sum * 100
    df_top_10.columns = COLUMN_TITLES_TOP_10

    return df_top_10


def get_overdue_receivable(dataframe):
    return None


if __name__ == '__main__':
    for file in FILES:

        # 1 проверяем номер ОСВ в названии файла
        osv_number = get_osv_number(file)
        if not osv_number:
            continue

        # 2 получаем датафрейм
        dataframe = pd.read_excel(f'{INPUT_DIR}{file}', header=None)

        # 3 обрабатываем данные в зависимости от номера осв

        # 3.1 отдельная функция для осв 60 и 62 по крупным контрагентам
        top_10_counterparts = get_top_10_counterparts(dataframe, osv_number)
        # 3.2 отдельная для 60/62/76 по просроченной ДЗ
        overdue_receivable = get_overdue_receivable(dataframe)

        # 4 наводим красоту и сохраняем результат
        if type(top_10_counterparts) is pd.DataFrame:
            save_result(top_10_counterparts, file)
        if type(overdue_receivable) is pd.DataFrame:
            save_result(overdue_receivable, file)
