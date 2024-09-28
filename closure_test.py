#
#
# def outer_fn():
#     x = 0
#     def increment():
#         nonlocal x
#         x = x + 1
#         return x
#
#     return increment
#
# counter = outer_fn()
# print(counter())
# print(counter())

# adder =[]
# for n in range(1,4):
#     adder.append(lambda x: x + n)
#
#
# print(adder[0](10))
# print(adder[1](10))
# print(adder[2](10))


##############################3

# class average:
#     def __init__(self):
#         self.numbers = []
#
#     def add(self,number):
#         self.numbers.append(number)
#         total = sum(self.numbers)
#         cnt = len(self.numbers)
#         return total/cnt
#
#
# a = average()
# print(a.add(10))
# print(a.add(20))

##############################

def average():
    numbers = []
    def add(number):
        numbers.append(number)
        total = sum(numbers)
        cnt = len(numbers)
        return total/cnt

    return add



a = average()
print(a(10))
print(a(20))
