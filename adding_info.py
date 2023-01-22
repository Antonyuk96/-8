Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def adding():
     to_add = []
    print("\nВы добавляете информацию в базу.Если вы не знаете что добавить в базу, пишите Нет\n")
    
SyntaxError: unindent does not match any outer indentation level
 = []
    print("\nВы добавляете информацию в базу.Если вы не знаете что добавить в базу, пишите: Нет\n")
    
SyntaxError: unexpected indent
print("\nВы добавляете информацию в базу.Если вы не знаете что добавить в базу, пишите: Нет\n")

Вы добавляете информацию в базу.Если вы не знаете что добавить в базу, пишите: Нет

to_add.append(input('ФИО: '))
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    to_add.append(input('ФИО: '))
NameError: name 'to_add' is not defined
to_add = []
to_add.append(input('ФИО: '))
ФИО: 
to_add.append(input('Дата рождения: '))
Дата рождения: 
o_add.append(input('Класс: '))
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    o_add.append(input('Класс: '))
NameError: name 'o_add' is not defined. Did you mean: 'to_add'?
to_add.append(input('Subject: '))
Subject: 
o_add.append(input('Класс: '))
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    o_add.append(input('Класс: '))
NameError: name 'o_add' is not defined. Did you mean: 'to_add'?
to_add.append(input('Класс: '))
Класс: 
to_add.append(input('Ряд: '))
Ряд: 
o_add.append(input('Парта: '))
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    o_add.append(input('Парта: '))
NameError: name 'o_add' is not defined. Did you mean: 'to_add'?
to_add.append(input('Парта: '))
Парта: 
to_add.append(input('Вариант: '))
Вариант: 
to_add.append(input('Статус по оценкам: '))
Статус по оценкам: 
>>> to_add.append(input('Заметки: '))
Заметки: 
>>>  with open('Копия 060922 Семинар 1 - Задача 1.csv', "a", encoding='utf-8') as base:
...      
SyntaxError: unexpected indent
>>>  with open('Копия 060922 Семинар 1 - Задача 1.csv', "a", encoding='utf-8') as base:
...      
SyntaxError: unexpected indent
>>> with open('Копия 060922 Семинар 1 - Задача 1.csv', "a", encoding='utf-8') as base:
...    base.write('{};{};{};{};{};{}\n'.format(to_add[0], to_add[1], to_add[2], to_add[3], to_add[4],to_add[5], to_add[6], to_add[7]]))
...    
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
>>> base.write('{};{};{};{};{};{}\n'.format(to_add[0], to_add[1], to_add[2], to_add[3], to_add[4],to_add[5], to_add[6], to_add[7]))
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    base.write('{};{};{};{};{};{}\n'.format(to_add[0], to_add[1], to_add[2], to_add[3], to_add[4],to_add[5], to_add[6], to_add[7]))
NameError: name 'base' is not defined. Did you mean: 'False'?
>>> with open('Копия 060922 Семинар 1 - Задача 1.csv', "a", encoding='utf-8') as base:
... base.write('{};{};{};{};{};{}\n'.format(to_add[0], to_add[1], to_add[2], to_add[3], to_add[4],to_add[5], to_add[6], to_add[7]))
SyntaxError: expected an indented block after 'with' statement on line 1
>>> base.write('{};{};{};{};{};{}\n'.format(to_add[0], to_add[1], to_add[2], to_add[3], to_add[4],to_add[5], to_add[6], to_add[7]))
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    base.write('{};{};{};{};{};{}\n'.format(to_add[0], to_add[1], to_add[2], to_add[3], to_add[4],to_add[5], to_add[6], to_add[7]))
NameError: name 'base' is not defined. Did you mean: 'False'?
>>> with open('Копия 060922 Семинар 1 - Задача 1.csv', "a", encoding='utf-8') as base:
...     base.write('{};{};{};{};{};{}\n'.format(to_add[0], to_add[1], to_add[2], to_add[3], to_add[4],to_add[5], to_add[6], to_add[7]))
