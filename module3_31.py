a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
p = (a + b + c) / 2
import math

s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(s)
