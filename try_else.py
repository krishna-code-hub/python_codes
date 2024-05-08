#
# def func(x):
#     try:
#         x = x / x
#     except:
#         print('a', end='')
#     else:
#         print('b', end='')
#     finally:
#         print('c', end='')
#
#
# func(1)
# func(0)
#
# for i in range(1, 6):
#     print(i, i, i, i, i)
#
# print(str('-') * 5)
# for i in range(1, 6):
#     print(i, i, i, i, i,sep='')
#
# print(str('-') * 5)
# for i in range(1, 6):
#     print(str(i) * 5)
#
# print(str('-') * 5)
# for i in range(1, 5):
#     print(str(i) * 5)
#
# print(str('-') * 5)
# for i in range(0, 5):
#     print(str(i) * 5)
#
#
# print(3 / 5)
#
# print(5 * 4 // 3)

# with open('file', 'w') as f:
#     for i in range(1, 6):
#         f.write(str(i) + '. Line\n')
#
# for x in open('file', 'rt'):
#     print(x)


nums = [3, 4, 5, 20, 5, 25, 1, 3]
nums.pop(2)
print(nums)  # [3, 5, 20, 5, 25, 1, 3]


print(list('hello'))