import re

import pandas as pd

from constants import (K, KK, COLUMN_TITLES_DZ, COLUMN_TITLES_TOP_10, END_PATTERN,
                       FILES, INN_PATTERN, INPUT_DIR, PERCENT, START_PATTERN)
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

    column_to_drop = 1 if osv_number == '60' else 2
    cleared_df.drop(cleared_df.columns[column_to_drop], axis=1, inplace=True)

    turnover_total = cleared_df[cleared_df.columns[1]].sum() / K
    cleared_df[cleared_df.columns[1]] = cleared_df.iloc[:, 1] / K
    df_top_10 = cleared_df.sort_values(by=cleared_df.columns[1], ascending=False).head(10)
    df_top_10[COLUMN_TITLES_TOP_10[2]] = df_top_10.iloc[:, 1] / turnover_total * PERCENT

    df_top_10.columns = COLUMN_TITLES_TOP_10

    return df_top_10


def get_overdue_receivable(df):

    data = df.fillna(0)
    filtered_data = data.query('1')

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
        if top_10_counterparts is not None:
            save_result(top_10_counterparts, osv_number)
        if overdue_receivable is not None:
            save_result(overdue_receivable)
