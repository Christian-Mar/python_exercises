# Oefening 1: is een woord een palindroom

def is_palindrome(word):
    """
    Check if a word is a palindrome.
    
    A palindrome is a word that reads the same forwards and backwards,
    ignoring case differences.
    
    Args:
        word (str): The word to check
        
    Returns:
        bool: True if the word is a palindrome, False otherwise
        
    Examples:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("Racecar")
        True
        >>> is_palindrome("hello")
        False
        >>> is_palindrome("A")
        True
        >>> is_palindrome("Noon")
        True
        >>> is_palindrome("")
        True
    """
    normalized_word = word.lower()
    return normalized_word == normalized_word[::-1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()

print(is_palindrome("racecar"))

# Oefening 5: wat is het langste palindroom in word.txt

def find_longest_palindrome(filename):
    longest_palindrome = ""

    with open(filename, 'r') as file:
        for line in file:
            word = line.strip() # get the word pure
            if is_palindrome(word) and len(word) > len(longest_palindrome):
                longest_palindrome = word
    
    return longest_palindrome if longest_palindrome else None

if __name__ == "__main__":
    result = find_longest_palindrome("words.txt")
    print(result)



# Oefening 4: komt dit anagram ook voor in de lijst word.txt
# Oefening 5: wat is het langste palindroom in word.txt
