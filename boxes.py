def print_edge_line():
    for i in range(2):
        print("+", end="")
        print("-" * 4, end="")
    print("+")

def print_box_line():
    for j in range(4):
        for i in range(2):
            print("|", end="")
            print(" " * 4, end="")
        print("|")

def draw_boxes(): 
    print_edge_line()

    for i in range(2):
        print_box_line()
        print_edge_line()

def main(): 
    draw_boxes()

if "__name__" == "__main__":
    main()

main() # executed function


