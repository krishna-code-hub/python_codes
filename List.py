

num_list = [1,2,3,4,5,2,2]

for i in range(len(num_list) - 1, -1, -1):
    print(i)

num_list.remove(2)
print(num_list)

num_list.pop(2)
print(num_list)


print(list(reversed(range(1,11))))