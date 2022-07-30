# library working with RNG
import random
# Using while loop to enable rolling repeatedly
while True:
    # user input and processing for number of die and die size
    dice_roll = input('Roll your dice: ')
    number = int(dice_roll.find('d'))
    number_of_die = dice_roll[0: number]
    die_size = int(dice_roll[number + 1:])

    pre_addition_roll = int(number_of_die) * int(random.randint(1, die_size))
    print(pre_addition_roll)

    # adjusting the roll by a modifier
    modifier = input('What modifier would you like to use? ')
    if '+' in modifier:
        print(pre_addition_roll + int(modifier[1:]))
    elif '-' in modifier:
        print(pre_addition_roll - int(modifier[1:]))
    elif '*' in modifier:
        print(pre_addition_roll * int(modifier[1:]))
    elif '/' in modifier:
        print(pre_addition_roll // int(modifier[1:]))
    # if no modifies used
    else:
        print('No modifier used')
    # option to leave the loop
    go = input('If you dont want to roll again say "end" or continue by pressing enter ')
    if go.lower() == 'end':
        break
