import random


def has_duplicate(lst):
    """Returns True if any element appears more than once."""
    return len(lst) != len(set(lst))


def generate_birthdays(n):
    """Generates a list of n random birthdays (day of year 1-365)."""
    return [random.randint(1, 365) for _ in range(n)]


def estimate_probability(num_students, num_simulations):
    """Estimates the probability of a birthday match in a group."""
    matches = 0
    for _ in range(num_simulations):
        birthdays = generate_birthdays(num_students)
        if has_duplicate(birthdays):
            matches += 1
    return matches / num_simulations


if __name__ == "__main__":
    num_students = 23
    num_simulations = 10000

    probability = estimate_probability(num_students, num_simulations)
    print(f"With {num_students} students and {num_simulations} simulations:")
    print(f"Probability of shared birthday: {probability:.2%}")
