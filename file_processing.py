import re
import pandas as pd
import numpy as np

from constants import (AV_VA_PATTERN, K, KK, COLUMN_TITLES_DZ,
                       COLUMN_TITLES_TOP_10, END_PATTERN, OSV_DZ_PATTERN,
                       PERCENT, START_PATTERN)


def statements(df, suffixes=None):
    return df


def top_10(df, suffixes):

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

    column_to_drop = 1 if '60' in suffixes else 2
    cleared_df.drop(cleared_df.columns[column_to_drop], axis=1, inplace=True)

    turnover_total = cleared_df[cleared_df.columns[1]].sum() / K
    cleared_df[cleared_df.columns[1]] = cleared_df.iloc[:, 1] / K
    df_top_10 = cleared_df.sort_values(by=cleared_df.columns[1], ascending=False).head(10)
    df_top_10[COLUMN_TITLES_TOP_10[2]] = df_top_10.iloc[:, 1] / turnover_total * PERCENT

    df_top_10.columns = COLUMN_TITLES_TOP_10

    return df_top_10


def receivable_overdue(df, suffixes=None):
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


def receipts(df, suffixes=None):
    result_dict = {}
    cleared_df = df.dropna(how='all').dropna(axis=1, how='all')
    for index, row in cleared_df.iterrows():
        for i, cell_value in enumerate(row):

            if i == 0 and not pd.isna(cell_value):
                key_value = cell_value
                continue

            if str(cell_value) == '62':
                for value_index in range(i + 1, len(row)):
                    if not pd.isna(row[value_index]) and str(row[value_index]) != '62':
                        result_dict[key_value] = [int(row[value_index])]
                        break

    print(result_dict)

    return pd.DataFrame(result_dict)
