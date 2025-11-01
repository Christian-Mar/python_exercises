def power_check(number, power_base):

    x = 2
    is_perfect_power = False

    while power_base ** x <= number:
        if power_base ** x == number:
            print(f"{power_base} tot de {x}e macht = {number}")
            is_perfect_power = True
            return
            
        x += 1

    if not is_perfect_power: 
       print(f"{power_base} kan niet via een machtverheffing met een geheel getal tot {number} komen.")
            

if __name__ == "__main__":

    number = int(input("Geef een getal waarvan je wil checken of dit een macht is van je tweede input: "))
    power_base = int(input("Geef een getal waarvan je vermoedt dat het tot een bepaalde macht het eerste getal weergeeft: "))
    power_check(number, power_base)
    