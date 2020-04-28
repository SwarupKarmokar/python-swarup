# list comprehensions: its allow us to build out lists using a different notation.
# grab every letter from string into list:
my_list = [item for item in 'hello world']
print(my_list)

# square the value of range operator:
my_list1 = [item ** 2 for item in range(9)]
print(my_list1)

# make list of even number from range operator:
my_list2 = [item for item in range(10) if item % 2 == 0]
print(my_list2)

# complicated arithmetic:
celsius = [0, 25, 50, 100]
fahrenheit = [(9/5 * temp_celsius + 32) for temp_celsius in celsius]
print(fahrenheit)

# nested list comprehension:
my_list3 = [item ** 2 for item in [item ** 2 for item in range(9)]]
print(my_list3)
# try
my_list4 = [item for item in my_list3 if item % 2 == 0]
print(my_list4)