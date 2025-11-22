def calculate_gcd(a, b):
    """
    Calculates the Greatest Common Divisor (GCD) of two integers
    using the Euclidean algorithm.

    Parameters
    ----------
    a : int
        The first integer.
    b : int
        The second integer.

    Returns
    -------
    int
        The greatest common divisor of `a` and `b`.
        The result is always non-negative.

    Examples
    --------
    Basic example with common factors:
    >>> calculate_gcd(48, 18)
    6

    Example with prime numbers (coprime):
    >>> calculate_gcd(101, 13)
    1

    Example where one number is a multiple of the other:
    >>> calculate_gcd(50, 10)
    10

    Edge case: GCD with zero (returns the absolute of the non-zero number):
    >>> calculate_gcd(15, 0)
    15
    >>> calculate_gcd(0, 5)
    5

    Edge case: Negative numbers (GCD is always positive):
    >>> calculate_gcd(-48, 18)
    6
    >>> calculate_gcd(-48, -18)
    6

    Edge case: Both zero (mathematically 0):
    >>> calculate_gcd(0, 0)
    0
    """
    # Ensure inputs are positive to keep the result positive standard
    a, b = abs(a), abs(b)
    
    while b:
        a, b = b, a % b
        
    return a

# --- Code om de doctests automatisch te draaien ---
if __name__ == "__main__":
    import doctest
    print("Running doctests...")
    # verbose=True laat alle tests zien, ook de geslaagde
    doctest.testmod(verbose=True)

print(calculate_gcd(81, 27))