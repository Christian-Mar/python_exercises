import doctest

def count_common_unique_letters_manual(word1, word2):
    """
    Calculates the number of unique letters shared between two words
    without using sets, lists, or tuples.

    It uses a string accumulator to manually track unique common characters.

    Parameters
    ----------
    word1 : str
        The first word.
    word2 : str
        The second word.

    Returns
    -------
    int
        The count of unique common letters.

    Examples
    --------
    Test case from the prompt: 'e' is the only common unique letter.
    >>> count_common_unique_letters_manual('meer', 'sleep')
    1
    
    Multiple common unique letters, including different case:
    >>> count_common_unique_letters_manual('Apple', 'aPricot')
    2
    
    No common letters:
    >>> count_common_unique_letters_manual('CAT', 'dog')
    0
    
    Common letters: r, i, d
    >>> count_common_unique_letters_manual('Rider', 'Drive')
    4
    """
    # Initialize variables
    common_count = 0
    # String used to track unique characters found (replaces the set)
    common_chars = ""
    
    # Ensure case-insensitivity
    word1_lower = word1.lower()
    word2_lower = word2.lower()

    # Iterate through the first word
    for char in word1_lower:
        # 1. Check if the character is present in the second word
        if char in word2_lower:
            # 2. Check if the character has already been counted
            # (Checking existence in a string is much slower than in a set)
            if char not in common_chars:
                common_count = common_count + 1
                # Mark the character as counted by adding it to the tracker string
                common_chars = common_chars + char
                
    return common_count

if __name__ == "__main__":
    print("Running doctests for manual implementation...")
    doctest.testmod(verbose=False)
    print("Tests finished.")

print(count_common_unique_letters_manual('meest', 'leder'))    