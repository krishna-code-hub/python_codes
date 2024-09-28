

# List of strings
strings = ["apple", "banana", "cherry", "kiwi"]

# Sort strings by length
sorted_strings = sorted(strings, key=lambda x: len(x))

print(sorted_strings)  # Output: ['kiwi', 'apple', 'banana', 'cherry']

################################


people = [
    {"name": "John", "age": 17},
    {"name": "Jane", "age": 22},
    {"name": "Dave", "age": 15},
    {"name": "Emily", "age": 29}
]

#Using lambda function
print([i for i in filter( lambda person: person['age'] > 18, people)])

#Using list comprehension
print([person for person in people if person['age'] > 18])

# Filter out people under 18 and create a greeting message
adult_greetings = list(map(
    lambda person: f"Hello, {person['name']}! Welcome.",
    filter(lambda person: person['age'] >= 18, people)
))

print(adult_greetings)
# Output: ['Hello, Jane! Welcome.', 'Hello, Emily! Welcome.']


def count_recursive(n=1):
    if n > 3:
        return
    print(n)



    count_recursive(n + 1)


count_recursive()