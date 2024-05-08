# Precedence of or & and
# meal = "fruit"
# money = 0
# if meal == "fruit" or meal == "sandwich" and money >= 2:
#     print("Lunch being delivered")
# else:
#     print("Can't deliver lunch")


# print("Regular division")
# print(2 / 2, "\tis a float.")
#
# print("\nFloor division")
# print(15 // 4, "\tis an int.")
# print(15.0 // 4, "\tis a float.")

#unpacking a list
# List=[1,2,3,4]
# print(*List)

try:
    even_numbers = [2, 4, 6, 8]
    print(even_numbers[5])

except ZeroDivisionError:
    print("Denominator cannot be 0.")

except IndexError:
    print("Index Out of Bound.")

except:
    print("Index Out of Bound.")

# Output: Index Out of Bound