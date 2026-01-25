def signature(word):
    """Returns a string with the letters of the word sorted."""
    t = list(word)
    t.sort()
    t = ''.join(t)
    return t

def word_distance(word1, word2):
    """Returns the number of indices where two words differ."""
    count = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            count += 1
    return count

def all_metathesis_pairs(filename):
    """Finds and prints all metathesis pairs in the dictionary."""
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

    # Check for metathesis pairs within anagram sets and write to file
    output_file = 'metathesis_pairs.txt'
    with open(output_file, 'w') as out:
        for t in d:
            words = d[t]
            if len(words) > 1:
                for i in range(len(words)):
                    for j in range(i + 1, len(words)):
                        if word_distance(words[i], words[j]) == 2:
                            out.write(f"{words[i]} {words[j]}\n")
    
    print(f"Metathesis pairs have been written to '{output_file}'.")

if __name__ == '__main__':
    all_metathesis_pairs('words.txt')
