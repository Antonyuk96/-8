Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import log
from person_search2 import person_search
from print_info import print_hogwarts
from find_of_atribute import print_position
from adding_info import adding
from model_update_1 import read, update
from model_delete import delete_data
from exceptions import user_choice







def input_menu_choice():
    log.start_app()
    while True:
         print()
         print('-----------------------')
         print('Что Вы хотите сделать?')
           print('-----------------------')
           
SyntaxError: unexpected indent
print('-----------------------')
-----------------------
print()

print('1.Показать всё')
1.Показать всё
print('2. Найти информацию')
2. Найти информацию
print('3. Добавить информацию')
3. Добавить информацию
 print('4. Изменить информацию')
 
SyntaxError: unexpected indent
print('4. Изменить информацию')
4. Изменить информацию
print('5. Удалить информацию')
5. Удалить информацию
print('0. Exit')
0. Exit
choice_menu = user_choice()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    choice_menu = user_choice()
NameError: name 'user_choice' is not defined
choice_menu = user_choice()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    choice_menu = user_choice()
NameError: name 'user_choice' is not defined
from exceptions import user_choice
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    from exceptions import user_choice
  File "C:\Users\NewGamePC\AppData\Local\Programs\Python\Python311\exceptions.py", line 1
    Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
           ^^^^
SyntaxError: invalid syntax
>>> from exceptions import user_choice
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    from exceptions import user_choice
  File "C:\Users\NewGamePC\AppData\Local\Programs\Python\Python311\exceptions.py", line 1
    Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
           ^^^^
SyntaxError: invalid syntax
>>> from exceptions.py import user_choice
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    from exceptions.py import user_choice
  File "C:\Users\NewGamePC\AppData\Local\Programs\Python\Python311\exceptions.py", line 1
    Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
           ^^^^
SyntaxError: invalid syntax
>>> from exceptions.py import User_choice
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    from exceptions.py import User_choice
  File "C:\Users\NewGamePC\AppData\Local\Programs\Python\Python311\exceptions.py", line 1
    Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
           ^^^^
SyntaxError: invalid syntax
from exceptions.py import user_choice

choice_menu = user_choice()
if choice_menu == 1:
            print_copy()
        elif choice_menu == 2:
            print('1. Найти по имени')
            print('2. Найи по классу')
            print('0. Выход')
            choice1 = user_choice()
            if choice1 == 1:
                person_search()
            elif choice1 == 2:
                print_position()
            elif choice1 == 0:
                log.end_app()
                input_menu_choice()
            else:
                print('Error')
                log.error_enter()
                input_menu_choice()
        elif choice_menu == 3:
            adding()
            log.add()
            print('Данные были успешно добавлены')
        elif choice_menu == 4:
            read()
            update()
            log.change()
        elif choice_menu == 5:
            read()
            delete_data()
            log.del_item()
        elif choice_menu == 0:
            log.end_app()
            return exit()
        else:
            print('Error')
            log.error_enter()
            return input_menu_choice()


input_menu_choice()


