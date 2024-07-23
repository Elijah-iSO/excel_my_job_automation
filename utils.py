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


def save_result(df, file):
    if file.endswith('xls'):  # pandas не сохраняет старый формат
        file = file.replace('xls', 'xlsx')
    df.to_excel(f'{OUTPUT_DIR}{file}', index=False)
