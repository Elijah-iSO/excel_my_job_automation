import pandas as pd

from constants import OUTPUT_DIR


def get_osv_number(file):
    if '60' in file:
        return '60'
    elif '62' in file:
        return '62'
    elif '76' in file:
        return '76'
    else:
        return None


def save_result(df, osv_number=None):
    path = f'{OUTPUT_DIR}ТОП10_{osv_number}.xlsx'
    df.to_excel(path, index=False)
