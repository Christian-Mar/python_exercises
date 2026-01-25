def has_duplicates(sequence): # with dict
    seen = {} # dict takes a word and checks on duplicates
    for element in sequence: # loop over 1 sequence
        if element in seen:
            return True
        seen[element] = True
    return False

def has_duplicates2(sequence): # with set
    return len(set(sequence)) < len(sequence) # True if set is smaller than original sequence

def find_longest_unique_word(filename):
    longest = ""

    with open(filename) as f:
        for line in f: # loop over the whole list
            word = line.strip().lower()
            if not has_duplicates2(word) and len(word) > len(longest):
                longest = word

    return longest

longest = find_longest_unique_word("words.txt")
print(f"Longest word with unique letters: '{longest}'")
print(f"Length: {len(longest)}")
print(f"{has_duplicates('cata')}")
print(f"{has_duplicates2('cat')}")
