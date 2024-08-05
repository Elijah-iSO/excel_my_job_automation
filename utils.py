import pandas as pd
import tabula

from constants import OUTPUT_DIR, INPUT_DIR


def get_osv_number(file: str):
    if '60' in file:
        return '60'
    elif '62' in file:
        return '62'
    elif '76' in file:
        return '76'
    elif file.endswith('.pdf'):
        parce_pdf(file)
    else:
        return None


def save_result(df, osv_number=None, name=None):
    path = f'{OUTPUT_DIR}{name}_{osv_number}.xlsx'
    df.to_excel(path, index=False)


def parce_pdf(file):
    tables = tabula.read_pdf(
        f'{INPUT_DIR}{file}',
        pages='all',
        multiple_tables=True)

    if tables:
        # Создаем пустой Excel-файл
        writer = pd.ExcelWriter('all_tables.xlsx')

        # Проходимся по каждой найденной таблице
        for i, table in enumerate(tables):
            # Преобразуем таблицу в DataFrame (если это ещё не DataFrame)
            if not isinstance(table, pd.DataFrame):
                table = pd.DataFrame(table)

            # Сохраняем таблицу в отдельном листе Excel
            table.to_excel(writer, sheet_name=f'Sheet_{i + 1}', index=False)

        # Сохраняем Excel-файл
        writer._save()
