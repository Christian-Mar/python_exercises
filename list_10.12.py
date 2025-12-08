def in_bisect(sorted_list, target):
    """Uses binary search to check if target is in sorted_list."""
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] == target:
            return True
        elif sorted_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return False


def extract_letters(word, start, step):
    """Extracts every 'step' letter from word, starting at 'start'."""
    return word[start::step]


def find_interlocked_pairs(words):
    """Finds all pairs of words that interlock to form another word."""
    pairs = []
    for word in words:
        # Split word into alternating letters
        word1 = extract_letters(word, 0, 2)  # even positions
        word2 = extract_letters(word, 1, 2)  # odd positions
        # Check if both halves are valid words
        if in_bisect(words, word1) and in_bisect(words, word2):
            pairs.append((word, word1, word2))
    return pairs


def find_three_way_interlocked(words):
    """Finds words that are three-way interlocked."""
    triples = []
    for word in words:
        # Split word into every third letter starting at 0, 1, 2
        word1 = extract_letters(word, 0, 3)
        word2 = extract_letters(word, 1, 3)
        word3 = extract_letters(word, 2, 3)
        # Check if all three are valid words
        if in_bisect(words, word1) and in_bisect(words, word2) and in_bisect(words, word3):
            triples.append((word, word1, word2, word3))
    return triples


if __name__ == "__main__":
    # Load words from words.txt
    words = []
    with open("words.txt") as f:
        for line in f:
            words.append(line.strip())

    print(f"Loaded {len(words)} words\n")

    # Part 1: Find interlocked pairs
    print("=== Two-way interlocked words ===")
    pairs = find_interlocked_pairs(words)
    print(f"Found {len(pairs)} interlocked words:\n")
    for word, word1, word2 in pairs[:20]:  # Show first 20
        print(f"{word} = {word1} + {word2}")
    if len(pairs) > 20:
        print(f"... and {len(pairs) - 20} more")

    # Part 2: Find three-way interlocked words
    print("\n=== Three-way interlocked words ===")
    triples = find_three_way_interlocked(words)
    print(f"Found {len(triples)} three-way interlocked words:\n")
    for word, word1, word2, word3 in triples:
        print(f"{word} = {word1} + {word2} + {word3}")
