def chop(lst):
    """Modifies the list by removing the first and last elements. Returns None."""
    del lst[0]
    del lst[-1]


if __name__ == "__main__":
    t = [1, 2, 3, 4]
    chop(t)
    print(t)  # [2, 3]
