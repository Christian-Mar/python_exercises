def nested_sum(t):
    """
    Takes a list of lists of integers and adds up the elements from all of the nested lists.

    Args:
        t: A list of lists of integers (e.g., [[1, 2], [3], [4, 5, 6]]).

    Returns:
        The total sum of all elements in the nested lists.
    """
    total = 0
    # Iterate through each inner list in the outer list 't'
    for inner_list in t:
        # Iterate through each number in the current inner list
        for number in inner_list:
            # Add the number to the running total
            total += number
    return total

# Example usage:
t = [[1, 2], [3], [4, 5, 6]]
result = nested_sum(t)

print(result)

