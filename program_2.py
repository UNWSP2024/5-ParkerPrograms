# Nathan Parker
# 2/17/25
# Program #2: Math Quiz


# define a function that chooses a random three-digit number
def random_number():
    import random
    number = random.randint(100, 999)
    return number

# set number_1 and number_2 to random numbers by using the random_number function
number_1 = random_number()
number_2 = random_number()

# display the problem
print(f'''  {number_1}
+ {number_2}
——————''')

# get an answer from the user
answer = int(input('= '))

# determine if the answer is correct and display the appropriate message
if answer == number_1 + number_2:
    print('Correct!')
else:
    print('''Incorrect
The correct answer is''', number_1 + number_2)

