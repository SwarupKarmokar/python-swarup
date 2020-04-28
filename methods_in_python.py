# method: methods are essentially function built into objects.
# in pycharm ide we can see possible method after pressing . key
# we take list here:
my_list = [1, 2, 3, 4, 5]

# append method:
my_list.append(6)
print(my_list)  # its add element at the end of the list

# pop method:
my_list.pop()
print(my_list)  # default it remove last item from list but we can also remove item by putting index position
print(my_list.pop(3))
print(my_list)

# remove method:
my_list.remove(5)
print(my_list)  # its remove the element we want

# count method:
my_list = [1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4]
print(my_list.count(4))
print(my_list.count(2))  # its count the number of occurrance

# reverse method:
print(my_list.reverse())  # its return none

# sort method:
my_list = [5, 4, 3, 2, 1]
my_list.sort()
print(my_list)

# extend method:
my_list.extend()
print(my_list)

# insert method:
my_list.insert(1, 3)  # it insert element into given index position
print(my_list)