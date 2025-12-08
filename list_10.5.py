def is_sorted(lst):
    """Returns True if the list is sorted in ascending order, False otherwise."""
    return lst == sorted(lst)


if __name__ == "__main__":
    print(is_sorted([1, 2, 2]))    # True
    print(is_sorted(['b', 'a']))   # False
