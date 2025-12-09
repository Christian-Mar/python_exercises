import random

def binaire_zoek_stappen(doelgetal):
    
    laag = 1
    hoog = 10000
    stappen_teller = 0
    
    # if not 1 <= doelgetal <= 10000:
    #    return "Fout: Het doelgetal ligt buiten het bereik (1-10000)."

    while laag <= hoog:
        stappen_teller += 1
        
        # Bepaal het midden (Integer deling // zorgt voor een geheel getal)
        midden = (laag + hoog) // 2
        
        # 2. Vergelijk het midden met het doelgetal
        if midden == doelgetal:
            # Gevonden!
            return stappen_teller
        elif midden < doelgetal:
            # Het doelgetal moet in de rechterhelft liggen.
            # Verplaats de 'laag' grens naar 'midden + 1'.
            laag = midden + 1
        else: # midden > doelgetal
            # Het doelgetal moet in de linkerhelft liggen.
            # Verplaats de 'hoog' grens naar 'midden - 1'.
            hoog = midden - 1
            
    # Dit zou in dit geval niet mogen gebeuren, tenzij de input ongeldig is.
    return "Het getal is niet gevonden (wat onwaarschijnlijk is in dit bereik)."

# --- Voorbeeld Gebruik ---

# Genereer een willekeurig getal tussen 1 en 10000
willekeurig_getal = random.randint(1, 10000)

aantal_stappen = binaire_zoek_stappen(willekeurig_getal)

print(f"Het willekeurige getal om te zoeken is: **{willekeurig_getal}**")
print(f"Het aantal stappen dat nodig was om {willekeurig_getal} te vinden: **{aantal_stappen}** keer")