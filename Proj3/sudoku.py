"""The Sudoku solver."""

__author__ = 'Zach Martin'
__author__ = 'Askar Takhirov'

class Square:
    """A `Square` consists of 4 attributes.

    `value` is an integer value between 0 and 9, inclusive.  0 means
    empty, otherwise `value` indicates the value currently assigned to
    the corresponding location in the grid.

    `row` is an array of 8 references to all the `Square` neighbors in
    the same row as the this Square.

    `column` is the same as `row` but for neighbors in the same column.

    `block` is the same as `row` but for neighbors in the same block.

    Note: don't edit this class definition.

    """
    pass

def main() -> None:
    """Prints the solution to the puzzle in the specified file."""

    with open('sudoku1.txt') as file:
        puzzle = file.read()
    grid = create_squares(puzzle)
    solve(grid)
    print(__str__(grid))

def create_location(row : int, col : int) -> tuple[int, int]:
    """Returns with the specified `row` and `column` as a 2-tuple also called an
    ordered pair."""
    return (row, col)

def find_row(here : tuple[int, int]) -> list[tuple[int, int]]:
    """Returns an array of the eight `location`s (represented by ordered pairs)
    in the same row as `here` (represented by an ordered pair)."""
    lst = []
    for i in range(9):
        if i == here[1]:
            continue
        lst.append(create_location(here[0], i))
    return lst

def find_column(here : tuple[int, int]) -> list[tuple[int, int]]:
    """Returns an array of the eight `location`s (represented by ordered pairs)
    in the same column as `here` (represented by an ordered pair)."""
    lst = []
    for i in range(9):
        if i == here[0]:
            continue
        lst.append(create_location(i, here[1]))
    return lst

def find_block(here : tuple[int, int]) -> list[tuple[int, int]]:
    """Returns an array of the eight `location`s (represented by ordered pairs)
    in the same 3x3 block as `here` (represented by an ordered pair)."""
    r = here[0] - here[0]%3
    c = here[1] - here[1]%3
    
    lst = []
    for i in range(r, r+3):
        for j in range (c, c+3):
            if i == here[0] and j == here[1]:
                continue
            lst.append(create_location(i,j))
    return lst

def create_squares(diagram : str = None) -> list[list[Square]]:
    """Returns a 9x9 array of instances of `Square` objects.  Recall that
    each `Square` has 4 attributes.  The attributes are `value`,
    `row`, `column`, and `block`.  The first attribute is the value
    assigned to the associated position in the grid.  The other three
    attributes are references to all the 3*8 neighbors in the same
    row, in the same column, and in the same block as this location.

    If argument `diagram` is None, then all the values are set to 0.
    Otherwise, the values are set according to the diagram (empty
    squares are represented with value 0).  The optional argument
    `diagram` is a string with numbers to be filled in the grid, or
    dots to represent empty squares, or optional newlines to enhance
    readability when printed."""

    grid = [[Square() for _ in range(9)] for _ in range(9)]

    # Initialize square attributes
    for r in range(9):
        for c in range(9):
            s = grid[r][c]
            s.value = 0
            s.row = [None] * 8
            s.column = [None] * 8
            s.block = [None] * 8

    # Populate the grid with values from the diagram
    if diagram:
        lines = diagram.strip().split('\n')  # Split by lines
        for r in range(9):
            for c in range(9):
                if lines[r][c].isdigit():
                    value = int(lines[r][c])
                else:
                    value = 0
                grid[r][c].value = value

    # Set neighbors for each square
    for r in range(9):
        for c in range(9):
            s = grid[r][c]
            s.row = [grid[r][i] for i in range(9) if i != c]
            s.column = [grid[i][c] for i in range(9) if i != r]
            s.block = [grid[i][j] for i in range((r // 3) * 3, (r // 3) * 3 + 3)
                                           for j in range((c // 3) * 3, (c // 3) * 3 + 3)
                                           if (i, j) != (r, c)]

    return grid

def __str__(grid : list[list[Square]]) -> str:
    """Returns a string representing `grid`, showing the numbers (or . for
    square with value 0)."""

    return '\n'.join(
        ''.join(str(square.value) if square.value != 0 else '.' for square in row)
        for row in grid
    ) + '\n'  # Add a newline at the end for consistency
    # TODO You have to write this
    return None

def find_valid_numbers(square : Square) -> list[bool]:
    """Returns a boolean array of length 10.  For each digit, the
    corresponding entry in the array is `True` if that number does not
    appear elsewhere in the `Square`'s row, column, or block."""
    valid_numbers = [True] * 10  # Index 0-9, where 0 is ignored
    
    # Check row, column, and block for existing numbers
    for neighbor in square.row + square.column + square.block:
        if neighbor.value != 0:  # Ignore empty squares
            valid_numbers[neighbor.value] = False
            
    return valid_numbers
    # TODO You have to write this

def solve(grid : list[list[Square]]) -> bool:
    """Returns true if `grid` can be solved. If so, `grid` is modified to fill
    in that solution."""
    
    for r in range(9):
        for c in range(9):
            if grid[r][c].value == 0:  # Found an empty square
                # Try numbers 1 to 9
                for num in range(1, 10):
                    grid[r][c].value = num  # Place the number
                    valid_numbers = find_valid_numbers(grid[r][c])
                    
                    if valid_numbers[num]:  # If the number is valid
                        if solve(grid):  # Recursively try to solve the rest of the grid
                            return True  # Found a solution
                        
                    grid[r][c].value = 0  # Backtrack if not valid
                
                return False  # No valid number could be placed in this square
    
    return True  # No empty squares left; the puzzle is solved

    # TODO You have to write this
    # Here's an outline of the algorithm:
    # for each square
    #     if its value is 0
    #         for each valid number that could be filled in
    #             if you can solve the rest of the grid
    #                 return True
    #         nothing worked: set value back to 0 and return False
    # no squares left to fill in: return true

if __name__ == '__main__':
    main()
