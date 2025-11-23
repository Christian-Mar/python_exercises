def right_justify(s):
    """
    Prints the string with enough leading spaces so that the last letter
    of the string is in column 70 of the display.

    Args:
        s: The string to right-justify
    """
    num_spaces = 70 - len(s)
    print(' ' * num_spaces + s)


# Test de functie
if __name__ == "__main__":
    right_justify("Hello")
    right_justify("Python")
    right_justify("This is a test string")