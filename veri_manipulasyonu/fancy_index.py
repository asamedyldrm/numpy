# Fancy Index ile Elemanlara Erismek
# Ileri duzey eleman secme imkanı vermektedir. Pandas'da da kullanılacaktır. ONEMLI!

import numpy as np

a = np.arange(0, 30, 3)
print(a)
print([a[1], a[3], a[5]])

# Fancy Index Etkisi

al_getir = [1, 3, 5]
print(a[al_getir])

# iki boyutta fancy

m = np.arange(9).reshape(3,3)
print(m)

satir = np.array([0,1])
sutun = np.array([1,2])
print(m[satir,sutun])

# basit index ile fancy index

print(m)
print(m[0,[1,2]])

# slice ile fancy index

print(m[0:,[1,2]])