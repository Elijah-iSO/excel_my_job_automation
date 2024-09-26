# Автоматизация работы

## Описание
Создан для автоматизации части банковской работы, в частности автоматизирует рутину по анализу ОСВ, Карточек счетов, Отчетности.
Находится в разработке и периодически улучшается.

## Запуск
На сегодняшний день работает в виде скрипта, поэтому для запуска достаточно:
1. **Клонируйте репозиторий:**

   ```bash
   git clone git@github.com:Elijah-iSO/excel_my_job_automation.git
   cd excel_my_job_automation
   ```
   
2. **Создание и активация окружения:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
   
3. **Обновление pip и установка зависимостей:**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Создайте папку `files` и скопируйте в нее ваши .xls, .pdf файлы:**

   ```bash
   mkdir files
   ```

5. **Запустите, результат обработки появится в директории `results`:**

   ```bash
   python3 main.py
   ```

## План
- [ ] отточить работу скрипта; 
- [ ] написать тесты;
- [ ] перенести в вэб для совместного доступа;
- [ ] (To Be Continued...)

## Cтек технологий
<span style="display: inline-block; margin-right: 5px;">![alt text](https://img.shields.io/badge/python-3.9-blue)
</span>
<span style="display: inline-block; margin-right: 5px;">
![alt text](https://img.shields.io/badge/distro-1.9.0-brightgreen)
</span><span style="display: inline-block; margin-right: 5px;">
![alt text](https://img.shields.io/badge/et--xmlfile-1.1.0-orange)
</span><span style="display: inline-block; margin-right: 5px;">
![alt text](https://img.shields.io/badge/JPype1-1.5.0-yellow)
</span><span style="display: inline-block; margin-right: 5px;">
![alt text](https://img.shields.io/badge/numpy-1.26.4-blue)
</span><span style="display: inline-block; margin-right: 5px;">
![alt text](https://img.shields.io/badge/openpyxl-3.1.5-green)
</span><span style="display: inline-block; margin-right: 5px;">
![alt text](https://img.shields.io/badge/packaging-24.1-red)
</span><span style="display: inline-block; margin-right: 5px;">
![alt text](https://img.shields.io/badge/pandas-2.2.2-blue)
</span><span style="display: inline-block; margin-right: 5px;">
![alt text](https://img.shields.io/badge/python--dateutil-2.9.0-yellowgreen)
</span><span style="display: inline-block; margin-right: 5px;">
![alt text](https://img.shields.io/badge/pytz-2024.1-blue)
</span><span style="display: inline-block; margin-right: 5px;">
![alt text](https://img.shields.io/badge/six-1.16.0-orange)
</span><span style="display: inline-block; margin-right: 5px;">
![alt text](https://img.shields.io/badge/tabula--py-2.9.3-red)
</span><span style="display: inline-block; margin-right: 5px;">
![alt text](https://img.shields.io/badge/tzdata-2024.1-green)
</span><span style="display: inline-block; margin-right: 5px;">
![alt text](https://img.shields.io/badge/xlrd-2.0.1-lightgrey)
</span><span style="display: inline-block; margin-right: 5px;">
![alt text](https://img.shields.io/badge/re-python-blue)
</span>

## Автор
ILYA OLEYNIKOV
GitHub:	https://github.com/Elijah-iSO
E-mail: oleynikovis@yandex.ru
