def uses_only(word, letters):
    """
    Check if a word uses only the letters from a given set.

    Parameters
    ----------
    word : str
        The word to check.
    letters : str
        The allowed letters.

    Returns
    -------
    bool
        True if word uses only letters from the letters string, False otherwise.

    Examples
    --------
    >>> uses_only('hello', 'helo')
    True
    >>> uses_only('hello', 'hel')
    False
    >>> uses_only('python', 'pythonxyz')
    True
    >>> uses_only('', 'abc')
    True

    Author
    ------
    Christian Marginet

    Date
    ----
    2025-11-22
    """
    for letter in word:
        if letter not in letters:
            return False
    return True


def uses_all(word, letters):
    """
    Check if a word uses all the letters from a given set.

    This function uses the uses_only function to check whether all letters
    in the letters string appear in the word (repeats are allowed).

    Parameters
    ----------
    word : str
        The word to check.
    letters : str
        The required letters that should all appear in the word.

    Returns
    -------
    bool
        True if word uses all letters from the letters string, False otherwise.

    Examples
    --------
    >>> uses_all('hello', 'hel')
    True
    >>> uses_all('hello', 'helo')
    True
    >>> uses_all('hello', 'heloz')
    False
    >>> uses_all('python programming', 'python')
    True
    >>> uses_all('test', 'testing')
    False

    Author
    ------
    Christian Marginet

    Date
    ----
    2025-11-22
    """
    return uses_only(letters, word)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

print(uses_all('beter', 'bart'))