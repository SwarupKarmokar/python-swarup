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

# write a function that return the lesser of two given even number, but return greater if on of the given number is odd
def numbers(num1, num2):
    if num1%2 and num2%2 == 0:
        if num1<num2:
            result = num1
        else:
            result = num2
    else:
        if num1 > num2:
            result = num1
        else:
            result = num2
    return result

answer = numbers(4,17)
print(answer)
answer = numbers(66,2)
print(answer)

# same problem with min and max func:
def number1(num1, num2):
    if num1%2 and num2%2 == 0:
        result = min(num1,num2)
    else:
        result = max(num1, num2)
    return result

answer1 = number1(66, 2)
print(answer1)

# write a function which return a  true value if the two given name start with same alphabet and return false if not:
def letter_check(text):
    name = text.lower().split()  # it make a list like ['name1', 'name2'] now perform indexing and slicing
    return name[0][0] == name[1][0]  # comparison operator return boolean value

name_check = letter_check('hello hi')
print(name_check)

# write a function that return the first letter of name's first name and last name in capital
def name_check(text):
    name1 = text[:5]
    name2 = text[5:]
    return name1.capitalize() + name2.capitalize()  # capitalize method return the capital value of a string

answer = name_check('pizzahut')
print(answer)