import pandas as pd
import openpyxl

def read_file():
    df_tires = pd.read_excel('data_read/tyres.xlsx')
    print(df_tires)


def string_with_found_word():
    df = pd.read_excel('data_read/tyres.xlsx')
    search_word = 'Winter'
    result = df[df.apply(lambda row: row.astype(str).str.contains(search_word, case=False).any(), axis=1)]
    print(result)


def find_word_in_file():
    workbook = openpyxl.load_workbook('data_read/tyres.xlsx')
    sheet = workbook.active
    search_word = 'SUV'
    word_found = False

    for row in sheet.iter_rows(values_only=True):
        for cell in row:
            if search_word in str(cell):
                print(f'Слово {search_word} найдено в файле tyres.xls')
                word_found = True
                break
        if word_found:
            break
    if not word_found:
            print(f'Слово {search_word} не найдено')

    # workbook.close()



def find_diff():

    df1 = pd.read_excel('data_read/Подписка_апрель_2024 (2).xlsx')
    df2 = pd.read_excel('data_read/Подписка_апрель_2024 (замечания).xlsx')

    df1['Контрагент RN'] = df1['Контрагент RN'].fillna(0).astype('int64')
    df2['Контрагент RN'] = df2['Контрагент RN'].fillna(0).astype('int64')

    merged = pd.merge(df1, df2, on='Контрагент RN', how='outer', indicator=True)
    not_found = merged[merged['_merge'] != 'both']

    not_found.to_excel('различия.xlsx', index=False)



if __name__ == '__main__':
    find_word_in_file()