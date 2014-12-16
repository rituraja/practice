"""
A python Sudoku solver. Takes in a csv input grid and spits out the solution
to a csv prefixed with "solved_".

Run as:
$ python sudoku.py <filename.csv>

Author: Ritu Rathore
"""

import csv, sys
import pprint

# The sudoku grid - updated in-place with solution.
sudoku = [[] for x in xrange(9)]
# [
# [0,0,0,9,0,0,1,7,0],
# [0,0,4,0,3,0,8,0,5],
# [0,0,3,0,0,8,0,0,4],
# [7,0,9,6,0,0,0,0,8],
# [0,0,0,0,0,0,0,0,0],
# [8,0,0,0,0,5,7,0,2],
# [4,0,0,2,0,0,3,0,0],
# [1,0,7,0,5,0,6,0,0],
# [0,8,5,0,0,6,0,0,0]
# ]


def is_valid(row, col, value):
    """
    Returns false if given 'value' already exists in a given 'row' or 'col' or the mini 3 X 3 grid
    that contains the 'row', 'col'.
    """
    for i in xrange(9):
        if sudoku[row][i] == value: # check within row
            return False
        if sudoku[i][col] == value: # check within column
            return False

    # find top, left corner of the mini grid
    gridx = 3 * (row / 3)
    gridy = 3 * (col / 3)

    for grid_row in xrange(gridx, gridx + 3):
        for grid_col in xrange(gridy, gridy + 3):
            if sudoku[grid_row][grid_col] == value:
                return False

    return True # no dupe found

def next_empty_cell(row, col):
    """
    Returns the next cell (left to right) from 'sudoku' without a pre-filled value.
    """
    col = (col + 1) % 9
    row = (row + 1) if col == 0 else row
    try:
        if sudoku[row][col] != 0:
            return next_empty_cell(row, col)
        else:
            return row, col
    except Exception, e:
        return None, None

def find_solution(i = -1, j = -1):
    """
    The main solver function that solves the 'sudoku' starting at
    row i, column j onwards, excluding the cell i,j.

    Uses backtracking and stores the result in-place in 'sudoku global var.'
    """
    i, j = next_empty_cell(i, j)
    if (i is None or j is None):
        return True # found the solution!

    solved = False
    for val in xrange(1, 10):
        if is_valid(i, j, val):
            sudoku[i][j] = val
            # Now solve the sub-grid
            solved = find_solution(i, j)

    if not solved:
        sudoku[i][j] = 0 # cleanup after ourselves to retry
    return solved

def read_grid(filename):
    """
    Reads the sudoku grid from a csv file from 'filename' and stores it in
    'sudoku' global var.
    """
    with open(filename, "rb") as csvfile:
        csv_reader = csv.reader(csvfile)
        # TODO: Validate grid here.
        i = 0
        try:
            for row in csv_reader:
                for val in row:
                    sudoku[i].append(int(val))
                i += 1
        except csv.Error as e:
            sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))

def write_solution(filename):
    """
    Writes the sudoku solution grid to a csv file 'filename'.
    """
    with open(filename,'wb') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(sudoku)

def main(argv):
    if len(argv) != 2:
        print 'sudoku.py <filename.csv>'
        sys.exit(2)
    else:
        filename = argv[1]
    read_grid(filename)
    print "input sudoku puzzle:"
    pprint.pprint(sudoku)
    print "======================================"
    if find_solution():
        out_file = 'solved_' + filename
        print "Found solution. Writing to " + out_file
        pprint.pprint(sudoku)
        write_solution(out_file)
        print "======================================"
    else:
        print "Invalid Sudoku Puzzle! Couldn't find a solution."

if __name__ == '__main__':
    main(sys.argv)
