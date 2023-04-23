import os
os.system("cls")

### Dates ###

import datetime as datetimeModule
from datetime import time, date
from datetime import timedelta

### Declaración de funciones ###
def print_date(date):
    print(date)

now = datetimeModule.datetime.now()
print("Año:" , now.year)
print("Mes:" , now.month)
print("Día:" , now.day)
print("Hora:" , now.hour)
print("Minutos:" , now.minute)
print("Segundos:" , now.second)

timestamp = now.timestamp()
print("Timestamp:" , timestamp)

print("Convertir de vuelta timestamp" , datetimeModule.datetime.fromtimestamp(timestamp))

year_2023 = datetimeModule.datetime(2023, 1, 1)
year_2024 = datetimeModule.datetime(2024, 1, 1)

print_date(year_2023)

current_time = time()
print(current_time)

current_date = date.today()
print(current_date)

diff = year_2024 - year_2023
print(diff)

init_timedelta = timedelta(200, 100, 100, weeks = 10)
end_timedelta = timedelta(300, 100, 100, weeks = 13)

print(end_timedelta - init_timedelta)