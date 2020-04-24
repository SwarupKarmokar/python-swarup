# python dictionary is very flexible, its holds multiple datatype
my_dict = {'k1': 'value1', 'k2': 'value2', 'k3': 123, 'k4': 0.000456, 'k5' :[1, 2, 3, 4, 5], 'k6': {'k7': 1234, 'k8': 0.09}, 'k9': (1, 2, 3, 4)}
print(my_dict)  # dictionary is the form of key value pair

# dictionary basic operation=>
# try
#print(my_dict[0])  # its shows an error because dictionary can't support indexing

# calling key value:
print(my_dict['k5'])
# now we can indexing the key value
print(my_dict['k5'][3])

# we apply methods on that key values
print(my_dict['k1'].upper())

# method to get all key values
print(my_dict.keys())
# method to get all values
print(my_dict.values())
# method to get all key and value's tuple
print(my_dict.items())

# nesting dictionary
print(my_dict['k6'])  # its holds a dictionary on it

# we can get values from nested dictionary
print(my_dict['k6']['k7'])

# optional operation
# we can doing some stuff with dictionary
print(my_dict['k3'] + 4) # we can also do subtraction/division/multiplication etc.

# creating a new dictionary
dictionary = {}
dictionary['name'] = 'swarup'
dictionary['age'] = 20
print(dictionary)