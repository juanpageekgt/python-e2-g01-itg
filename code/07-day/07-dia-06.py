# el módulo time
import time

print('Ej.1')

class Student:
    def take_nap(self, seconds):
        print('Estoy muy cansado. Tengo que tomar una siesta. Hasta luego.')
        time.sleep(seconds)
        print('!Dormí bien!, !Me siento genial!')


student = Student()
student.take_nap(1)

print()

print('Ej.2')

timestap = 1572879180
print(time.ctime(timestap))

print()

print('Ej.3')

print(time.ctime())

print()

print('Ej.4')

''' time.struct_time:
    tm_year   # Especifica el año.
    tm_mon    # Especifica el mes (valor de 1 a 12)
    tm_mday   # Especifica el día del mes (value from 1 to 31)
    tm_hour   # Especifica la hora (valor de 0 a 23)
    tm_min    # Especifica el minuto (valor de 0 a 59)
    tm_sec    # Especifica el segundo (valor de 0 a 61)
    tm_wday    # Especifica el día de la semana (valor de 0 a 6)
    tm_yday   # Especifica el día del año (valor de 1 a 366)
    tm_isdst  # Especifica si se aplica el horario de verano (1: sí, 0: no, -1: no se sabe)
    tm_zone   # Especifica el nombre de la zona horaria (valor en forma abreviada)
    tm_gmtoff # Especifica el desplazamiento al este del UTC (valor en segundos)
 '''

print()

print('Ej.5')

timestap = 1572879180
print(time.gmtime(timestap))
print()
print(time.localtime(timestap))

print()

print('6b')

timestap = 1572879180
st = time.gmtime(timestap)

print(time.asctime(st))
print('-')
print(time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0)))

print()

""" sugnificado de la tupla enviada 
2019 => tm_year
11 => tm_mon
4 => tm_mday
14 => tm_hour
53 => tm_min
0 => tm_sec
0 => tm_wday
308 => tm_yday
0 => tm_isdst
"""

print('Ej.7')
from datetime import datetime

print('hoy:', datetime.today())
print('ahora:', datetime.now())
#print('utc_ahora', datetime.utcnow())

print()

print('ej.8')

dt = datetime(2020, 10, 4, 14, 55)
print("Timestap:", dt.timestamp())