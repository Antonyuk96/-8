Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import csv
def read():
    with open('Копия 060922 Семинар 1 - Задача 1.csv', 'r', newline='\n', encoding='utf-8') as f:
        r = csv.reader(f, delimiter=";")
        for rec in r:
            print(rec)
            def update():
                with open('Копия 060922 Семинар 1 - Задача 1.csv', 'r', newline='\n', encoding='utf-8') as f:
                    n_fio = input('Введите ФИО учентка, по которому хотите внести изменения:')
                    print('1. Изменить ФИО')
                    print('2. Изменить дату рождения')
                    print('3. Изменить класс')
                    print('4. Изменить ряд')
                    print('5. Изменить парту')
                    print('6. Вариант')
                    print('7. Изменить статус по оценкам')
                    print('8. Изменить заметки')
                    try:
                        n = int(input('Введите раздел,который хотели бы изменить (1,2->8):'))
                        except ValueError:
                            
SyntaxError: invalid syntax
try:
                        n = int(input('Введите раздел,который хотели бы изменить (1,2->8):'))
except ValueError:
    error_enter()
     found = 0
     
SyntaxError: unexpected indent
try:
                        n = int(input('Введите раздел,который хотели бы изменить (1,2->8):'))
except ValueError:
    error_enter()
    found = 0
    r = csv.reader(f, delimiter=";")
     nrec = []
     
SyntaxError: unexpected indent
 nrec = []
 
SyntaxError: unexpected indent
SyntaxError: unexpected indent
SyntaxError: incomplete input
nrec = []
for rec in r:
    if rec[0] == n_id:
         if rec[0] == n_fio:
             if n == 1:
                 print('Текущая запись:', rec)
                 rec[1] = input("Введите новое имя:")
                 print('Обновлённая запись:', rec)
                 found = 1
             elif n == 2:
                 print('Текущая запись:', rec)
                 rec[2] = input("Введите новую дату рождения:")
                 print('Обовлённая запись:', rec)
                 found = 1
             elif n == 3:
                 print('Текущая запись:', rec)
                 rec[3] = input("Введите новый класс:")
                  print('Обновлённая запись:', rec)
                  
SyntaxError: unexpected indent
print('Updated record:', rec)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    print('Updated record:', rec)
NameError: name 'rec' is not defined. Did you mean: 'nrec'?
for rec in r:
    if rec[0] == n_id:
         if rec[0] == n_fio:
             if n == 1:
                 print('Текущая запись:', rec)
                 rec[1] = input("Введите новое имя:")
                 print('Обновлённая запись:', rec)
                 found = 1
             elif n == 2:
                 print('Текущая запись:', rec)
                 rec[2] = input("Введите новую дату рождения:")
                 print('Обовлённая запись:', rec)
                 found = 1
             elif n == 3:
                 print('Текущая запись:', rec)
                 rec[3] = input("Введите новый класс:")
                 print('Обновлённая запись:', re)
                 found = 1
             elif n == 4:
                 print('Текущая запись:', rec)
                 rec[4] = input("Введите новый ряд:")
                 print('Обовлённая запись:', rec)
                 found = 1
             elif n == 5:
                 print('Текущая запись:', rec)
                 rec[5] = input("Введите новую парту:")
                 print('Обовлённая запись:', rec)
                 found = 1
             elif n == 6:
                print('Текущая запись:', rec)
                rec[6] = input("Введите новый вариант:")
                print('Обовлённая запись:', rec)
                found = 1
             elif n == 7:
                 print('Текущая запись:', rec)
                 rec[7] = input("Введите новый статус по оценкам:")
                 print('Обовлённая запись:', rec)
                 found = 1
             elif n == 8:
                 print('Текущая запись:', rec)
                 rec[8] = input("Введите новые заметки:")
                 print('Обовлённая запись:', rec)
                 found = 1
                 nrec.append(rec)
                 if found == 0:
                      print('Ошибка.Попробуйте снова')
                      error_enter()
...                       f.close()
...                  else:
...                      with open('Копия 060922 Семинар 1 - Задача 1.csv', 'w', newline='', encoding='utf-8') as f
...                      
SyntaxError: incomplete input
>>> SyntaxError: incomplete input
SyntaxError: incomplete input
>>> if found == 0:
...                       print('Ошибка.Попробуйте снова')
...                       error_enter()
...                       f.close()
... else:
...     with open('Копия 060922 Семинар 1 - Задача 1.csv', 'w', newline='', encoding='utf-8') as f:
...         w = csv.writer(f, delimiter=';')
...          w.writerows(nrec)
...          
SyntaxError: unexpected indent
>>> w.writerows(nrec)
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    w.writerows(nrec)
NameError: name 'w' is not defined
>>> w = csv.writer(f, delimiter=';')
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    w = csv.writer(f, delimiter=';')
NameError: name 'f' is not defined
>>> if found == 0:
...                       print('Ошибка.Попробуйте снова')
...                       error_enter()
...                       f.close()
... else:
...     with open('Копия 060922 Семинар 1 - Задача 1.csv', 'w', newline='', encoding='utf-8') as f:
...         w = csv.writer(f, delimiter=';')
...         w.writerows(nrec)
...        # read()
