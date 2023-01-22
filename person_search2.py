Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def person_search():
...     fio = input('Введите ФИО: ')
...     search(fio)
...     with open('Копия 060922 Семинар 1 - Задача 1.csv', 'r', encoding='utf_8') as data:
...         data_list = data.readlines()
...         for i in range(1, len(data_list)):
...             if name in data_list[i]:
...                 print(data_list[i])
...                 break
...             else:
...                 error_enter()
