# dando formato a la fecha y hora

from datetime import date
from datetime import datetime
from datetime import time


""" print('ej.1')

d = date(2020, 1, 4)
print(d.strftime('%Y/%m/%d'))

print()

print('Ej.2')

t = time(14, 53)
print(t.strftime("%H:%M:%S"))

dt = datetime(2020, 11, 4, 14, 53)
print(dt.strftime("%y/%B/%d %H:%M:%S"))

print() """

print('Ej.3')
import time

timestap = 1572879180
st = time.gmtime(timestap)

print(time.strftime("%Y/%m/%d %H:%M:%S", st))
print(time.strftime("%Y/%m/%d %H:%M:%S"))

print()

print('Ej.4')
from datetime import datetime

print(datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))

print()

print('Ej.5')

import time

print(time.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))

print()

print('Ej.6')

from datetime import date
from datetime import datetime

d1 = date(2020, 11, 4)
d2 = date(2019, 11, 4)

print(d1 - d2)

dt1 = datetime(2020, 11, 4, 0, 0 ,0)
dt2 = datetime(2019, 11, 4, 14, 53, 0)

print(dt1 - dt2)

print()

print('ej,7')

from datetime import timedelta

delta = timedelta(weeks=2, days=2, hours=3)
print(delta)

print()

print('Ej.8')

from datetime import timedelta

delta = timedelta(weeks=2, days=2, hours=3)
print('Días:', delta.days)
print('Segundos:', delta.seconds)
print('Microsegundos:', delta.microseconds)

print()


print('Ej.9')

from datetime import timedelta
from datetime import date
from datetime import datetime

delta = timedelta(weeks=2, days=2, hours=2)
print(delta)

print()

delta2 = delta * 2
print(delta2)

print()

d = date(2019, 10, 4) + delta2
print(d)

print()

dt = datetime(2019, 10, 4, 14, 53) + delta2
print(dt)