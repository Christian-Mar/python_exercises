def middle(lst):
    """Returns a new list containing all but the first and last elements."""
    return lst[1:-1]


if __name__ == "__main__":
    t = [1, 2, 3, 4]
    print(middle(t))  # [2, 3]
