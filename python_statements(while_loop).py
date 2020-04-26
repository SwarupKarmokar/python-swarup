# while statement will repeatedly execute a code as long as the condition is true:
sum1 = 0
while sum1 < 5:
    print('sum is => ', sum1)
    print('adding 1 in sum1')
    sum1 += 1
print('end')

# try
name = ''
while name != "swarup":
    name = input('enter the right name=> ')
print('the name is: ', name)


# break, continue, pass function:
# lets understand through the example
sum1 = 0
while sum1 < 5:
    print('sum is ', sum1)
    print('adding 1 to sum1')
    sum1 += 1
    if sum1 == 3:
        print('breaking the loop because sum1 == 3')
        break
    else:
        print('continue')

# try
while sum1 < 5:
    print('sum is ', sum1)
    print('adding 1 to sum1')
    sum1 += 1
    if sum1 == 3:
        print('sum1 == 3')
    else:
        continue