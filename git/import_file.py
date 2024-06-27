import pandas as pd

def read_file():
    df_tires = pd.read_excel('data_read/tyres.xlsx')
    print(df_tires)




if __name__ == '__main__':
    read_file()