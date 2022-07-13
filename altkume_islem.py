# Alt Kume Uzerinde Islem Yapmak

import numpy as np

a = np.random.randint(10, size=(5,5))
print(a)

# Alt kumeleri genel kumeden bagimsiz yapmak isteyebiliriz.

alt_a = a[0:3,0:2]
print(alt_a)

alt_a[0,0] = 9999
alt_a[1,1] = 8888

# Alt kumede yaptigimiz degisiklik ana kumede de meydana geldi.

print(alt_a)
print(a)

m = np.random.randint(10, size=(5,5))
print(m)

alt_m = m[0:3,0:2].copy()
print(alt_m)

alt_m[0,0] = 9999
alt_m[1,1] = 8888

print(alt_m)
print(m)