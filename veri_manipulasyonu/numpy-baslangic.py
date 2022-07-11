import numpy as np

# Tek boyutlu olanlar VEKTOR, iki boyutlu olanlar ise MATRIS'dir.

a = np.array([1,2,3,4,5])
b = np.array([2,3,4,5,6])
print(a*b)

# Böyle kolay bir şekilde iki listeyi birbiriyle çarpabiliyoruz.

# Numpy Array'i olusturmak
a = np.array([1, 2, 3, 4, 5])
print(a)
print(type(a))

# Sıfırdan array olusturma

a = np.zeros(10, dtype="int")
print(a)

b = np.ones((3, 5), dtype="int")
print(b)

c = np.full((2, 10), 5)
print(c)

print(np.arange(0,31, 2))

d = np.linspace(0,1,10)
print(d.shape)

e = np.random.normal(10,4, (3,4)) #ortalama 10 standart sapma 4
print(e)

f = np.random.randint(0,10, (3,3))
print(f)

# Özellikleri
# ndim: boyut sayısı
# shape: boyut bilgisi
# size: toplam eleman sayısı
# dtype: array veri tipi

g = np.random.randint(25, size= 5)
print(g)
print(g.ndim)
print(g.shape)
print(g.size)
print(g.dtype)

h = np.random.randint(10, size= (3,5))
print(h)
print(h.ndim)
print(h.shape)
print(h.size)
print(h.dtype)

