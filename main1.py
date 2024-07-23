import re

import pandas as pd

from constants import (COLUMN_TITLES_DZ, COLUMN_TITLES_TOP_10, END_PATTERN,
                       FILES, INN_PATTERN, INPUT_DIR, OUTPUT_DIR, START_PATTERN)


def get_osv_number(file):
    if '60' in file:
        return '60'
    elif '62' in file:
        return '62'
    elif '76' in file:
        return '76'
    else:
        return None


def get_dataframe(file, osv_number):
    return pd.read_excel(f'{INPUT_DIR}{file}', header=None)


def get_top_10_counterparts(dataframe, osv_number):
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

    return pd.DataFrame(filtered_rows).fillna(0)

    df.drop(
        [COLUMN_TITLES[1], COLUMN_TITLES[2], COLUMN_TITLES[5], COLUMN_TITLES[6]],
        axis=1,
        inplace=True
    )

    if osv_number == '60':
        df.drop(
            [COLUMN_TITLES[3]],
            axis=1,
            inplace=True
        )
        turnover_sum = df[COLUMN_TITLES[4]].sum()
        df_top_10 = df.sort_values(by=COLUMN_TITLES[4], ascending=False).head(10)
        df_top_10['Доля'] = df_top_10[COLUMN_TITLES[4]] / turnover_sum
        return df_top_10

    df.drop(
        [COLUMN_TITLES[4]],
        axis=1,
        inplace=True
    )
    turnover_sum = df[COLUMN_TITLES[3]].sum()
    df_top_10 = df.sort_values(by=COLUMN_TITLES[3], ascending=False).head(10)
    df_top_10['Доля'] = df_top_10[COLUMN_TITLES[3]] / turnover_sum
    return df_top_10


def get_overdue_receivable(dataframe):
    pass


if __name__ == '__main__':
    for file in FILES:

        # 1 проверяем номер ОСВ в названии файла
        osv_number = get_osv_number(file)
        if osv_number is None:
            continue

        # 2 получаем датафрейм
        df = get_dataframe(file, osv_number)

        # 3 обрабатываем данные в зависимости от номера осв
        # 3.1 отдельная функция для осв 60 и 62 по крупным контрагентам
        top_10_counterparts = get_top_10_counterparts(df, osv_number)

        # 3.2 отдельная для 60/62/76 по просроченной ДЗ
        overdue_receivable = get_overdue_receivable(df)
        # 4 наводим красоту и сохраняем результат

        if file.endswith('xls'):  # pandas не сохраняет старый формат
            file = file.replace('xls', 'xlsx')
        top_10_counterparts.to_excel(f'{OUTPUT_DIR}{file}', index=False)
        overdue_receivable.to_excel(f'{OUTPUT_DIR}{file}', index=False)

