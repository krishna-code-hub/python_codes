class MyClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"MyClass instance with value: {self.value}"

# Create an object of MyClass
obj = MyClass(42)

# Now, when you print the object or convert it to a string, it will use the __str__() method:
print(obj)  # Output: MyClass instance with value: 42

# Using string formatting
formatted_str = f"The object is: {obj}"
print(formatted_str)  # Output: The object is: MyClass instance with value: 42

x = [[[1, 2], [8, 4]], [[5, 6], [7, 8]]]


def func(data):
    res = data[0][0]
    for da in data:
        for d in da:
            if res < d:
                res = d
    return res


print(func(x[1]))


s = "hello"
try:
    s[1] = 'a'
except TypeError as e:
    print(e)


characters = ["Iron Man", "Spider Man", "Captain America"]
actors = ["Downey", "Holland", "Evans"]

#example output : [("IronMan", "Downey"), ("Spider Man", "Holland"), ("Captain America", "Evans")]

# print(list(zip(characters,actors)))
#
# print(type({lambda x : x*x for x in range(1,100)}))
#
# print({ x : x*x for x in range(1,100)})
#
# sq = lambda x : x*x
#
# print({sq(x) for x in range(1,100)})
#
# result = [1, 2, 3] * 3
# print(result)  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]
# print(id(result))
# result[0]=100
# print(result)


print((256).bit_length())
#print((256).bit_count())
print("foo" if (256).bit_length() > 8 else "bar")

import numpy as np

a = np.arange(100)
b = a[50:60:2]

print(type(a),type(b))