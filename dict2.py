from pathlib import Path

words = Path("words.txt").read_text().splitlines()

def is_interlocking(word):

    evens = word[::2] # starts at 0, takes 2 steps
    odds = word[1::2] # starts at 1, takes 2 steps
    if evens in words and odds in words:
        return True
    
print(is_interlocking("schooled"))
print(is_interlocking("smoodnak"))



# 1. Lees de woorden en maak er een SET van voor supersnelle lookups
word_list = Path("words.txt").read_text().splitlines()
word_set = set(word_list)

def find_all_interlocking():
    interlocking_results = []
    
    # 2. Gebruik slechts één loop door alle woorden
    for word in word_list:
        # Een interlock moet minimaal 2 letters hebben om opgesplitst te worden
        if len(word) < 2:
            continue
            
        evens = word[::2]
        odds = word[1::2]
        
        # 3. Check direct in de set of beide delen bestaan
        if evens in word_set and odds in word_set:
            interlocking_results.append((word, evens, odds))
            
    return interlocking_results

# Uitvoeren en resultaten tonen
results = find_all_interlocking()
for word, p1, p2 in results:
    print(f"{word} is een interlock van '{p1}' en '{p2}'")

# with new text-file

# 1. Inlezen
word_list = Path("words.txt").read_text().splitlines()
word_set = set(word_list)

def save_interlocking_words(output_file):
    # 2. Open het nieuwe bestand om in te schrijven ('w' staat voor write)
    with open(output_file, 'w', encoding='utf-8') as f:
        count = 0
        for word in word_list:
            if len(word) < 2:
                continue
                
            evens = word[::2]
            odds = word[1::2]
            
            if evens in word_set and odds in word_set:
                # 3. Schrijf naar het bestand in plaats van naar de terminal
                f.write(f"{word}: {evens} + {odds}\n")
                count += 1
        
        print(f"Klaar! Er zijn {count} interlocking words gevonden en opgeslagen in {output_file}.")

# Voer de functie uit
save_interlocking_words("interlocking_results.txt")    