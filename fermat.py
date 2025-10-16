def control_fermat(a: int, b: int, c: int, n: int):
   
    if a**n + b**n == c**n and n > 2: # essential check of the theorem
        print("Holy smokes, Fermat was wrong!!")
    else:
        print("No, that doesn’t work.")

def ask_values(): # input values before the check
    
    a_str = input("Give an int (positive) for a: ")
    b_str = input("Give an int (positive) for b: ")
    c_str = input("Give an int (positive) for c: ")
    n_str = input("Give an int (positive) for n: ")
    
    a = int(a_str)
    b = int(b_str)
    c = int(c_str)
    n = int(n_str)
        
    control_fermat(a, b, c, n) # the result will be given by the print in control fermat function
    
ask_values() # start by giving the input