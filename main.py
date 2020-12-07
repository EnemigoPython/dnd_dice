import random
import re

pattern = re.compile(r'(\d+)?\s?d(4|6|8|10|12|20|100)')

while True:
    user = input('Roll the dice, "h" for help\n')
    x = pattern.match(user)
    if x is not None:
        if user[0].isnumeric():
            total = 0
            for roll in range(int(user.split('d')[0])):
                total += random.randint(1, int(user.split('d')[1]))
            print(total)
        else:
            print(random.randint(1, int(user.split('d')[1])))
    elif user.lower() == 'h':
        print('Type the amount of die, followed by "d", followed by a dice type')
        print('Dice types: 4, 6, 8, 10, 12, 20, 100')
    else:
        print('Invalid roll, try again.')