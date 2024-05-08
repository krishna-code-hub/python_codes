

# Suppose we could create a mutable set element
mutable_element = ['lemon']
fruits = set()
fruits.add(tuple(mutable_element))  # Tuples are immutable, so we use a tuple of a list

# Now if we try to change the list
mutable_element.append('lime')
print(fruits)  # This would cause confusion in set behavior if it were allowed

# Python will output the set with the tuple, but you cannot change the tuple's content directly
