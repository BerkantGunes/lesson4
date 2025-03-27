
# Yontem 1
import math as islem

value = islem.factorial(5) # math yerine islem degiskeniyle tanimladigimiz icin islem ile math fnks erisebiliriz!

#value = dir(math)
#value = help(math) #terminal de CRTL+C yaparak calistirilan programdan cikabiliriz!!!!
#value = math.sqrt(196)
#value = math.factorial(7)
#value = math.floor(5.7) # asagi dogru yuvarlama yapar.
#value = math.ceil(5.7) # yukari dogru yuvarlar.


# Yontem 2 
from math import * # math kutuphanesinin butun fonksiyonlarini import ettik!

def sqrt(x):
    print('x: ' + str(x))

from math import sqrt

#value = factorial(7) # math.factorial yazmaya gerek kalmadi cunku butun fonksiyonlari direk kullanabiliriz artik!
value = sqrt(81)

print(value)