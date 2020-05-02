# in this topic we see how python deal with variable names we assign. pthon variable store in name_space.
# variable name visiblity to other part of code called scope.

# we can see in LEGB rule in this topic:
# L = locals: define variable within a function
# E = enclosing function locals: this is the function inside function
# G = global(module): variable assign at the top of code
# B = built_in: python pre_installed module: open, range, len, syntax error

# global variable
name = 'global name: hello all'

def locals(name):
    # locals variable
    print('name is: ',name)

    # enclosing function
    def welcome():
        print('hello ', name)

    welcome()

locals('swarup')

print(name)