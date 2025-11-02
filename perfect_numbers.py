# Write a Python function to check whether a number is perfect or not. The function should return True if the number is perfect
# and False otherwise.
# Perfect numbers: https://www.britannica.com/science/perfect-number


def all_divisors(n):
    """
     This function returns all divisors of a number
    """
    divisors = []
    for x in range(1, int(n/2)+1):
        if n % x == 0:
            divisors.append(x)
    return divisors


def perfect_number(n):
    divs = all_divisors(n)
    if sum(divs) == n:
        return True
    else:
        return False


# calling the function
n = 28
if perfect_number(n):
    print(f'{n} is one rare of a kind number, it\'s a perfect number')
else:
    print(f'Nothing special about {n}, it\'s no perfect number')
