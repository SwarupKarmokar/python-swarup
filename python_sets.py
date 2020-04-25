# sets are an unordered collection of unique values
# create an empty set
my_set = set()
my_set.add(1)
print(my_set)  # output is not a dictionary
# my_set.add(2, 4, 5, 6) # it shows an error(because add argument take one argument
# print(my_set)

# create a list
my_list = [1, 2, 3, 4, 5]

# we create a set using casting method
my_set1 = set(my_list)   # using cast type casting we change variable values
print(my_set1)

# finding unique values=>
# using set we can find unique values from unorder sequence
my_list1 = [1, 2, 3, 4, 4, 5, 3, 2, 1, 6, 6, 6, 5, 5]
my_set2 = set(my_list1)
print(my_set2)