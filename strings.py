import uuid

fruit = "banana"

first_letter = fruit[0]
second_letter = fruit[1]

i = -1
print(fruit[i])
print(fruit[0:3])
print(fruit[0:10])
print(fruit[0:5:2])
print(fruit[3:])
print(fruit[::-1])
print("20251101" > "20251010")
# Datums altijd scrhijven als 2025-10-1
# In toepassingen altijd calender controll gebruiken om inputfouten te voorkomen

print(uuid.uuid4())
# beter:
print(uuid.uuid5())
# want sorteerbaar ??? -> uuid7 - Python 3.14?

ip = ["127", "0", "0", "1"]
print(".".join(ip))

# files:
# R - read
# W - write
# A - append
# RB - read binary ...

name = "Yves"
if name is not None: # niet !=
    pass

# Oefening 1: is een woord een palindroom
# Oefening 2: id een woord een vodo-woord (eerste letter vanachter, dan omgekeerd leest het hetzelfde
# Oefening 3: is een woord een anagram (met dezelfde letter een ander woord vormen)
# Oefening 4: komt dit anagram ook voor in de lijst word.txt
# Oefening 5: wat is het langste palindroom in word.txt
# Oefening 6: schrijf oefening 2 zonder het plusteken te gebruiken
