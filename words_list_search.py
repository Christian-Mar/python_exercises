def woord_meeste_klinkers():
    klinkers = "aeiou"
    max_klinkers = 0
    woord_met_meeste_klinkers = ""

    with open("words.txt", 'r') as f:
        for regel in f:
            woorden = regel.split()
            for woord in woorden:
                aantal_klinkers = sum(1 for letter in woord if letter in klinkers)
                if aantal_klinkers > max_klinkers:
                    max_klinkers = aantal_klinkers
                    woord_met_meeste_klinkers = woord

    return woord_met_meeste_klinkers

resultaat = woord_meeste_klinkers()
print("Woord met de meeste klinkers:", resultaat)



