import random

number = random.randint(1, 10)

answer = input('Enter a number from 1 to 10 (or type "give up"): ').lower()
attempts = 0

if answer == 'give up':
    print('Game over...')
    exit()

answer = int(answer)
while answer != number:
    if attempts < 4:
        print('Incorrect, try again!')
        attempts += 1
        if answer > number:
            print("Lower")
        else:
            print('Higher')
        answer = int(input('Enter a number from 1 to 10: '))

    else:
        print("Game over...")
        break

if answer == number:
    print('You guessed it! Victory!')
    print(f'You guessed the number in {attempts + 1} attempts.')
