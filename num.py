from numpy import array
x=array(sum(range(100)))
print ("сумма ряда 1-100 =", x)

from numpy import array
print('Введите целое число')
y=int(input())
x=array(sum(range(y)))
print("Сумма ряда 1-",y, 'равна', x)

import numpy as np
x=np.random.randint(1000, size=100)
print(x)
print("Среднее среди 100 случайных чисел:", np.mean(x))
