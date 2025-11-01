def type_of_triangle(side1, side2, side3):
    """
    Classifies a triangle based on the lengths of its three sides.

    The function first checks if the given lengths can form a valid triangle
    based on the Triangle Inequality Theorem.

    Parameters
    ----------
    side1 : float
        Length of the first side.
    side2 : float
        Length of the second side.
    side3 : float
        Length of the third side.

    Returns
    -------
    str
        The type of triangle: 'Invalid (Non-positive sides)', 'Invalid (Triangle Inequality)',
        'Equilateral', 'Isosceles', or 'Scalene'.

    Author
    ------
    Christian Marginet

    Date
    ----
    November 1, 2025
    """
    if side1 == side2 == side3:
        print("Equillateral")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("Isosceles")
    else:
        print("Scalene")

if __name__ == "__main__":
    side1 = float(input("Please, give the length of the first side: "))
    side2 = float(input("Please, give the length of the second side: "))
    side3 = float(input("Please, give the length of the third side: "))
    type_of_triangle(side1, side2, side3)