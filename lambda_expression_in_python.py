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