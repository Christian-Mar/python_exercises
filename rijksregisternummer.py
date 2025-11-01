# Schrijf een functie die de geldigheid van het kaartnummer van een e-id card verifieert.  Als parameter krijg je het volledige kaartnummer zonder streepjes, dus als een integer.  Het principe is dat het eerste gedeelte van het kaartnummer module 97 gelijk moet zijn aan de laatste 2 cijfers.  In enkele gevallen wordt dit laatste nummer ook bepaald door het getal 100 min de modulo van 97.

# Schrijf een gelijkaardige functie die het rijksregisternummer nakijkt op de geldigheid.

# Schrijf een functie die van een rijksregisternummer nakijkt of je als man of vrouw geboren bent.

# Schrijf een functie die nakijkt of een jaartal een schrikkeljaar is.

# Schrijf een functie die het aantal dagen in de maand terug stuurt

# Zoek op het internet naar een functie om te bepalen op welke weekdag de eerste dag van de maand valt.  Tip: het is een algoritme geschreven door een Japanner.

# Schrijf een functie die bepaalt of een nummer een priemgetal is of niet.


def check_id(id_number_string):
#    id_number_string = input("Can you give me your id-number (11 characters), please: ")

    if len(id_number_string) != 11: # controll input
        print("You didn't have 11 characters")

    first_nine_numbers = int(id_number_string[0:9])
    # print(first_nine_numbers) # check
    last_two_numbers = int(id_number_string[9:11])
    # print(last_two_numbers) # check

    if 97 - (first_nine_numbers % 97) == last_two_numbers:
        print("Valid number")
    elif 100 - (first_nine_numbers % 97) == last_two_numbers:
        print("Valid number")
    else:
        print("False number")

    if first_nine_numbers % 2 == 0:
        print("You're female")
    else:
        print("Your're male")



id_number_string = input("Can you give me your id-number (11 characters), please: ")
check_id(id_number_string)