def is_vodo_word(word):
    """
    Check if a word is a vodo word.
    
    A vodo word is a word where moving the first letter to the end
    results in the word reversed. In other words, if you rotate the
    word left by one position, you get the reverse of the original word.
    
    Args:
        word (str): The word to check
        
    Returns:
        bool: True if the word is a vodo word, False otherwise
        
    Examples:
        >>> is_vodo_word("vodo")
        True
        >>> is_vodo_word("Vodo")
        True
        >>> is_vodo_word("hello")
        False
        >>> is_vodo_word("ab")
        True
        >>> is_vodo_word("aba")
        False
        >>> is_vodo_word("a")
        True
        >>> is_vodo_word("")
        True
    """
    if len(word) == 0:
        return True
    
    normalized_word = word.lower()
    rotated_word = normalized_word[1:] + normalized_word[0]
    reversed_word = normalized_word[::-1]
    
    return rotated_word == reversed_word


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    print(is_vodo_word("vodo"))

def is_vodo_word_no_plus(word):
    """
    Check if a word is a vodo word.
    
    A vodo word is a word where moving the first letter to the end
    results in the word reversed. In other words, if you rotate the
    word left by one position, you get the reverse of the original word.
    
    Args:
        word (str): The word to check
        
    Returns:
        bool: True if the word is a vodo word, False otherwise
        
    Examples:
        >>> is_vodo_word("vodo")
        True
        >>> is_vodo_word("Vodo")
        True
        >>> is_vodo_word("hello")
        False
        >>> is_vodo_word("ab")
        True
        >>> is_vodo_word("aba")
        False
        >>> is_vodo_word("a")
        True
        >>> is_vodo_word("")
        True
    """
    if len(word) == 0:
        return True
    
    normalized_word = word.lower()
    rotated_word = ''.join([normalized_word[1:], normalized_word[0]])
    reversed_word = normalized_word[::-1]
    
    return rotated_word == reversed_word


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    print(is_vodo_word_no_plus("vodo"))   