# Oefening 3: is een woord een anagram (met dezelfde letters een ander woord vormen)

def is_anagram(word1, word2):
    """
    Check if two words are anagrams of each other.
    
    An anagram is formed by rearranging the letters of a word to create
    a different word, using all the original letters exactly once.
    Case differences are ignored.
    
    Args:
        word1 (str): The first word
        word2 (str): The second word
        
    Returns:
        bool: True if the words are anagrams, False otherwise
        
    Examples:
        >>> is_anagram("listen", "silent")
        True
        >>> is_anagram("Listen", "Silent")
        True
        >>> is_anagram("hello", "world")
        False
        >>> is_anagram("anagram", "nagaram")
        True
        >>> is_anagram("rat", "car")
        False
        >>> is_anagram("abc", "cba")
        True
        >>> is_anagram("a", "a")
        True
        >>> is_anagram("", "")
        True
        >>> is_anagram("abc", "abcd")
        False
    """
    normalized_word1 = word1.lower()
    normalized_word2 = word2.lower()
    
    if len(normalized_word1) != len(normalized_word2):
        return False
    
    for char in normalized_word1:
        if normalized_word1.count(char) != normalized_word2.count(char):
            return False
    
    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()

print(is_anagram("droom", "moord"))

def find_anagram(filename):
    with open(filename, 'r') as file:
        for line in file:
            word1 = line.strip().lower()
            word2 = line.strip().lower()
            if len(word1) != len(word2):
                return False
    
            for char in word1:
                if word1.count(char) != word2.count(char):
                    return False
    
    return True

if __name__ == "__main__":
    result = find_anagram("words.txt")
    print(result)




# Anagram van gegeven woord opzoeken in words.txt
def find_anagrams_in_file(word, filename):
    anagrams = []
    
    with open(filename, 'r') as file:
        for line in file:
            file_word = line.strip().lower()
            normalized_word = word.lower()
            
            if len(file_word) != len(normalized_word):
                continue
            
            if file_word == normalized_word:
                continue
            
            is_anagram = True
            for char in normalized_word:
                if normalized_word.count(char) != file_word.count(char):
                    is_anagram = False
                    break
            
            if is_anagram:
                anagrams.append(file_word)
    
    return anagrams


if __name__ == "__main__":
    word = "donaban"
    result = find_anagrams_in_file(word, "words.txt")
    if result:
        print(f"Anagrams of '{word}': {result}")
    else:
        print(f"No anagrams of '{word}' found.")