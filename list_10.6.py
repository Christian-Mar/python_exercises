def is_anagram(s1, s2):
    """Returns True if the two strings are anagrams, False otherwise."""
    return sorted(s1.lower()) == sorted(s2.lower())


if __name__ == "__main__":
    print(is_anagram("listen", "silent"))  # True
    print(is_anagram("hello", "world"))    # False
    print(is_anagram("Evil", "Vile"))      # True
