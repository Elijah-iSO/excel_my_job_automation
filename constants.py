import os

COLUMN_TITLES_TOP_10 = [
    'Контрагенты',
    'Оборот за период, тыс. руб.',
    'Доля, %',
]

COLUMN_TITLES_DZ = [
    'Дебитор',
    'Сумма, тыс. руб.',
    'Комментарий',
]

START_PATTERN = r"^6(0|2)\.[0-9]1.*$"
END_PATTERN = r"^6(0|2)\.[0-9]2.*$"
INN_PATTERN = r"^\d{10}(\d{2})?$|^\d{12}$"

FILES = os.listdir('files/')
INPUT_DIR = os.getcwd() + '/files/'
OUTPUT_DIR = os.getcwd() + '/results/'
