def square(n):
    """
    Returns the square of a number.

    The tests are listed below. Doctest checks if the output 
    of the code matches what is expected here.

    >>> square(5)
    25

    >>> square(-3)
    9

    >>> square(0)
    0
    """
    # Calculation of the square
    return n * n

if __name__ == "__main__":
    import doctest
    
    print("Starting doctest...")
    doctest.testmod(verbose=True) # 'verbose=True' ensures you see details, even if the tests pass.