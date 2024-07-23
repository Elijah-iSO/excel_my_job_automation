import os
import re

import pandas as pd

# Перебираем файлы в директории с приложением
# точка означает текущую директорию
files = os.listdir('.')

# Определяем путь к директории приложения
base_dir = (os.getcwd() + '/')

for file in files:
    if '60 за 2' in file:
        osv_60 = pd.read_excel(base_dir + file, header=None)
    elif '62' in file:
        osv_62 = pd.read_excel(base_dir + file, header=None)
    elif '76' in file:
        osv_76 = pd.read_excel(base_dir + file, header=None)

# Тестим 60 ОСВ, ищем крупнейших поставщиков
turnover_KT = []
providers_10 = []
pattern = r"^60\.[0-9]1.*$"

filtered_rows = osv_60[osv_60.iloc[:, 0].astype(str).str.match(pattern)]
print(filtered_rows)
total_turnover_KT = filtered_rows.iloc[:, 4].sum()
print(total_turnover_KT)
exit()

for row in osv_60.iterrows():
    if row[6] is not None and '60.' not in row[0]:
        providers_10.append(row)
top_providers_10 = sorted(providers_10, reverse=True)
top_providers_10 = top_providers_10[:10]

#print(providers_10)

print(top_providers_10[0])
