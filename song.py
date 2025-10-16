def repeat(word, n):
    print(word * n)

spam = "Spam, "


def first_two_lines():
    repeat(spam, 4)
    repeat(spam, 4)



def last_three_lines():
    repeat(spam, 2)
    print("Hello there")
    repeat(spam, 3)

def print_verse():
    first_two_lines()
    last_three_lines()



# for i in range(2):
#    print_verse()

def print_n_verses(n):
    for i in range(n):
        print_verse()

# print_n_verses(3)

def letterdriehoek(letter, rijen):
   
    for i in range(rijen):
        print(letter * (i + 1))

#letterdriehoek('x', 14)

def letterrechthoek(letter, hoogte, breedte):

    for i in range(hoogte):
        print(letter * breedte)

#letterrechthoek('x', 5, 7)

def beersong():
    for n in range(99, 0,-1):
        print(f"{n} bottles of beer on the wall") 
        print(f"{n} bottles of beer")
        print("Take one down, pass it around")

# beersong()

def cross(n):
    cross= n * "+ "
    print(cross)

def horizontal(n):
    horizontal = n * "- "
    print(horizontal)

def vertical(n):
    vertical = n * "| \n"
    print(vertical)

def rectangle(height, width):
    baseline = "+ " + (width - 2) * "- " + "+ "
    vertical_line = ((height - 1) * ("| " + (width  - 2) * "  " + "| \n")) + ("| " + (width  - 2) * "  " + "|")
    print(baseline)
    print(vertical_line)
    print(baseline)

rectangle(9, 7)


