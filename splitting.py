# Array Ayırma (splitting)

import numpy as np

a = np.array([1,2,3,99,99,3,2,1])
print(a)
print(np.split(a, [3,5]))
a,b,c = np.split(a,[3,5])
print(a)
print(b)
print(c)

# iki boyutlu

m = np.arange(16).reshape(4,4)
print(m)

ust, alt = np.vsplit(m, [2])
print(ust)
print(alt)

sol, sag = np.hsplit(m,[2])
print(sol)
print(sag)


