import numpy as np


a = np.zeros([3,4])
b = a.copy()
print(np.array_equal(a,b))

print(a)

c = np.empty([3,4])
d = np.empty([3,4])
print(c)
print(np.array_equal(c,d))

e = np.zeros([3,4])
f = np.zeros([4,3])
print(e)
print(np.array_equal(e,f))


