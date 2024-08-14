import pandas as pd
import tabula

from constants import OUTPUT_DIR, INPUT_DIR


def save_result(df, osv_number=None, name=None):
    path = f'{OUTPUT_DIR}{name}_{osv_number}.xlsx'
    df.to_excel(path, index=False)


def get_dataframe(file, file_suffix):
    if file_suffix == 'pdf':
        tables = tabula.read_pdf(
            f'{INPUT_DIR}{file}',
            pages='all',
            multiple_tables=True
        )
        concat_dataframe = pd.concat(tables, axis=1)
        return concat_dataframe

    excel = pd.read_excel(
        f'{INPUT_DIR}{file}',
        header=None,
    )
    return excel
