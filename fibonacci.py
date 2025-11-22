def print_fibonacci_sequence(max_value):
    # Initialize variables
    a, b = 0, 1
    
    print(f"Fibonacci sequence up to {max_value}:")
    
    # Generate and print inside the loop
    while a <= max_value:
        print(a) # Print the value immediately
        
        # Calculate the next value
        a, b = b, a + b

# --- Usage ---
print_fibonacci_sequence(1000)