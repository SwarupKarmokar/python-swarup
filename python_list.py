# list can contain multiple data type on its:
# check the len and type of the list
my_list = [1, 2, 3, 4]
# or
my_list1 = [1, 2, 'string', 0.004]

# indexing and slicing of list=>
# check various index position:
my_list2 = [1, 2, 3, 4, 5, 6]
# like
print(my_list2[0])

# slicing:
my_list3 = [1, 2, 3, 5, 6, 7, 8, 9]
print(my_list3[:])
print(my_list3[1:3])
print(my_list3[:-1])
print(my_list3[::2])

# list operations=>
my_list4 = ['swarup', 1, 2, 3, 'how are you']
# reassign list:
my_list5 = my_list4 + ['hello']
print(my_list5)
# make double list:
print(my_list5*2)

# mutablity checking:
my_list6 = ['swarup', 1, 2, 3, 'how are you']
my_list6[0] = 'iam'
print(my_list6) # list was mutable

# try:
my_list6[0][0] = 'S'
print(my_list6)



# list methods=>

my_list7 = ['swarup', 1, 2, 3, 'how are you']
my_list7.append('appended item')  # append method is not permanent

my_list7.pop()  # by default pop method pop off and item from last index
# we can pop off item from index position
my_list7.pop(2)
# if we want to show the poped item
poped_item = my_list7.pop(2)

my_list8 = [4, 2, 3, 7, 9, 1, 8, 5, 6]
print(my_list8.reverse())

print(my_list8.sort())

# Nesting list=>
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

my_matrix = [list1, list2, list3]
print(my_matrix)
# try
print(my_matrix[0])
# if we want to grab the element from specific list
print(my_matrix[1][0])

# list comprehension (the construction of list)
first_columns = [row[0] for row in my_matrix]
print(first_columns)