import pandas as pd

from constants import FILES
from file_handlers import FILE_HANDLERS
from utils import get_dataframe

if __name__ == '__main__':
    results = {}

    for file in FILES:
        for (handler, file_suffixes) in FILE_HANDLERS.items():
            file_suffix = next(
                (file_suffix for file_suffix in file_suffixes if file_suffix in file),
                None
            )
            if file_suffix:
                sheet_name = f'{file_suffix}_{handler.__name__}'
                dataframe = get_dataframe(file, file_suffix)

                result = handler(dataframe.copy(), suffixes=file_suffix)
                results[sheet_name] = result

    with pd.ExcelWriter('Результат обработки файлов.xlsx') as writer:
        for sheet_name, df in results.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)
