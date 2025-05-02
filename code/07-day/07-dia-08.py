# módulo calendar

import calendar

print('ej.1')

print(calendar.calendar(2025))

print()

print('Ej.2')

calendar.prcal(2026)

print()

print('Ej.3')

print(calendar.month(2025, 5))

print()

print('Ej.4')

calendar.setfirstweekday(calendar.SUNDAY)
calendar.prmonth(2025, 5)

print()

print('Ej.5')

print(calendar.weekday(2025, 5, 2))

print()

print('Ej.6')

print(calendar.weekheader(2))

print()

print('Ej.7')

print(calendar.isleap(2025))
print(calendar.leapdays(2025, 2031))

print()

print('Ej.8')

c = calendar.Calendar(calendar.SUNDAY)

for weekday in c.iterweekdays():
    print(weekday, end=" ")

print()

print('Ej.9')

c = calendar.Calendar()

for iter in c.itermonthdays(2019, 11):
    print(iter, end=" ")

print()

print('10')

c = calendar.Calendar()

for iter in c.itermonthdays(2019, 11):
    print(iter, end=" ")

print()

print('ej.11')

c = calendar.Calendar()

for data in c.monthdays2calendar(2025, 5):
    print(data)