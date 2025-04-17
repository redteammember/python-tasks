password = str(input('Enter a password: '))

def PasswordMask(password):
    AmountOfDots = len(password[2:-2])
    print(password[:2] + '*' * AmountOfDots + password[-2:])

if len(password) > 4:
    password_backwarts = password[::-1]
    print('First 2 characters:', password[0:2])
    print('Last 3 characters:', password[-3:])
    print('Reversed (every 2nd character):', password_backwarts[::2])
    print('Mask:', PasswordMask(password))
else:
    print('The password is too short!')
