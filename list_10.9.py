import time


def read_words_append(filename):
    """Reads words from file using append method."""
    words = []
    with open(filename) as f:
        for line in f:
            words.append(line.strip())
    return words


def read_words_concat(filename):
    """Reads words from file using t = t + [x] idiom."""
    words = []
    with open(filename) as f:
        for line in f:
            words = words + [line.strip()]
    return words


if __name__ == "__main__":
    filename = "words.txt"

    # Time the append version
    start = time.time()
    words1 = read_words_append(filename)
    end = time.time()
    print(f"append method: {end - start:.4f} seconds")

    # Time the concatenation version
    start = time.time()
    words2 = read_words_concat(filename)
    end = time.time()
    print(f"t = t + [x] method: {end - start:.4f} seconds")

    print(f"\nBoth lists have {len(words1)} words")

    # Why is t = t + [x] slower?
    # append() modifies the list in place - O(1) operation
    # t = t + [x] creates a new list each time - O(n) operation
    
