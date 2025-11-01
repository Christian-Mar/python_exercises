def eerste_dag_weekdag(jaar, maand):
    """
    Geeft de weekdag van de eerste dag van de opgegeven maand en jaar (Zeller’s Congruence).
    Retourneert een string met de weekdag (bijv. 'maandag').
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