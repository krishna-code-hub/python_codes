import sys

# Get list of command-line arguments (excluding script name)
print(sys.argv)
arguments = sys.argv[1:]

if len(arguments) < 2:
    print("Error: Please provide at least two arguments.")
    print("Usage: script_name.py <argument1> <argument2> [optional arguments]")
    exit()

# Access and process arguments
first_argument = arguments[0]
second_argument = arguments[1]

# Example usage (modify as needed based on your specific requirements)
print(f"The first argument is: {first_argument}")
print(f"The second argument is: {second_argument}")

# You can process any number of arguments using a loop or list comprehension
for arg in arguments:
    print(f"Argument: {arg}")
