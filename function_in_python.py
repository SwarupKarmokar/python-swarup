# function: a function is a useful device that group together a set of statements so they they can run more than one.
# functions will be one of the most basic levels of reusing code in python.

# syntax:
def function_name(arguments):
    '''
    it is called docstring, docstring helps programmer about the programming code
    '''
    # code here

# example:
def hello(): # default argument
    print('hey how are you')

# calling the func:
hello()


# using return statement:
# sum:
def sum1(a, b): # we can perform multiplication,division,subtraction etc
    return a+b

result = sum1(4,5)  # using return statement we can store the output of the function and reuse the output in other programe

print(result)

# return two string:
result1 = sum1('iam', ' swarup')
print(result1)
# in python we don't declare variable type so user make sure to check put the right variable arguments

# prime number checking:
def prime_num(number):
    '''

    :param num: naive method of checking prime number
    :return: prime number
    '''

    for n in range(2,number):
        if number % n == 0:
            print(number, ' is not prime')
            break
    else:
        print(number, ' is prime')

prime_num(17)
prime_num(16)