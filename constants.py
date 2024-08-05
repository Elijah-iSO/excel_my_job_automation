import os

COLUMN_TITLES_TOP_10 = [
    'Контрагенты',
    'Оборот за период, тыс. руб.',
    'Доля, %',
]

COLUMN_TITLES_DZ = [
    'Дебитор',
    'Сумма, тыс. руб.',
]

START_PATTERN = r"^6(0|2)\.[0-9]1.*$"
END_PATTERN = r"^6(0|2)\.[0-9]2.*|Итого$"
OSV_DZ_PATTERN = r'^(60|62|76)$'
AV_VA_PATTERN = r'^76\.(АВ|ВА)$'
# INN_PATTERN = r"^\d{10}(\d{2})?$|^\d{12}$"

INPUT_DIR = os.getcwd() + '/files/'
OUTPUT_DIR = os.getcwd() + '/results/'
FILES = os.listdir(INPUT_DIR)


PERCENT = 100
K = 1000
KK = 1000000

FILE_HANDLERS = {
    ('60', '62'): process_60_62,
    ('60', '62', '76'): process_60_62_76,
    ('50', '51', '52'): process_50_51_52,
    ('.pdf',): process_pdf,
}
