def factorial_recursive(n):
    """Calculates the factorial of a non-negative integer using recursion."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    # Base case: The recursion stops here
    if n == 1:
        return 1
    
    # Recursive step: Call the function again with n-1
    else:
        if n < 995:
            return n * factorial_recursive(n - 1)
        else: 
            pass

number = 5
print(f"The factorial of {number} is {factorial_recursive(number)}")