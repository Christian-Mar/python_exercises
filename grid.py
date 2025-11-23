def print_horizontal_line():
    """Prints a horizontal line of the grid."""
    print('+', end=' ')
    print('- - - -', end=' ')
    print('+', end=' ')
    print('- - - -', end=' ')
    print('+')


def print_vertical_line():
    """Prints a vertical line of the grid."""
    print('|', end=' ')
    print(' ' * 7, end=' ')
    print('|', end=' ')
    print(' ' * 7, end=' ')
    print('|')


def draw_grid():
    """Draws a 2x2 grid."""
    # Top border
    print_horizontal_line()

    # First row of cells
    for i in range(4):
        print_vertical_line()

    # Middle border
    print_horizontal_line()

    # Second row of cells
    for i in range(4):
        print_vertical_line()

    # Bottom border
    print_horizontal_line()


# Test de functie
if __name__ == "__main__":
    draw_grid()