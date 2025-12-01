CLASSROOM = ['Yves', 'Brent', 'Femke', 'Jeroen', 'Uwe', 'Bas', 'Robin', 'Hendrik-Jan', 'Christian']
CLASSROOM_NEW = []

PROVINCES = ['West-Vlaanderen', 'Oost-Vlaanderen', 'Antwerpen', 'Vlaams-Brabant', 'Waals-Brabant', 'Limburg', 'Namen', 'Luxemburg']
PROVINCES_NEW = []

def clear_names_starting_with_vowel(first_list, new_list):
    vowels = 'AEIOUY'
    for name in first_list:
        if name[0] not in vowels:
            new_list.append(name)
    return new_list

clear_names_starting_with_vowel(CLASSROOM, CLASSROOM_NEW)
print("Original:", CLASSROOM)
print("Filtered:", CLASSROOM_NEW)

clear_names_starting_with_vowel(PROVINCES, PROVINCES_NEW)
print("Original:", PROVINCES)
print("Filtered:", PROVINCES_NEW)

# verschil tussen delete, remove en pop
# opletten want indexen vallen weg, waardoor 2 woorden met klinkers na elkaar overgeslagen worden
# list comprehension
# linked list

print(PROVINCES.sort()) # None? 
