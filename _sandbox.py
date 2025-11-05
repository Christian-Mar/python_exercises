from datetime import datetime, date #,timedelta
from time import sleep

datetime.today() # geeft de dag van vandaag
datetime.now() # geeft ook de tijd mee

def long():
    sleep(5)

start_ts = datetime.now()
long()
end_ts = datetime.now()
print(f"This operation took: {end_ts - start_ts} seconds")

first_of_month = date(year = 2025, month = 11, day = 1)

# pendulum is een andere nuttige library, te installeren wel, niet standaard in Python

def balans_stenen(gewicht):
    # Werkt met variabelen, geen lijsten/dicts
    stenen1 = 1
    stenen3 = 3
    stenen9 = 9
    stenen27 = 27

    nog_over = gewicht

    # Bepaal plaatsing per steen
    k1 = ((nog_over + stenen1)//(2*stenen1)) - ((nog_over - stenen1)//(2*stenen1))
    nog_over -= k1 * stenen1

    k3 = ((nog_over + stenen3)//(2*stenen3)) - ((nog_over - stenen3)//(2*stenen3))
    nog_over -= k3 * stenen3

    k9 = ((nog_over + stenen9)//(2*stenen9)) - ((nog_over - stenen9)//(2*stenen9))
    nog_over -= k9 * stenen9

    k27 = ((nog_over + stenen27)//(2*stenen27)) - ((nog_over - stenen27)//(2*stenen27))
    nog_over -= k27 * stenen27

    # Print resultaat
    print(f"Voor {gewicht} kg:")
    print(f"1 kg steen: {'rechts' if k1==1 else ('links' if k1==-1 else 'niet gebruiken')}")
    print(f"3 kg steen: {'rechts' if k3==1 else ('links' if k3==-1 else 'niet gebruiken')}")
    print(f"9 kg steen: {'rechts' if k9==1 else ('links' if k9==-1 else 'niet gebruiken')}")
    print(f"27 kg steen: {'rechts' if k27==1 else ('links' if k27==-1 else 'niet gebruiken')}")
    print("")

# Voor alle gewichten
for w in range(1, 41):
    balans_stenen(w)

def my_function(x:int):
    if x < 0:
        return 0 # functie wordt uitgevoerd en verlaten, gaat dus uit de functie
    
    while True:
        x += 1

        if x > 5: 
            break # stopt de lus, maar gaat niet uit de functie

    for letter in "Vindevogel":
        if letter == "i":
            continue # gaat met de lus verder maar stopt tijdelijk ???

        print(letter)
    
print(my_function(-1))