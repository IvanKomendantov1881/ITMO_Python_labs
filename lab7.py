import requests
from PIL import Image, ImageTk
from io import BytesIO
import tkinter as tk

# Task 1
# city_name = input()
# api_key = '308fb024a098f9a4b343465f8f191427'
#
# url= f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&APPID={api_key}&units=metric&lang=ru'
#
# try:
#     res = requests.get(url)
#     res.raise_for_status()
#     data = res.json()
#     # print(data)
#     temperature = data["main"]["temp"]
#     feels_like = data["main"]["feels_like"]
#     humidity = data["main"]["humidity"]
#     pressure = data['main']['pressure']
#
#     print(f"\nПогода в городе {city_name}:")
#     print(f"Температура: {temperature}°C")
#     print(f"Ощущается как: {feels_like}°C")
#     print(f"Влажность: {humidity}%")
#     print(f'Давление: {pressure}гПа')
#
# except:
#     print("Город не найден или ошибка запроса.")
#

# Task 2

# def information():
#     holiday_name = input('Какой праздник вас интересует на английском:')
#     holiday_name = holiday_name.replace(' ', '%20')
#     country = input('Ваша страна на английском:')
#     year = input('Год до 2025 включительно:')
#     url = f'https://holidayapi.com/v1/holidays?key={api_key}&country={country}&year={year}&name={holiday_name}&pretty'
#     try:
#         res = requests.get(url)
#         res.raise_for_status()
#         data = res.json()
#         print('Вывод:')
#         print(data["holidays"][0]["name"])
#         print(data["holidays"][0]["date"])
#
#     except:
#         print('Праздник не найден или ошибка запроса')
#
# def day_information():
#     country = input('Ваша страна на английском:')
#     year = input('Год до 2025 включительно:')
#     month = input('Номер месяца:')
#     day = input('Номер дня в месяце:')
#     url = requests.get(f"https://holidayapi.com/v1/holidays?key={api_key}&country={country}&year={year}&month={month}&day={day}")
#     data = url.json()
#     if data["holidays"]:
#         print("Есть праздник:", data["holidays"][0]["name"])
#     else:
#         print("Праздников нет")
#
# def holidays_in_month():
#     country = input('Ваша страна на английском:')
#     year = input('Год до 2025 включительно:')
#     month = input('Номер месяца:')
#     res = requests.get(f"https://holidayapi.com/v1/holidays?key={api_key}&country={country}&year={year}&month={month}")
#     data = res.json()
#     # print(data)
#     try:
#         for i in data["holidays"]:
#             print(i["name"])
#     except:
#         print('Праздник не найден или ошибка запроса')
#
# def holidays_in_year():
#     country = input('Ваша страна на английском:')
#     year = input('Год до 2025 включительно:')
#     res = requests.get(f"https://holidayapi.com/v1/holidays?key={api_key}&country={country}&year={year}")
#     try:
#         for i in res.json()["holidays"]:
#             print(i["name"], "-", i["date"])
#     except:
#         print('Праздник не найден или ошибка запроса')
#
#
# api_key = '1fe201da-626b-484d-b43c-00c2e8ff86e0'
# a = input('Выберете один из вариантов: \n информация о празднике - 1, \n есть ли в этот день праздник - 2, \n праздники за месяц - 3, \n праздники за год - 4')
# if a == '1':
#     information()
# elif a == '2':
#     day_information()
# elif a == '3':
#     holidays_in_month()
# elif a == '4':
#     holidays_in_year()


# Task 3
root = tk.Tk()
root.title('Генератор котиков')


def load_image():
    url = "https://cataas.com/cat?width=400&height=400"
    res = requests.get(url)
    img = Image.open(BytesIO(res.content))
    photo = ImageTk.PhotoImage(img)
    label.config(image=photo)
    label.image = photo

label = tk.Label(root)
label.pack()
btn = tk.Button(root, text="Следующий кот", command=load_image)
btn.pack(pady=10)
load_image()
root.mainloop()



