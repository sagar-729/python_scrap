# creating infrastructure for our new branch project

# Rules for a list
list_squares = [x**2 for x in range(10)]

print(list_squares)

list_cubes = [x**3 for x in range(10)]

print(list_cubes)

# conditional
list_squares = [x**2 for x in range(10) if x % 2 == 0]                                                                  # Condition in the result of the rule
print("Even Squares only - " + str(list_squares))

list_cubes = [x**3 for x in range(10) if x % 2 == 0]                                                                    # IF condition in the result of rule.
print("Even Cubes only - " + str(list_cubes))