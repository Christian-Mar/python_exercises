def cumsum(t):
    
    cumulative_sums = []
    running_total = 0
    
    # Iterate through each number in the input list 't'
    for number in t:
        # Update the running total
        running_total += number
        
        # Append the current running total (the cumulative sum up to this point)
        # to the new list
        cumulative_sums.append(running_total)
        
    return cumulative_sums

# Example usage:
t = [1, 2, 3]
result = cumsum(t)
print(result)

# Another example:
t2 = [4, 1, 5, 2]
result2 = cumsum(t2)
print(f"\nExample 2: Input: {t2}, Output: {result2}")

# onliner: return [sum(t[:i+1]) for i in range(len(t))]
