def func(p1, p2):
    p1 = 1
    p2[0] = 42


x = 3
y = [1, 2, 3]

func(x, y)

print(x, y[0])  # 3 42

### Mutable List while passing as argument
m = list([1, 2, 3])
n = m

print(id(m) == id(n))

print(m.pop(1))

print(id(m) == id(n))

print(n)