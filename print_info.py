Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from os import path
>>> def print_copy():
...     file = 'Копия 060922 Семинар 1 - Задача 1.csv'
...     if path.exists(file):
...         show_all()
...         with open(file, 'r', encoding='utf-8') as text:
...             ext_csv = text.readlines()
...              for i, v in enumerate(text_csv):
...                  
SyntaxError: unexpected indent
>>>  for i, v in enumerate(text_csv):
...      
SyntaxError: unexpected indent
>>> for i, v in enumerate(text_csv):
...     print(v.strip())
