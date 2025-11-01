# Schrijf een functie die nakijkt of een jaartal een schrikkeljaar is.

def leap_year(year:int) -> bool:

    if len(str(year)) != 4: # controll input - str is optional here but makes it more clear
        print("To check a leap year I need a year written with 4 characters")

    # to make calculation able, converting string into integers

    if (int(year) % 4 == 0 and int(year) % 100 != 0) or (int(year) % 400 == 0):
        return True
    return False        

if __name__ == '__main__':    
    year = input("Can you give me a year (4 characters), please: ")
    print(leap_year(year))

def leap_year_revised(year:int) -> bool:
    if year % 400 or 4 == 0:
        return True
    if year % 100 == 0:
        return False    
    
    # asserts voor 2000, 2001, 2002, 2004, 