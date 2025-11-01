def generate_divisors():
    
    user_input = int(input("Voer een positief geheel getal in (groter dan 1): "))
    
    for i in range(user_input):

        divisors = []
        
        for j in range(1, user_input + 1): # user_input + 1 to include given number as the range counts in indexes
            if user_input % j == 0:
                divisors.append(j)         

    print(f"{divisors}")

if __name__ == "__main__":
    generate_divisors()
    

def generate_divisors_optimized():
    
    user_input = int(input("Voer een positief geheel getal in (groter dan 1): "))
    
    for i in range(user_input):

        divisors = [1] # het getal is altijd deelbaar door één
        
        for j in range(2, user_input // 2 + 1): # vanaf 2, gezien we 1 al hebben, tot en met de helft
            if user_input % j == 0:
                divisors.append(j)    

        divisors.append(user_input) # het getal is altijd deelbaar door zichzelf         

    print(f"{divisors}")

if __name__ == "__main__":
    generate_divisors_optimized()