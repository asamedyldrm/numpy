# Siralama (sorting)

import numpy as np

a = np.array([2, 5, 3, 4, 1])

print(a)
print(np.sort(a)) #veri setinin orijinal yapısını bozmaz.
print(a)
a.sort() #veri setinin orijinal yapısını bozuyor. print(a) dedigimizde bunu fark ediyoruz.
print(a)

# iki boyutlu array siralama

b = np.random.normal(20,5,(3,3))
print(b)
print(np.sort(b, axis= 1))
print(np.sort(b, axis= 0))