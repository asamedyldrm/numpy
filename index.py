import numpy as np

a = np.random.randint(10, size = 10)
print(a)

print(a[0])
print(a[-1])
a[0] = 100
print(a)

b = np.random.randint(10, size=(3,5))
print(b)

print(b[0,0])
print(b[1,1]) #[satır,sutun]
b[1,3] = 95
print(b)
b[1,4] = 15.2

# Görüldüğü gibi int seklinde ekleme yapiyor.
# Zaten olusturulmus bir arraye ekleme yaparken array'e gore hareket eder.
# Array'i olustururken yazsaydık o zaman hepsini float'a cevirecekti.
print(b)