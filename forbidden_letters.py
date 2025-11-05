def uses_none(word, forbidden):
    """Checks whether a word avoid forbidden letters.
    >>> uses_none('banana', 'xyz')
    True
    >>> uses_none('apple', 'efg')
    False
    """
    
    for letter in word.lower():
        if letter in forbidden.lower():
            return False
    return True
            
print(uses_none('banana', 'xyz'))

def uses_only(word, available):
    """Checks whether a word uses only the available letters.
    >>> uses_only('banana', 'ban')
    True
    >>> uses_only('apple', 'apl')
    False
    """

    for letter in word.lower():
        if letter not in available.lower():
            return False
    return True

print(uses_only('apple', 'apl'))

def uses_all(word, required):
    """Checks whether a word uses all required letters.
    >>> uses_all('banana', 'ban')
    True
    >>> uses_all('apple', 'api')
    False
    """
    for letter in required.lower():
        if letter not in word.lower():
            return False
    return True

print(uses_all('apple', 'api'))

def check_word(word, available, required):
    """Check whether a word is acceptable.
    >>> check_word('color', 'ACDLORT', 'R')
    True
    >>> check_word('ratatat', 'ACDLORT', 'R')
    True
    >>> check_word('rat', 'ACDLORT', 'R')
    False
    >>> check_word('told', 'ACDLORT', 'R')
    False
    >>> check_word('bee', 'ACDLORT', 'R')
    False
    """
    # Check if required letter is in the word
    if required not in word.upper():
        return False
    
    # Check if all letters in word are in available letters
    for letter in word.upper():
        if letter not in available:
            return False
        
    # Check if word contains at least 4 letters
    if len(word) < 4:
        return False
    return True

print(check_word('told', 'ACDLORT', 'R'))

def word_score(word, available):
    """Compute the score for an acceptable word.
    >>> word_score('card', 'ACDLORT')
    1
    >>> word_score('color', 'ACDLORT')
    5
    >>> word_score('cartload', 'ACDLORT')
    15
    """
    length = len(word)
    if length == 4:
        score = 1
    else:
        score = length
    if all(letter in word.upper() for letter in available):
        score += 7
    return score

print(word_score('cartload', 'ACDLORT'))


# function uses_all that uses function uses_only
def uses_only(word, available):
    """Returns True if all letters in word are in available."""
    for letter in word:
        if letter not in available:
            return False
    return True

def uses_all(word, required):
    """Checks whether a word avoids forbidden letters.
    >>> uses_none('banana', 'xyz')
    True
    >>> uses_none('apple', 'efg')
    False
    >>> uses_none('', 'abc')
    True"""
    for letter in required:
        if not uses_only(letter, word):
            return False
    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(uses_all('better', 'ter'))

# Test - er gebeurt niets als de test succesvol verlopen zijn, fail als test niet passeert