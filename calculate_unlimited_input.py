print("Voer float-getallen in. Gebruik 0 om te stoppen.")

total = 0.0   # som
product = 1.0 # product
count = 0     # aantal getallen

while True: # nog niet gekend hoeveel inputs er zullen zijn
    x = float(input("Getal: "))
    if x == 0.0: # while True blijft doorlopen tot er een 0.0 of 0 gegeven wordt. 
        break
    # na alle inputs, de berekening
    total += x
    product *= x
    count += 1

if count == 0:
    print("Geen getallen ingevoerd.") # check
else:
    average = total / count
    print("Som:", total)
    print("Product:", product)
    print("Gemiddelde:", average)
