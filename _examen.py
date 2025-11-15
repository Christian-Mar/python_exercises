# docstring (Zweller-formule) -> schrijf er ook testen in: 

import doctest

def first_day_weekday(year, month):
    """
    Calculates the day of the week for the first day of a given month and year
    using Zeller's Congruence algorithm.

    The returned weekday is based on a list starting with 'Saturday' (0).

    Parameters
    ----------
    year : int
        The year (e.g., 2025).
    month : int
        The month (1 for January, 12 for December).

    Returns
    -------
    str
        The name of the weekday for the first day of the specified month, in English
        (e.g., 'Saturday', 'Monday').

    Author
    ------
    Christian Marginet

    Date
    ----
    November 24th, 2025

    Examples
    --------
    >>> first_day_weekday(2025, 10)
    'Wednesday'
    >>> first_day_weekday(2024, 1)
    'Monday'
    >>> first_day_weekday(2023, 7)
    'Saturday'
    """
    days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    # Zeller's algorithm works with March=3, ..., February=14.
    # January and February are months 13 and 14 of the previous year.
    if month < 3:
        month += 12
        year -= 1

    d = 1  # first day of the month
    k = year % 100  # year within century
    j = year // 100  # century

    # Zeller's calculation:
    h = (d + (13 * (month + 1)) // 5 + k + (k // 4) + (j // 4) - 2 * j) % 7

    return days[h]

assert first_day_weekday(2023, 7) == 'Saturday' # other test method

if __name__ == "__main__":
    
    doctest.testmod()
    print(first_day_weekday(1972, 2))  # Output: 'Wednesday'


# check letters in txt-file

def count_vowels_in_file(filename):
    """
    Counts the occurrences of each vowel in a text file.
    
    Parameters
    ----------
    filename : str
        Path to the text file
    
    Returns
    -------
    None
        Prints the number of times each vowel appears
    """
    a_count = 0
    e_count = 0
    i_count = 0
    o_count = 0
    u_count = 0

    with open(filename, "r") as f:
        for line in f:
            for char in line:
                if char == 'a' or char == 'A':
                    a_count += 1
                elif char == 'e' or char == 'E':
                    e_count += 1
                elif char == 'i' or char == 'I':
                    i_count += 1
                elif char == 'o' or char == 'O':
                    o_count += 1
                elif char == 'u' or char == 'U':
                    u_count += 1

    print("a:", a_count)
    print("e:", e_count)
    print("i:", i_count)
    print("o:", o_count)
    print("u:", u_count)

if __name__ == "__main__":
    count_vowels_in_file("quote.txt")

# Lees volledig bestand

with open("quote.txt", "r") as file:
    content= file.read()

print(content)

# functies in functies 

def binnenfunctie(b):
    return b * 2

def buitenfunctie(a):
    return binnenfunctie(a) + 1

print(buitenfunctie(3))

# loops in loops

for i in range(1):
    for j in range(2):
        print("i: ", i, "j: ", j) # j is second loop in loop i - for every i all j's are given

def nested_loop_pairs(major_loop_number, minor_loop_number):
    """
    Generates pairs (i, j) for i in range(5) and j in range(3).
    
    Returns
    -------
    list of tuples
        Each tuple contains (i, j)
    """
    result = []
    for i in range(major_loop_number):
        for j in range(minor_loop_number):
            result.append((i, j))
    return result

# Gebruik buiten de functie:
print("*" * 15)
for pair in nested_loop_pairs(3, 2):
    print("i: ", pair[0], "j: ", pair[1])

# for loop with string

for i in 'loop':
    print(i)

# recursion

def print_n_times(word, n):
    if n > 0:
        print(word)
        print_n_times(word, n-1)

print_n_times('Hello', 3)

def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

recurse(5, 2) # bij n == 5, s == 7 --- bij n == 4, s == 11 --- bij n == 3, s == 14 --- bij n == 2, s == 16 --- bij n == 1, s == 17 --- bij n == 0 wordt s geprint
recurse(2, 2)

def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n - 1)
        return n * recurse

print(factorial(5))

# logische poorten
# Push naar github - Pull/Fetch from github -> clone bij eerste keer