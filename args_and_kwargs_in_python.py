# lets see an example:
def example_func(a=0, b=0, c=0): # puts three default argument
    return sum((a,b,c))
ans = example_func(2,3,4)
print(ans)  # it return the ans
# but if we want to put more argument in this example_func() like
# ans1 = example_func(1,2,3,4,5,6,7)
# print(ans1)  # it shows an error: this function will take from 0 to 3 positional arguments

# for this problem solution we use *args:
def example_func1(*args): # it take whatever name we give after *: like: *hello
    return sum(args)
ans2 = example_func1(1,2,3,4,5,6,7)
print(ans2)
# when a function argument start with 'asterisk(*)' its allows programmer to take an arbitary number of arguments and take them in tule values
