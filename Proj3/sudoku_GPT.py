class Square:
    """A `Square` consists of 4 attributes.

    `value` is an integer value between 0 and 9, inclusive. 0 means
    empty, otherwise `value` indicates the value currently assigned to
    the corresponding location in the grid.

    `row` is an array of 8 references to all the `Square` neighbors in
    the same row as this Square.

    `column` is the same as `row` but for neighbors in the same column.

    `block` is the same as `row` but for neighbors in the same block.
    """
    pass

def main() -> None:
    """Prints the solution to the puzzle in the specified file."""
    with open('sudoku1.txt') as file:
        puzzle = file.read()
    grid = create_squares(puzzle)
    if solve(grid):
        print(__str__(grid))
    else:
        print("No solution exists.")

def create_location(row: int, col: int) -> tuple[int, int]:
    """Returns with the specified `row` and `column` as a 2-tuple."""
    return (row, col)

def find_row(here: tuple[int, int]) -> list[tuple[int, int]]:
    """Returns an array of the eight `location`s in the same row as `here`."""
    return [create_location(here[0], i) for i in range(9) if i != here[1]]

def find_column(here: tuple[int, int]) -> list[tuple[int, int]]:
    """Returns an array of the eight `location`s in the same column as `here`."""
    return [create_location(i, here[1]) for i in range(9) if i != here[0]]

def find_block(here: tuple[int, int]) -> list[tuple[int, int]]:
    """Returns an array of the eight `location`s in the same 3x3 block as `here`."""
    r_start = (here[0] // 3) * 3
    c_start = (here[1] // 3) * 3
    return [create_location(r, c) for r in range(r_start, r_start + 3)
                                    for c in range(c_start, c_start + 3)
                                    if (r, c) != here]

def create_squares(diagram: str = None) -> list[list[Square]]:
    """Returns a 9x9 array of instances of `Square` objects."""
    grid = []
    for r in range(9):
        row = []
        for c in range(9):
            s = Square()
            s.value = int(diagram[r * 9 + c]) if diagram and diagram[r * 9 + c].isdigit() else 0
            row.append(s)
        grid.append(row)

    # Set neighbors for each square
    for r in range(9):
        for c in range(9):
            square = grid[r][c]
            square.row = find_row((r, c))
            square.column = find_column((r, c))
            square.block = find_block((r, c))

    return grid

def __str__(grid: list[list[Square]]) -> str:
    """Returns a string representing `grid`, showing the numbers (or . for empty)."""
    return '\n'.join(' '.join(str(square.value) if square.value != 0 else '.' for square in row) for row in grid)

def find_valid_numbers(square: Square) -> list[bool]:
    """Returns a boolean array of length 10 indicating valid numbers for the square."""
    valid = [True] * 10
    for neighbor in square.row + square.column + square.block:
        if neighbor.value != 0:
            valid[neighbor.value] = False
    return valid

def solve(grid: list[list[Square]]) -> bool:
    """Returns true if `grid` can be solved."""
    for r in range(9):
        for c in range(9):
            if grid[r][c].value == 0:  # Find an empty square
                for num in range(1, 10):  # Try numbers 1 to 9
                    grid[r][c].value = num
                    if find_valid_numbers(grid[r][c])[num]:  # Check if valid
                        if solve(grid):  # Recursively solve the rest
                            return True
                    grid[r][c].value = 0  # Reset if not valid
                return False  # No valid number found
    return True  # Solved

if __name__ == '__main__':
    main()