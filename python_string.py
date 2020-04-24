# python support both single and double quotes because python is very flexible
my_string = 'my name is swarup karmokar'
print(my_string)

my_string = "my name is swarup karmokar"
print(my_string)

# now try
#my_string = 'kalu and lalu are swarup's pets'
# its shows error because when the single quote end python interpreter don't recognize rest of the code
# now try
my_string = "kalu and lalu are swarup's pets"



# string basics operation=>
# use of len method:
my_string = 'Hello World'
print(len(my_string))
# len method return length of a string

# string indexing and slicing=>
# indexing:
my_string = 'Hello World'
print(my_string[4]) # its return a index position

# slicing:
my_string = 'Hello World'
print(my_string[:])
print(my_string[:3])
print(my_string[1:-1])
print(my_string[-1])
print(my_string[::2]) # step size
print(my_string[::-1]) # reverse string

# string mutablity
my_string[0] = 'X'
print(my_string[0])  # string are immutable its shows an error

# string concatenation:
my_name = 'swarup'
color = 'black'
print(my_name + ' loves' + color)

# string concatenation using formatted string:
print(f'{my_name} + " favarite color is" + {color}')

print('hello {} how are you'.format('swarup'))

print("hello {name} so your favrite color is {color}".format(name = 'swarup', color = 'black'))

# index formatting concatenation:
print('hello {1} so your favrite color is {0}'.format('swarup','black'))


# Built in string methods=>
my_string = 'hello everyone'
# for Upper casing the letter of the string
print(my_string.upper())
# for lower casing the letter of the string
print(my_string.lower())
# split a string and making a list:
print(my_string.split())
# split by a specific element:
print(my_string.split('o'))