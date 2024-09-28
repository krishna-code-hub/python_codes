
from collections import defaultdict

animals = {
    'a': ['ant', 'antelope', 'armadillo'],
    'b': ['beetle', 'bear', 'bat'],
    'c': ['cat', 'cougar', 'camel']
}


def empty():
    return "Key not available"


animals = defaultdict(empty, animals)

print(animals['b'])
print(animals['d'])

print("    programming    ".center(20,'#'))

print(0xA + 0xB + 0xC)

for i in range(5):
    print(i)
else:
    print("Done!")