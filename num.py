from numpy import array
x=array(sum(range(100)))
print ("сумма ряда 1-100 =", x)

from numpy import array
y=int(input())
x=array(sum(range(y)))
print("сумма ряда 1-input()", x)

import numpy as np
x=np.random.randint(10000, size=100)
print(x)
print("среднее среди 100 случайных чисел:", np.mean(x))
