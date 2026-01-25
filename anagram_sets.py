def signature(word):
    """Returns a string with the letters of the word sorted."""
    t = list(word)
    t.sort()
    t = ''.join(t)
    return t

def all_anagrams(filename):
    """Reads a word list from a file and prints all sets of words that are anagrams."""
    d = {}
    try:
        with open(filename, 'r') as f:
            for line in f:
                word = line.strip().lower()
                t = signature(word)
                if t not in d:
                    d[t] = [word]
                else:
                    d[t].append(word)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return

    
    # Collect all sets that are actual anagrams (more than 1 word)
    anagram_sets = []
    for t in d:
        if len(d[t]) > 1:
            anagram_sets.append(d[t])
    
    # Sort the sets by length in descending order
    anagram_sets.sort(key=len, reverse=True)

    # Print the sorted sets (top 20)
    for s in anagram_sets[:20]:
        print(s)

if __name__ == '__main__':
    all_anagrams('words.txt')
