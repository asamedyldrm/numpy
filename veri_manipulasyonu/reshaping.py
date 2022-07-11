# Yeniden Sekillendirme (reshaping)

import numpy as np

print(np.arange(1,10))
print(np.arange(1,10).reshape(3,3))

a = np.arange(1,10)
print(a)
print(a.ndim)

b = a.reshape(3,3)
print(b)
print(b.ndim)