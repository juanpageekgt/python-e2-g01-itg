# obtener la fecha local

# ej.1
from datetime import date

today = date.today()

print('Hoy:', today)
print('Año:', today.year)
print('Mes:', today.month)
print('Día:', today.day)

print()

print('Ej.2')

my_date = date(2019, 11, 4)
print(my_date)

print()

print('Ej.3')

import time

timestap = time.time()
print('Marca de tiempo:', timestap)

d = date.fromtimestamp(timestap)
print('Fecha:', d)

print()

print('Ej.4')

d = date.fromisoformat('2025-05-02')
print(d)

print()

print('Ej.5')

d = date(2025, 5, 2)
print(d)

print()

d = d.replace(year=2026, month=3, day=16)
print(d)

print()

print('Ej.6')

d = date(2025, 5, 2)
print(d.weekday() + 1)

print()