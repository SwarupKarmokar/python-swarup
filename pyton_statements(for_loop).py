# lets see how for loop works on python:
# python is very flexible, we can iterate item from list, string, tuple and dictioonary.

# using list:
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list1 = list(range(1, 11))

# using for loop
for item in list1:
    print(item)  # its print every item from the list with a new line
# we can print anything we want to print
# like
for item in list1:
    print('*')

# try
for item in list1:
    if item % 2 == 0:
        print(f'{item} is an even number')
    else:
        print(f'{item} is an odd number')

# sum of the list item:
item_sum = 0
for item in list1:
    item_sum = item_sum + item
    # print(item_sum)  # it print the sum value for each loop
print(f'the sum of the list item is {item_sum}')

# using string:
string1 = 'hello world'
for item in string1:
    print(item)


# using tuple:
tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# tuple1 = tuple(range(1, 11)) # it does same work
for item in tuple1:
    print(item)

# we create dictionay with tuple and iterate the value:
list2 = [(1, 2), (3, 4), (5, 6)]
for item in list2:
    print(item)

# now iterate the value from tuple:
# tuple unpacking:
for a, b in list2:
    print(a)
    print(b)

# using dictionary:
dict1 = {'k1': 'value1', 'k2': 'value2', 'k3': 'value3'}
for item in dict1:
    print(item)  # it print the key

# like tuple we can unpack the value from dictionary:
# dictionay unpacking:
for key, value in dict1.items():
    print(key)
    print(value)