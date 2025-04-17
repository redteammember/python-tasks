word = str(input('Enter a word: '))

def getMiddle(word):
    middle = len(word) // 2
    if len(word) % 2 == 0:
        return word[middle - 1 : middle + 1]
    else:
        return word[middle]

if len(word) < 3:
    print("The word is too short for analysis.")
else:
    print('First character of the word:', word[0])
    print('Last character of the word:', word[-1])
    print('Middle of the word:', getMiddle(word))
    print('The word reversed:', word[::-1])
