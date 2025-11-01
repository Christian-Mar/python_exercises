def eerste_dag_weekdag(jaar, maand):

    """
    Calculates the day of the week for the first day of a given month and year
    using Zeller's Congruence algorithm.

    The returned weekday is based on a list starting with 'Saturday' (0).

    Parameters
    ----------
    jaar : int
        The year (e.g., 2025).
    maand : int
        The month (1 for January, 12 for December).

    Returns
    -------
    str
        The name of the weekday for the first day of the specified month,
        in Dutch (e.g., 'zaterdag', 'maandag').

    Author
    ------
    Christian Marginer

    Date
    ----
    November 1, 2025
    """
    
    dagen = ['zaterdag', 'zondag', 'maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag']

    # Zeller gebruikt maanden: maart=3, ..., februari=14. Januari en februari worden als maand 13 en 14 van het vorige jaar gezien.
    if maand < 3:
        maand += 12
        jaar -= 1

    d = 1  # eerste dag van de maand
    k = jaar % 100  # jaar binnen eeuw
    j = jaar // 100  # eeuw

    # Berekening volgens Zeller:
    h = (d + (13*(maand + 1))//5 + k + (k//4) + (j//4) - 2*j) % 7

    return dagen[h]

# Voorbeeld:
print(eerste_dag_weekdag(2025, 10))  # Output: 'woensdag'