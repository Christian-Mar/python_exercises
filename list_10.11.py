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


def find_reverse_pairs(words):
    """Finds all reverse pairs in a sorted list of words."""
    pairs = []
    for word in words:
        reversed_word = word[::-1]
        # Only check if reversed word comes after current word to avoid duplicates
        if reversed_word > word and in_bisect(words, reversed_word):
            pairs.append((word, reversed_word))
    return pairs


if __name__ == "__main__":
    # Load words from words.txt
    words = []
    with open("words.txt") as f:
        for line in f:
            words.append(line.strip())

    print(f"Loaded {len(words)} words")

    pairs = find_reverse_pairs(words)
    print(f"Found {len(pairs)} reverse pairs:\n")
    for word, reversed_word in pairs:
        print(f"{word} <-> {reversed_word}")
