import random
import re

pattern = re.compile(r'(\d+)?\s?d(100|4|6|8|10|12|20)(\s)?([+-]\s?\d+)?')

while True:
    user = input('Roll the dice, "h" for help:\n')
    x = pattern.search(user)
    if x is not None:
        match = x.group()
        if '+' in match:
            add = int(match.split('+')[1])
            match = match.split('+')[0]
        elif '-' in match:
            add = -int(match.split('-')[1])
            match = match.split('-')[0]
        else:
            add = 0
        if match[0].isnumeric():
            rolls = int(match.split('d')[0])
        else:
            rolls = 1
        total = 0
        for roll in range(rolls):
            roll_val = random.randint(1, int(match.split('d')[1]))
            if add:
                print(f'{roll_val} (+ {add} = {roll_val + add})')
            else:
                print(roll_val)
            total += roll_val
        if rolls > 1:
            if add:
                print(f'total: {total} (+ {add} = {total + add}, + {add * rolls} = {total + (add * rolls)})')
            else:
                print(f'total: {total}')
    elif user.lower() == 'h':
        print('Type the amount of dice, followed by "d", followed by a dice type.')
        print('Optionally add "+" to add a number to your roll.')
        print('Example roll: "2d20+5"')
        print('Dice types: 4, 6, 8, 10, 12, 20, 100')
    else:
        print('Invalid roll, try again.')
    print()
