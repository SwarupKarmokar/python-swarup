# python have few built_in operator:

# range: range function allows us to quickly genarate a list of integers
# if we want a list of 0 to 9
print(range(0, 10))  # it does not print the actual output
# note range is a genarator function, a genarator is a special type of function that will genarate information.
# and it not need to save to memory.

# so if we want to get actual output we need to cast it with list()
my_list = list(range(0, 10))
print(my_list)
# try
my_tuple = tuple(range(0, 10))
print(my_tuple)

# step size:
my_list = list(range(0, 10, 2))
print(my_list)

# enumurate: enumurate is very handy with for loops:

# imagine
# index_count = 0
# for item in 'hello world':
#     print('at {} index letter is {}'.format(index_count, item))
#     index_count += 1

# the commented example is the same of it.
# it similar to the tuple unpacking.
for index_count, item in enumerate('hello world'):
    print('at {} index letter is {}'.format(index_count,item))
