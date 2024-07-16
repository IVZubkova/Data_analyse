import pandas as pd
import openpyxl
import logging

def read_file():
    """
    Вывод записей из Excel файла
    """
    df_tires = pd.read_excel('data_read/tyres.xlsx')
    print(df_tires)


def string_with_found_word():
    """
    Вывод строки с найденным словом
    """
    df = pd.read_excel('data_read/tyres.xlsx')
    search_word = 'Winter'
    result = df[df.apply(lambda row: row.astype(str).str.contains(search_word, case=False).any(), axis=1)]
    print(result)


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


def find_diff():
    """
    Сравнение файлов и запись различий в отдельный Excel файл
    """

    df1 = pd.read_excel('data_read/Подписка_апрель_2024 (2).xlsx')
    df2 = pd.read_excel('data_read/Подписка_апрель_2024 (замечания).xlsx')

    df1['Контрагент RN'] = df1['Контрагент RN'].fillna(0).astype('int64')
    df2['Контрагент RN'] = df2['Контрагент RN'].fillna(0).astype('int64')

    merged = pd.merge(df1, df2, on='Контрагент RN', how='outer', indicator=True)
    not_found = merged[merged['_merge'] != 'both']

    not_found.to_excel('различия.xlsx', index=False)

def write_logs():
    """
    Логироание действий с Excel файлами
    """
    logging.basicConfig(
        level=logging.INFO
    )
if __name__ == '__main__':
    read_file()