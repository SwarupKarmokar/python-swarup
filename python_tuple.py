# tuple also holds multiple datatype into it
my_tuple = (1, 'string', [1, 2, 3, 4], {'k1':123, 'k2':'iam'})
print(my_tuple)

# indexing and slicing=>
print(my_tuple[2])
print(my_tuple[:])
print(my_tuple[0:-1])
print(my_tuple[::2])
print(my_tuple[::-1])

# we can find index position values
print(my_tuple[3]['k1'])
print(my_tuple[2][3])

# mutable checkup
my_tuple[0] = 'String'
print(my_tuple)  # its shows an error
