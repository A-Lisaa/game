from math import e
from decimal import Decimal, getcontext

getcontext().prec = 100000
res = 0
for i in range(1000):
    fact = Decimal(1)
    for i in range(2, i):
        fact *= Decimal(i)
    res += Decimal(1)/fact
print(e)
print(res)