def has_duplicates(lst):
    """Returns True if any element appears more than once. Does not modify the list."""
    for element in lst:
        if lst.count(element) > 1:
            return True
    return False


if __name__ == "__main__":
    print(has_duplicates([1, 2, 3, 4]))    # False
    print(has_duplicates([1, 2, 2, 4]))    # True
    print(has_duplicates(['a', 'b', 'a'])) # True
