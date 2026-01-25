def signature(word):
    """Returns a string with the letters of the word sorted."""
    t = list(word)
    t.sort()
    t = ''.join(t)
    return t

def bingo_solver(filename):
    """Finds the collection of 8 letters that forms the most possible bingos."""
    d = {}
    try:
        with open(filename, 'r') as f:
            for line in f:
                word = line.strip().lower()
                if len(word) == 8:
                    t = signature(word)
                    if t not in d:
                        d[t] = [word]
                    else:
                        d[t].append(word)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return

    # Find the set with the most words
    max_len = 0
    best_set = []
    best_signature = ""

    for t in d:
        if len(d[t]) > max_len:
            max_len = len(d[t])
            best_set = d[t]
            best_signature = t
    
    if best_set:
        print(f"The collection of 8 letters that forms the most bingos is: {best_signature}")
        print(f"Number of bingos: {max_len}")
        print(f"Words: {best_set}")
    else:
        print("No 8-letter words found.")

if __name__ == '__main__':
    bingo_solver('words.txt')
