import sudoku

"""Unit tests for the Sudoku solver.
"""
__author__ = 'Alain Kaegi'


def test_create_location():
    assert sudoku.create_location(7, 4) == (7, 4)

def test_find_row():
    expected = [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 6), (2, 7), (2, 8)]
    assert sudoku.find_row((2, 5)) == expected

def test_find_column():
    expected = [(0, 5), (1, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5)]
    assert sudoku.find_column((2, 5)) == expected

def test_find_block():
    expected = [(0, 6), (0, 7), (0, 8), (1, 6), (1, 7), (1, 8), (2, 7), (2, 8)]
    assert sudoku.find_block((2, 6)) == expected

def test_create_squares():
    # We're not checking everything here, just looking at a couple of
    # elements.
    grid = sudoku.create_squares()

    assert grid[8][3].value == 0

    row = grid[6][1].row
    assert row[0] is grid[6][0]

    col = grid[4][0].column
    assert col[6] is grid[7][0]

    blk = grid[3][7].block
    assert blk[2] is grid[4][6]

def test_grid_to_string():
    grid = sudoku.create_squares()
    grid[0][1].value = 1
    grid[1][8].value = 8
    grid[7][4].value = 5
    correct = ('.1.......\n'
               '........8\n'
               '.........\n'
               '.........\n'
               '.........\n'
               '.........\n'
               '.........\n'
               '....5....\n'
               '.........\n')
    assert sudoku.__str__(grid) == correct

def test_string_to_grid():
    correct = ('.1.......\n'
               '........8\n'
               '.........\n'
               '.........\n'
               '.........\n'
               '.........\n'
               '.........\n'
               '....5....\n'
               '.........\n')
    grid = sudoku.create_squares(correct)
    assert sudoku.__str__(grid) == correct

def test_find_valid_numbers():
    diagram = ('.........\n'
               '..2....4.\n'
               '.......7.\n'
               '......8..\n'
               '...3....1\n'
               '........5\n'
               '.........\n'
               '6..2.....\n'
               '.......9.\n')
    grid = sudoku.create_squares(diagram)
    s = grid[4][7]
    correct = [False, False, True, False, False, False, True, False, False, False]
    answer = sudoku.find_valid_numbers(s)
    answer[0] = False  # The value of answer[0] is irrelevant, force it to False
    assert answer == correct

def test_rejects_unsolvable_puzzle():
    diagram = ('.12345678\n'
               '2........\n'
               '3........\n'
               '4........\n'
               '5........\n'
               '6........\n'
               '7........\n'
               '8........\n'
               '9........\n')
    grid = sudoku.create_squares(diagram)
    assert sudoku.solve(grid) == False

def test_find_one_missing_square():
    # This puzzle adapted from www.puzzles.ca/sudoku/
    diagram = ('897312456\n'
               '613594728\n'
               '425678913\n'
               '941867532\n'
               '538921647\n'
               '276435.91\n'
               '359186274\n'
               '764253189\n'
               '182749365\n')
    grid = sudoku.create_squares(diagram)
    assert sudoku.solve(grid) == True
    correct = ('897312456\n'
               '613594728\n'
               '425678913\n'
               '941867532\n'
               '538921647\n'
               '276435891\n'
               '359186274\n'
               '764253189\n'
               '182749365\n')
    assert sudoku.__str__(grid) == correct

def test_find_two_missing_squares():
    # This puzzle adapted from www.puzzles.ca/sudoku/
    diagram = ('897312456\n'
               '6135..728\n'
               '425678913\n'
               '941867532\n'
               '538921647\n'
               '276435891\n'
               '359186274\n'
               '764253189\n'
               '182749365\n')
    grid = sudoku.create_squares(diagram)
    assert sudoku.solve(grid) == True
    correct = ('897312456\n'
               '613594728\n'
               '425678913\n'
               '941867532\n'
               '538921647\n'
               '276435891\n'
               '359186274\n'
               '764253189\n'
               '182749365\n')
    assert sudoku.__str__(grid) == correct

def test_solve_easy_puzzle():
    # This puzzle from www.puzzles.ca/sudoku/
    diagram = ('.97..24..\n'
               '....9..28\n'
               '4.567..1.\n'
               '.....7...\n'
               '.3.......\n'
               '..6..5.9.\n'
               '...1....4\n'
               '764......\n'
               '18....36.\n')
    grid = sudoku.create_squares(diagram)
    assert sudoku.solve(grid) == True
    correct = ('897312456\n'
               '613594728\n'
               '425678913\n'
               '941867532\n'
               '538921647\n'
               '276435891\n'
               '359186274\n'
               '764253189\n'
               '182749365\n')
    assert sudoku.__str__(grid) == correct

def test_solve_hard_puzzle():
    # This puzzle from www.puzzles.ca/sudoku/
    diagram = ('...6.2..3\n'
               '..3......\n'
               '..8..7.91\n'
               '6........\n'
               '.12.5.7..\n'
               '.....49..\n'
               '..5.3....\n'
               '.3.5....8\n'
               '7....1.6.\n')
    grid = sudoku.create_squares(diagram)
    assert sudoku.solve(grid) == True
    correct = ('571692483\n'
               '943815627\n'
               '268347591\n'
               '659723814\n'
               '412958736\n'
               '387164952\n'
               '825436179\n'
               '136579248\n'
               '794281365\n')
    assert sudoku.__str__(grid) == correct