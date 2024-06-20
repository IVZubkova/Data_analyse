import pandas as pd
import numpy as np
import re


def read_file():
    df_tires = pd.read_excel('data_read/tyres.xlsx')
    # print(df_tires)
    tyres_suv = df_tires['SUV 2'].apply(lambda x: re.search(r, str(x).lower()))
    print(tyres_suv)







#Поиск слова/слов в файле
# def find_attribute():





# def analize_file():
#     """Взято из наших предыдущих занятий,
#     можно будет внутри элифов наделать еще выборов, если потребуется
#     надеюсь, что это чем-то поможет =))) С любовью от Лины"""
#     spr = '#' * 38
#     print(spr, ' Вас приветствует служба работы с БД! ', spr, sep='\n')
#     while True:
#         print('Выберите действие: \n\t'
#               '1 - Вывести БД\n\t'
#               '2 - Добавить информацию\n\t'
#               '3 - Удалить информацию\n\t'
#               '4 - Изменить информацию\n\t'
#               '5 - Выйти из программы')
#         print(spr)
#         action = input()
#         print(spr)
#         if action == '1':
#             print_data_base()
#         elif action == '2':
#             input(' Выберите информацию, которую хотите добавить ')
#         elif action == '3':
#             input(' Что Вы хотите удалить? ')
#         elif action == '4':
#             print(' Что Вам нужно изменить? =) ')
#         else:
#             action == '5'
#             print()
#             print(' До новых встреч ')
#             print()
#             break

if __name__ == '__main__':
    read_file()



#Посмотрел твой код.

