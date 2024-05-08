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