def outer_function(x):
    # First level of nesting
    x = 'outer1'
    def first_nested_function():
        # Second level of nesting
        x = 'inner1'
        def second_nested_function():
            nonlocal x
            x = 'inner2'
            print(f"inner2 - x value is {x}")  # Multiply the input by 2

        second_nested_function()
        print(f"inner1 - x value is {x}")
        # Increment y by 1, then pass to second_nested_function

      # Increment x by 2, then pass to first_nested_function
    first_nested_function()
    print("Result:", x)

# Example usage
outer_function(3)

