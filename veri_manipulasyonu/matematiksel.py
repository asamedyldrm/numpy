# Matematiksel Islemler

import numpy as np

a = np.array([1, 2, 3, 4, 5])
print(a-1)
print(a+1)
print(a/5)
print(a*4)
print(a**3)
print(a%2)

print("-----ufunc-----")

print(np.subtract(a,1))
print(np.add(a,1))
print(np.multiply(a,4))
print(np.divide(a,5))
print(np.power(a,3))
print(np.mod(a,2))

print(np.absolute(np.array([-5]))) #MUTLAK DEGER
print(np.sin(360))
print(np.cos(60))

l = np.array([1,2,3,10])
print(np.log(l))
print(np.log2(l))
print(np.log10(l))