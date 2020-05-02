# map function: map function allows us to 'map' a iterable object so we can quickly call the same function for every iterable object
# def squre_num(num):
#     return num ** 2

# my_num = [1, 2, 3, 4]

# ans = squre_num(my_num)
# print(ans)  # it shows an error unsupported operand types

# for this problem we using map function
def squre_num(num):
    return num ** 2

my_num = [1, 2, 3, 4]

ans = map(squre_num, my_num)
print(ans)   # it shows memory location of the function
# to get the result we need to cast with list
ans1 = list(map(squre_num, my_num))
print(ans1)

# filter function: filter function same as map function but its allows us to return an item which fuction item is true

# using map function:

# def check_even(num):
#     return num % 2 == 0
#
# my_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# ans = list(map(check_even, my_num))
# print(ans)
# return the boolean value.

# using filter function:
def check_even(num):
    return num % 2 == 0

my_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

ans = list(filter(check_even, my_num))
print(ans)