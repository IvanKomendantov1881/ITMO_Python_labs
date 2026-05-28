# f = open('books.csv', 'r').readlines()
# matric = list()
# for i in f:
#     for j in i.split(';'):
#         matric.append([j])
# print(matric[:50])
# def cnt_name(matric):
#     cnt = 0
#     for i in range(1, len(matric), 13):
#         for h in matric[i]:
#             if len(h) > 30:
#                 cnt +=1
#     return cnt
# print(cnt_name(matric))
#
#
# name_author_book = input('Введите автора книги:')
# for i in range(1, len(matric[:50]), 13):
#     list_name_book = [matric[i+2], matric[i]]
#     for h in list_name_book:
#         if [name_author_book] == h and int(matric[i+6][0]) >= 150:
#             print()
#
#     print(matric[i-1], matric[i], matric[i+1], matric[i+2], matric[i+3], matric[i+4], matric[i+5], matric[i+6], matric[i+7], matric[i+8], matric[i+9], matric[i+10])
import random
from calendar import prweek
from dis import pretty_flags

# import pandas as pd
# import random as rd
# df = pd.read_csv('books.csv', sep=';', encoding='utf-8', na_values=['null'])

# 1
# def cnt_name():
#     return (df['Название'].str.len() > 30).sum()
# print(cnt_name())


# 2
# def search_book():
#     name_author = input('Введите название автора:').strip()
#     min_price = 150
#     df['Автор'] = df['Автор'].str.strip()
#     df['Цена поступления'] = pd.to_numeric(df['Цена поступления'])
#     mask = (df['Автор'] == name_author) & (df['Цена поступления'] >= min_price)
#     result = df[mask]
#     return result[['Название', 'Автор', 'Цена поступления']]
# print(search_book())

#3
# def rndclub():
#     author = random.choice(df['Автор'])
#     if str(author)[0]=='n':
#         author='Автор не известен'
#     name = random.choice(df['Название'])
#     year = random.choice(df['Дата поступления'])[6:10]
#     return f'{author}. {name} - {year}'
#
# with open('bibliography.txt', 'w', encoding='utf-8') as f:
#     for _ in range(20):
#         f.write(rndclub()+'\n')
# print('file done')
# input("press enter")

# 4
# df = pd.read_xml('currency.xml', parser='etree', encoding='cp1251')
# df['Value'] = df['Value'].str.replace(',','.').astype(float)
# print(df['Value'].sum()/len(df['Value']))

# 5 additional
# def dop_tag():
#     tags = df['Название']
#     list_tags = []
#     set_tags = set()
#     for i in tags:
#         if '#' in i:
#             list_tags.append(i.strip().split('#'))
#     # print(list_tags)
#     for j in list_tags:
#         for h in j:
#             clean_tag = h.strip()
#             if clean_tag:
#                 set_tags.add(clean_tag)
#     return set_tags
# or
# def dop_tag2():
#     set_tags = {tag.strip() for item in df['Название'] if '#' in item for tag in item.split('#') if tag.strip()}
#     return set_tags
# print(dop_tag())
# print(dop_tag2())

# def rndclub():
#     row = df.sample(n=1).iloc[0]
#     author = row['Автор']
#     if str(author).lower().startswith('n'):
#         author = 'Автор не известен'
#     name = row['Название']
#     year = str(row['Дата поступления'])[6:10]
#     return f'{author}. {name} - {year}'
#
# with open('bibliography.txt', 'w', encoding='utf-8') as f:
#     for _ in range(20):
#         f.write(rndclub()+'\n')
# print('file done')

# from tkinter import *
# from tkinter import messagebox
# from PIL import Image, ImageTk
#
# root = Tk()
#
# def generate_key():
#     messagebox.showinfo("Your key", "ABC-123-XYZ")
#
# root['bg'] = '#000000'
# root.title('Key Generator')
# root.wm_attributes('-alpha', 0.7)
# root.geometry('900x600')
# root.resizable(width=False, height=False)
#
# bg_image = Image.open("kilua.jpeg")
# bg_img = bg_image.resize((900, 600))
# bg_photo = ImageTk.PhotoImage(bg_image)
#
# title = Label(root,
#               text='KEY GENERATOR',
#               bg='black',
#               fg='white',
#               font=('SF Pro', 42)
#               )
# title.pack()
#
#
# btn = Button(
#     root,
#     text="generate",
#     bg="white",
#     fg="black",
#     font=("SF Pro", 14),
#     relief="flat",
#     activebackground="#f0f0f0",
#     activeforeground="black",
#     bd=0,
#     command=generate_key
# )
# btn.configure(height=2, width=20)
# btn.pack(pady=100)
# root.eval('tk::PlaceWindow . center')
# btn.pack()
# root.mainloop()

# from tkinter import *
# from tkinter import messagebox
# from PIL import Image, ImageTk
# from string import ascii_uppercase
# from random import *
#
# root = Tk()
#
# def generate(len_key):
#     alpha = f'{ascii_uppercase}012345679'
#     st = ''
#     for i in range(len_key):
#         st += choice(alpha)
#     return st
#
# def schet(key_element):
#     alpha = f'{ascii_uppercase}0123456789'
#     k = 0
#     for chislo, choi in enumerate(alpha, 1):
#         for i in key_element.replace('-', ''):
#             if i.isdigit():
#                 chislo += int(i)
#             elif choi == i:
#                 k += chislo
#     return k
#
# def generate_key():
#     key = ''
#     for i in [5, 4, 4]:
#         key_element = generate(i)
#         while not (10 <= (schet(key_element) // i) <= 15):
#             print(schet(key_element) // i)
#             key_element = generate(i)
#         key += f'{key_element}-'
#     output_label.config(text=f'{key.rstrip('-')}')
#
# root['bg'] = '#000000'
# root.title('Key Generator')
# root.wm_attributes('-alpha', 0.7)
# root.geometry('900x600')
# root.resizable(width=False, height=False)
#
# bg_image = Image.open("kilua.jpeg")
# bg_image_resized = bg_image.resize((900, 600))
# bg_photo = ImageTk.PhotoImage(bg_image_resized)
#
# bg_label = Label(root, image=bg_photo)
# bg_label.place(x=0, y=0, relwidth=1, relheight=1)
# bg_label.image = bg_photo
#
#
# title = Label(root,
#               text='KEY GENERATOR',
#               bg='black',
#               fg='white',
#               font=('SF Pro', 42)
#               )
# title.pack(pady=20)
#
# btn = Button(
#     root,
#     text="generate",
#     bg="white",
#     fg="black",
#     font=("SF Pro", 14),
#     relief="flat",
#     activebackground="#f0f0f0",
#     activeforeground="black",
#     bd=0,
#     command=generate_key
# )
# btn.configure(height=2, width=20)
# btn.pack(pady=100)
#
# output_label = Label(root,
#                      text='',
#                      bg='black',
#                      fg='white',
#                      font=('SF Pro', 26),
#                      )
# output_label.configure(height=2, width=40)
# output_label.pack(pady=20)
#
# root.eval('tk::PlaceWindow . center')
# root.mainloop()


# class Cat:
#     name = None
#     age = None
#     happy = None
#     our_info = []
#
#     def set_date(self, name, age, happy):
#         self.name = name
#         self.age = age
#         self.happy = happy
#
#     def get_date(self):
#         print(self.name, 'age:', self.age, 'Счастлив:', self.happy)
# cat1 = Cat()
# cat1.set_date('Барсик', 21, True)
# cat1.get_date()
# cat2 = Cat()
# cat2.set_date('Борис', 3, False)
# cat2.get_date()

# class Figura:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def volume(self, a, b, c):
#         V = a * b * c
#         print('Объём:', V)
#
#     def __str__(self):
#         print(f'Высота: {self.a}, длина: {self.b}, ширина: {self.c}')
#
#     def __add__(self, other):
#         if isinstance(other, Figura):
#             total_volume = self.volume() + other.volume()
#             return total_volume
#         else:
#             raise TypeError("Можно складывать только объекты класса Figure")
#
#
# class DepthFigure(Figura):
#     def __int__(self, d):
#         self.d = d
#
#     def volume(self, a, b, c):
#         first_figure = super().volume(a,b,c)
#         second_figure = (self.a - self.d) * (self.b - self.d) * (self.c - self.d)
#         third_figure = first_figure - second_figure
#         print('Объем тела с внутренней вполостью:', third_figure)
#
#     def __str__(self):
#         print(f'Стороны тела с внутренней вполостью: a={self.a}, b={self.b}, c={self.c}, d={self.d}')

# --- ПАТЧ ДЛЯ ЗАПУСКА НА НОВЫХ ВЕРСИЯХ PYTHON ---
# import inspect
#
# if not hasattr(inspect, 'getargspec'):
#     inspect.getargspec = inspect.getfullargspec
# # ------------------------------------------------
#
# import pymorphy2
#
# # Инициализация анализатора
# try:
#     morph = pymorphy2.MorphAnalyzer()
# except Exception as e:
#     print("Ошибка при запуске pymorphy2. Убедитесь, что установлено: pip install pymorphy2 pymorphy2-dicts-ru")
#     print(f"Детали ошибки: {e}")
#     exit()
#
# # Твой список (я очистил форматирование, чтобы Python его понял)
# raw_data = [
#     'Ъ', 'О', 'Ь', 'Я', 'О', 'З', 'И', 'K', '3', 'E', 'P', 'T', 'O', 'T', 'Е', 'Ъ', 'Е', 'Ё', 'Щ', 'Н',
#     'Р', 'Н', 'У', 'К', 'Э', 'Н', 'Д', 'Ю', 'Ь', 'П', 'Л', 'Щ', 'Ь', 'Ъ', 'Д', 'Ч', 'О', 'Ф', 'Ж', 'К',
#     'Я', 'Я', 'Е', 'У', 'Ц', 'У', 'Т', 'О', 'В', 'Я', 'М', 'С', 'С', 'Ж', 'Р', 'С', 'С', 'Э', 'Я', 'Щ',
#     'Ж', 'Э', 'Р', 'Р', 'И', 'Н', 'С', 'У', 'И', 'Р', 'A', 'T', 'O', 'Н', 'Ь', 'О', 'Т', 'Л', 'Н', 'Ь',
#     'С', 'Р', 'Э', 'И', 'Ш', 'Р', 'Д', 'И', 'Ц', 'Ч', 'Ф', 'Б', 'У', 'Е', 'С', 'У', 'Х', 'Б', 'А', 'В',
#     'Ч', 'Э', 'Б', 'Я', 'Р', 'Е', 'С', 'К', 'Р', 'И', 'Π', 'Τ', 'Ο', 'Κ', 'Н', 'Р', 'Ц', 'Б', 'Р', 'Ж',
#     'Ж', 'Н', 'И', 'Т', 'Ю', 'Л', 'И', 'М', 'Ы', 'Б', 'И', 'Л', 'Ε', 'Τ', 'Α', 'В', 'Ы', 'Б', 'О', 'Э',
#     'Ч', 'А', 'Ю', 'Й', 'И', 'Я', 'Щ', 'А', 'Р', 'Ч', 'Г', 'A', '3', 'O', 'K', 'К', 'Ф', 'В', 'Д', 'С',
#     'Л', 'В', 'Ж', 'Ж', 'Б', 'Ф', 'Ы', 'Ё', 'Ш', 'Н', 'М', 'Е', 'Л', 'П', 'Ё', 'Ъ', 'Р', 'Ш', 'Н', 'И',
#     'Й', 'Т', 'Н', 'Г', 'Ю', 'Ш', 'С', 'Щ', 'В', 'И', 'Ж', 'Т', 'A', 'К', 'O', 'В', 'Д', 'А', 'И', 'Ф',
#     'Б', 'С', 'Р', 'О', 'Б', 'Ш', 'О', 'А', 'Е', 'Ъ', 'О', 'Л', 'Я', 'Х', 'В', 'Х', 'И', 'Ч', 'К', 'И',
#     'Γ', 'Μ', 'Ε', 'Р', 'З', 'Ъ', 'Й', 'П', 'Л', 'Р', 'O', 'T', 'P', 'А', 'Б', 'О', 'Т', 'К', 'И', 'X',
#     'И', 'Е', 'М', 'Ч', 'К', 'В', 'И', 'Р', 'Е', 'Ф', 'Ч', 'Щ', 'Ш', 'З', 'Ь', 'Ф', 'Ъ', 'Ф', 'М', 'У',
#     'Д', 'З', 'Д', 'А', 'Л', 'Й', 'Ё', 'Л', 'Б', 'М', 'Р', 'И', 'П', 'Ё', 'Л', 'А', 'Й', 'М', 'С', 'С',
#     'Л', 'Х', 'Ю', 'К', 'Я', 'Р', 'Щ', 'Й', 'О', 'Б', 'В', 'Ж', 'Ь', 'Э', 'Б', 'Р', 'Ю', 'Й', 'У', 'Ш',
#     'Ы', 'Э', 'Т', 'О', 'О', 'Э', 'В', 'О', 'К', 'Ф', 'Ё', 'Э', 'Э', 'Е', 'Щ', 'Ш', 'Щ', 'И', 'Ё', 'И',
#     'Ч', 'Я', 'С', 'В', 'Ы', 'О', 'Э', 'Т', 'С', 'Е', 'Ф', 'И', 'Н', 'А', 'М', 'Г', 'И', 'Ы', 'Ч', 'Э',
#     'Ю', 'М', 'Ш', 'Ь', 'Т', 'Я', 'Э', 'Т', 'Б', 'А', 'Р', 'Щ', 'И', 'Н', 'А', 'Ц', 'Н', 'Ч', 'Щ', 'Ъ',
#     'Д', 'Ь', 'Ь', 'Ц', 'Щ', 'Ч', 'Л', 'Р', 'Х', 'С', 'П', 'У', 'Ж', 'Я', 'Ю', 'Л', 'М', 'Ф', 'О', 'Ë',
#     'О', 'Ы', 'И', 'Ж', 'Ь', 'Л', 'Е', 'Т', 'И', 'Д', 'О', 'Б', 'О', 'В', 'С', 'О', 'Ф', 'Ъ', 'Ж', 'О'
# ]
#
#
# def normalize_char(char):
#     """Заменяет английские/греческие буквы и цифры на русские."""
#     mapping = {
#         'A': 'А', 'a': 'а', 'B': 'В', 'E': 'Е', 'e': 'е', 'K': 'К', 'k': 'к',
#         'M': 'М', 'H': 'Н', 'O': 'О', 'o': 'о', 'P': 'Р', 'p': 'р', 'C': 'С',
#         'c': 'с', 'T': 'Т', 'y': 'у', 'X': 'Х', 'x': 'х', '3': 'З',
#         'Π': 'П', 'Τ': 'Т', 'Ο': 'О', 'Κ': 'К', 'Ε': 'Е', 'Α': 'А',
#         'Γ': 'Г', 'Μ': 'М', 'Ë': 'Ё'
#     }
#     return mapping.get(char, char)
#
#
# # 1. Чистим данные
# cleaned_data = [normalize_char(c) for c in raw_data]
#
# # 2. Собираем матрицу 20x20
# matrix_size = 20
# if len(cleaned_data) != 400:
#     print(f"ВНИМАНИЕ: В данных {len(cleaned_data)} букв, а должно быть 400 (20x20). Результат может быть неточным.")
#
# matrix = [cleaned_data[i:i + matrix_size] for i in range(0, len(cleaned_data), matrix_size)]
#
#
# # 3. Функция поиска
# def solve_word_search(matrix):
#     rows = len(matrix)
#     cols = len(matrix[0]) if rows > 0 else 0
#     found_words = set()
#
#     directions = [
#         (0, 1), (0, -1), (1, 0), (-1, 0),
#         (1, 1), (1, -1), (-1, 1), (-1, -1)
#     ]
#
#     print("Начинаю поиск слов...")
#
#     for r in range(rows):
#         for c in range(cols):
#             for dr, dc in directions:
#                 current_word = ""
#                 curr_r, curr_c = r, c
#
#                 while 0 <= curr_r < rows and 0 <= curr_c < cols:
#                     current_word += matrix[curr_r][curr_c]
#
#                     if len(current_word) >= 3:
#                         # Проверка в словаре
#                         if morph.word_is_known(current_word):
#                             p = morph.parse(current_word)[0]
#                             # Фильтр: только существительные, с хорошей вероятностью
#                             # score > 0.5 отсекает совсем редкий бред
#                             if 'NOUN' in p.tag and p.score >= 0.4:
#                                 found_words.add(current_word)
#
#                     curr_r += dr
#                     curr_c += dc
#
#     return sorted(list(found_words))
#
#
# # 4. Запуск и вывод
# results = solve_word_search(matrix)
#
# print(f"\nНайдено уникальных слов: {len(results)}")
# print("-" * 40)
# # Выводим красивые колонки
# for i, word in enumerate(results):
#     print(f"{word:<15}", end="")
#     if (i + 1) % 4 == 0:  # по 4 слова в строку
#         print()
# print("\n" + "-" * 40)


# stroka = 'Into each life some rain must fall, but too much is falling in mine.'
# stroka = stroka.split()
# new_stroka = ''
# for i in range(0, len(stroka)):
#     if i % 2 == 0:
#         new_stroka += stroka[i].upper() + ' '
#     else:
#         new_stroka += stroka[i].lower() + ' '
# print(new_stroka)
from fractions import Fraction













def new_arr(arr1, list1):
    result_array = np.append(arr1, list1)
    return (result_array.dtype, len(result_array))








