# import pyowm

# owm = pyowm.OWM('747e0b601ab68259ae79fec77ba09f68')  # You MUST provide a valid API key

# # Have a pro subscription? Then use:
# # owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

# # Search for current weather in London (Great Britain)
# place = input("Please input city name: ")
# observation = owm.weather_at_place(place)
# w = observation.get_weather()
# print(w)                      # <Weather - reference time=2013-12-18 09:20,
#                               # status=Clouds>

# # Weather details
# w.get_wind()                  # {'speed': 4.6, 'deg': 330}
# w.get_humidity()              # 87
# w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
# print("Wind:", w.get_wind()['speed'])
# print("Himidility", w.get_humidity())
# print("Temperature", w.get_temperature('celsius')['temp'])

# # Search current weather observations in the surroundings of
# # lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
# observation_list = owm.weather_around_coords(-22.57, -43.12)


###################################################

# Task 2
# 1.  Напишіть скрипт-гру, яка генерує випадковим чином число з діапазону 
# чисел від 1 до 100 і пропонує користувачу вгадати це число. 
# Програма зчитує числа, які вводить користувач і видає користувачу 
# підказки про те чи загадане число більше чи менше за введене користувачем. 
# Гра має тривати до моменту поки користувач не введе число, яке загадане програмою, 
# тоді друкує повідомлення привітання. 
# (для виконання завдання необхідно імпортувати  модуль random, а з нього функцію randint())
import random

x = random.randint(1,100)
user_number = int(input('input some numbers:'))
print (x)
while x!=user_number:
  if x < user_number: 
    user_number = int(input("input lower number"))
  elif x > user_number: 
    user_number = int(input("Input higher number"))
    
  
    
print("You are the best!!")
    
    
    





# 2.  Напишіть скрипт, який обчислює площу прямокутника a*b, площу трикутника 0.5*h*a, площу кола pi*r**2. 
# (для виконання завдання необхідно імпортувати  модуль math, а з нього функцію pow() та значення змінної пі).