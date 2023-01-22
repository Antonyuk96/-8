Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import csv
def read():
    with open('Копия 060922 Семинар 1 - Задача 1.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        for rec in reader:
            print(rec)
            def delete_data():
                with open('Копия 060922 Семинар 1 - Задача 1.csv', 'r', newline='\n', encoding='utf-8') as f:
                    try:
                        n_fio = input('Введите ФИО ученика, оторого хотите удалить из списка:')
                    except ValueError:
                    found = 0
                    
SyntaxError: expected an indented block after 'except' statement on line 10
try:
                        n_fio = input('Введите ФИО ученика, оторого хотите удалить из списка:')
                    except ValueError:
                        
SyntaxError: unindent does not match any outer indentation level
try:
                        n_fio = input('Введите ФИО ученика, оторого хотите удалить из списка:')
except ValueError:
    error_enter()
found = 0
SyntaxError: invalid syntax
ry:
                        n_fio = input('Введите ФИО ученика, оторого хотите удалить из списка:')
except ValueError:
    error_enter()
    
SyntaxError: invalid syntax
ry:
                        n_fio = input('Введите ФИО ученика, оторого хотите удалить из списка:')
except ValueError:
    
SyntaxError: invalid syntax
SyntaxError: invalid syntax
SyntaxError: incomplete input
try:
                        n_fio = input('Введите ФИО ученика, оторого хотите удалить из списка:')
except ValueError:
    error_enter()
    found = 0
...     r = csv.reader(f, delimiter=";")
...     nrec = []
...     for rec in r:
...         if rec[0] == n_fio:
...             print('deleted record:', rec)
...             found = 1
...             else:
...                 
SyntaxError: invalid syntax
>>> if rec[0] == n_fio:
...             print('deleted record:', rec)
...             found = 1
... else:
...     nrec.append(rec)
...     if found == 0:
...         print('Ошибка.Пожалуйста,попробуйте снова')
...         f.close()
...         else:
...             
SyntaxError: invalid syntax
>>> else:
...     
SyntaxError: invalid syntax
>>>     else:
...         
SyntaxError: unexpected indent
>>>     else:
...         
SyntaxError: unexpected indent
>>> if found == 0:
...         print('Ошибка.Пожалуйста,попробуйте снова')
...         f.close()
... else:
...     with open('опия 060922 Семинар 1 - Задача 1.csv', 'w', newline='', encoding='utf-8') as f:
...         w = csv.writer(f, delimiter=';')
...         w.writerows(nrec)
...        # read()
... # delete_data()
