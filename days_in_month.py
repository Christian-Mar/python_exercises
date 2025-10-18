from leap_year import leap_year

def days_in_month(month, year):
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in (4, 6, 9, 11):
        return 30
    elif month == 2:
        return 29 if leap_year(year) else 28
    else:
        print("The month needs to be a number from 1 to 12")

if __name__ == '__main__':    
    month = int(input("Can you give me a month (from 1 to 12), please: "))
    year = int(input("Can you give me a year (4 characters), please: "))
    print(days_in_month(month, year))       