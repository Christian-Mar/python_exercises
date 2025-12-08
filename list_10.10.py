def in_bisect(sorted_list, target):
    """Uses binary search to check if target is in sorted_list."""
    low = 0
    high = len(sorted_list) - 1
    steps = 0

    while low <= high:
        steps += 1
        mid = (low + high) // 2
        if sorted_list[mid] == target:
            return True, steps
        elif sorted_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return False, steps


if __name__ == "__main__":
    # Load words from words.txt
    words = []
    with open("words.txt") as f:
        for line in f:
            words.append(line.strip())

    print(f"Loaded {len(words)} words")

    # Test the binary search
    found, steps = in_bisect(words, 'apple')
    print(f"'apple': found={found}, steps={steps}")

    found, steps = in_bisect(words, 'banana')
    print(f"'banana': found={found}, steps={steps}")

    found, steps = in_bisect(words, 'zzzzzz')
    print(f"'zzzzzz': found={found}, steps={steps}")

    found, steps = in_bisect(words, 'python')
    print(f"'python': found={found}, steps={steps}")
