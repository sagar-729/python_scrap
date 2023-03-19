# creating infrastructure for our new branch project
# creating infrastructure for our new branch project

numbers = {
    1 : "One",
    2 : "Two",
    3 : "Three",
    4 : "Four"
}

print(numbers.get(5, "Key Not Found"))                                                                                                       # Perfectly Fine.

people = {
    "John" : 21,
    "Shyam" : 8,
    "Ram" : 27
}

name = "Ramu"

print("Age of " + name + " is "+  str(people.get(name, "Not Found.")))                                                  # Applause - We are not getting any KeyERROR .
