import re

import openpyxl
import pandas as pd

from constants import (AV_VA_PATTERN, K, KK, COLUMN_TITLES_DZ,
                       COLUMN_TITLES_TOP_10, END_PATTERN, FILES, FILE_HANDLERS,
                       INPUT_DIR, OSV_DZ_PATTERN, PERCENT, START_PATTERN)
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
        if capture:
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
    end_index = len(df)

    for index, row in data.iterrows():
        first_cell_value = str(row.iloc[0])  # Значение в первом столбце
        if re.match(OSV_DZ_PATTERN, first_cell_value):
            start_index = index
        if re.match(AV_VA_PATTERN, first_cell_value):
            end_index = index
            break

    data = data.iloc[start_index:end_index]
    mask = (data.iloc[:, 1].astype(int) != 0) & (data.iloc[:, 4].astype(int) == 0) & (data.iloc[:, 5].astype(int) > KK)
    filtered_df = data.loc[mask]
    filtered_df = filtered_df.drop(filtered_df.columns[[1, 2, 3, 4, 6]], axis=1)
    filtered_df.columns = COLUMN_TITLES_DZ

    return filtered_df


if __name__ == '__main__':
    result_book = openpyxl.Workbook()
    result_book.remove(result_book['Sheet'])

    for file in FILES:
        for handler, file_suffixes in FILE_HANDLERS.items():
            if any(file_suffix in file for file_suffix in file_suffixes):
                sheet_name = f'{file}_{handler}'
                result_book.create_sheet(title=sheet_name)

                handler(file)
                break

        # 1 проверяем номер ОСВ в названии файла
        osv_number = get_osv_number(file)
        if not osv_number:
            continue

        # 2 получаем датафрейм
        dataframe = pd.read_excel(f'{INPUT_DIR}{file}', header=None)

        # 3 обрабатываем данные в зависимости от номера осв

        # 3.1 отдельная функция для осв 60 и 62 по крупным контрагентам
        top_10_counterparts = get_top_10_counterparts(dataframe.copy(), osv_number)
        # 3.2 отдельная для 60/62/76 по просроченной ДЗ
        overdue_receivable = get_overdue_receivable(dataframe.copy())

        # 4 наводим красоту и сохраняем результат
        if top_10_counterparts is not None:
            save_result(top_10_counterparts, osv_number, name='TOP10')
        if overdue_receivable is not None:
            save_result(overdue_receivable, osv_number, name='overdue_receivable')
