import pandas as pd

def read_file():
    df_tires = pd.read_excel('data_read/tyres.xlsx')
    print(df_tires)


def find_diff():

    df1 = pd.read_excel('data_read/kub2.xlsx')
    df2 = pd.read_excel('data_read/file.xlsx')

    df1['Контрагент RN'] = df1['Контрагент RN'].fillna(0).astype('int64')
    df2['Контрагент RN'] = df2['Контрагент RN'].fillna(0).astype('int64')

    merged = pd.merge(df1, df2, on='Контрагент RN', how='outer', indicator=True)
    not_found = merged[merged['_merge'] != 'both']

    not_found.to_excel('различия.xlsx', index=False)



if __name__ == '__main__':
    read_file()