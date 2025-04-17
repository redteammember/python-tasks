date = input('Enter the date in DD.MM.YYYY format: ')

day = date[:2]
month = date[3:5]
year = date[-4:]

if len(date) == 10 and date[2] == '.' and date[5] == '.':
    if day.isdigit() and month.isdigit() and year.isdigit():
        if 1 <= int(day) <= 31 and 1 <= int(month) <= 12:
            print("Day:", date[:2])
            print("Month:", date[3:5])
            print("Year:", date[-4:])
            print(f"Swapped: {date[3:5]}.{date[:2]}.{date[-4:]}")
            print(f'Short year: {date[-2:]}')
        else:
            print("Please enter a valid date. There is an error in the day or month.")
    else:
        print("Please enter a valid date using only digits.")
else:
    print("Please enter a valid date using dots to separate day, month, and year.")
