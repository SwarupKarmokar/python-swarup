# lambda expression: it is a most useful tool that allow us to create "anonymous" function.
# we understand this using example:
def return_square(num):
    return num ** 2
ans = return_square(2)
print(ans)

# now
# using the lambda expression:
ans = lambda num: num ** 2
print(ans)  # its return the memory location of the function
# creating the anonymous function:
result = ans(6)
print(result)

# lambda expression with map and filter function=>
# see map and filter function before doing this.

# lambda expression with map function:
my_number = list(range(10))
ans = list(map(lambda num: num ** 3, my_number))
print(ans)

# lambda expression with filter function:
ans1 = list(filter(lambda num: num % 2 ==0, my_number))
print(ans1)