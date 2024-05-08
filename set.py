

# Define two sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Using the intersection method
intersection_result_method = set_a.intersection(set_b)
print("Intersection (Method):", intersection_result_method)  # Output: {4, 5}

# Using the intersection operator
intersection_result_operator = set_a & set_b
print("Intersection (Operator):", intersection_result_operator)  # Output: {4, 5}

# Using the union method
union_result_method = set_a.union(set_b)
print("Union (Method):", union_result_method)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Using the union operator
union_result_operator = set_a | set_b
print("Union (Operator):", union_result_operator)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}


set_cp = {x for x in range(100) if x%3 == 0}

list_cp = [x for x in range(100) if x%3 == 0]

print(type(set_cp),type(list_cp))