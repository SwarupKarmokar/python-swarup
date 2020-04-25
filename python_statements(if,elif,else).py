# basic example

a = True # run this code using False
if a:
    print('code is correct')
else:
    print('code is not correct')


# lets doing some stuffs
input1 = input('enter a name: ')

if input1 == 'swarup':
    print('Welcome swarup')
elif input1 == 'Swarup':  # in other programming language its call else if statement
    print('Welcome SWARUP')
else:
    print('thank you!')


# try
print('welcome to the guessing game:')
print('you have three chance to win the game')
import random
input2 = int(input('enter a number=> '))
if input2 == random.randint(0,1):
    print('you guess the number at first chance')
elif input2 == random.randint:
    print('you guess the number at second chance')
elif input2 == random.randint:
    print('you guess the number at very last chance')
else:
    print('you loose the guess game')
