import pandas as pd
import openpyxl
import logging

"""
    Логирование действий с Excel файлами
"""
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename = 'app.log',
    filemode = 'w',
)

def log_function_call(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Вызвана функция {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_function_call
def read_file():
    """
    Вывод записей из Excel файла
    """
    df = pd.read_excel('data_read/tyres.xlsx')
    print(df)


@log_function_call
def string_with_found_word(search_word = 'Winter'):
    """
    Вывод строки с найденным словом
    """
    df = pd.read_excel('data_read/tyres.xlsx')
    result = df[df.apply(lambda row: row.astype(str).str.contains(search_word, case=False).any(), axis=1)]
    print(result)

@log_function_call
def find_word_in_file():
    """
    Поиск слова в Excel файле, запись найденных слов
    """
    workbook = openpyxl.load_workbook('data_read/tyres.xlsx')
    sheet = workbook.active
    search_word = 'SUV'
    word_found = False

    file = open('found_words', 'w')
    for row in sheet.iter_rows(values_only=True):
        for cell in row:
            if search_word in str(cell):
                print(f'Слово {search_word} найдено в файле tyres.xls')
                word_found = True
                file.write(search_word)
                break
        if word_found:
            break
    if not word_found:
            print(f'Слово {search_word} не найдено')

    workbook.close()

    with open('found_words', 'r') as file:
        lines = file.readlines()
        print(f'Все найденные слова в файле -- {lines}')


@log_function_call
def find_diff():
    """
    Сравнение файлов и запись различий в отдельный Excel файл
    """
    try:
        df1 = pd.read_excel('data_read/rn_landsail_limits.xlsx')
        df2 = pd.read_excel('data_read/limits_landsail.xlsx')
        merged = pd.merge(df1[['RN Контрагент']], df2[['RN Контрагент']], on='RN Контрагент', how='outer', indicator=True)
        not_found = merged[merged['_merge'] != 'both']

        not_found.to_excel('различия.xlsx', index=False)

        print("Различия успешно записаны в 'различия_new.xlsx'.")

    except Exception as e:
        print(f"Произошла ошибка: {e}")
@log_function_call
def find_empty_space():
    file_path = 'data_read/output.xlsx'
    df = pd.read_excel(file_path)
    empty_columns = df.columns[df.isnull().any()]

    print("Колонки с пустыми значениями:")
    for column in empty_columns:
        print(column)
@log_function_call
def find_empty_space():
    file_path = 'data_read/output.xlsx'
    df = pd.read_excel(file_path)
    empty_columns = df.columns[df.isnull().any()]
    print("Колонки с пустыми значениями:")
    for column in empty_columns:
        print(column)



if __name__ == '__main__':
    find_empty_space()


