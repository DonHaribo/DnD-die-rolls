import random
# Using while loop to enable rolling repeatedly
while True:
    # user input and processing of number of die and die size
    dice_roll = input('Roll your dice: ')
    d_location = int(dice_roll.find('d'))
    number_of_die = dice_roll[0: d_location]
    die_size = int(dice_roll[d_location + 1:])
    # execution of dice roll
    dice_list = []
    if number_of_die != '':
        for single_die_roll in range(1, int(number_of_die)+1):
            random.randint(1, die_size)
            dice_list.append(single_die_roll)
    else:
        single_die_roll = random.randint(1, die_size)
        dice_list.append(single_die_roll)
    pre_modifier_roll = sum(dice_list)
    print(pre_modifier_roll)
    print(dice_list)

    # adjusting the roll by a modifier
    modifier = input('What modifier would you like to use? ')
    if '+' in modifier:
        print(pre_modifier_roll + int(modifier[1:]))
    elif '-' in modifier:
        print(pre_modifier_roll - int(modifier[1:]))
    elif '*' in modifier:
        print(pre_modifier_roll * int(modifier[1:]))
    elif '/' in modifier:
        print(pre_modifier_roll // int(modifier[1:]))
    # if no modifies used
    else:
        print('No modifier used, dice roll remains: ' + str(pre_modifier_roll))
    # option to leave the loop
    go = input('If you dont want to roll again say "end" or continue by pressing enter ')
    if go.lower() == 'end':
        break
