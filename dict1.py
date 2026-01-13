def has_duplicates(sequence):
    seen = {}
    for element in sequence:
        if element in seen:
            return True
        seen[element] = True
    return False


def find_longest_unique_word(filename):
    longest = ""

    with open(filename) as f:
        for line in f:
            word = line.strip().lower()
            if not has_duplicates(word) and len(word) > len(longest):
                longest = word

    return longest

longest = find_longest_unique_word("words.txt")
print(f"Longest word with unique letters: '{longest}'")
print(f"Length: {len(longest)}")
