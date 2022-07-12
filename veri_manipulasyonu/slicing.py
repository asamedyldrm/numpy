# Slicing ile Elemanlara Erismek (Array alt kumesine erismek)

import numpy as np

a = np.arange(20,30)
print(a)
print(a[0:3])
print(a[:3])
print(a[3:])
print(a[1::2])

# iki boyutlu slice islemleri

m = np.random.randint(10, size=(5,5))
print(m)
print(m[:,1]) #sutuna erismek icin
print(m[0,:])
print(m[0])
print(m[0:2,:3])
print(m[:,:2])
print("---------")
print(m)
print(m[2:4,1:3])