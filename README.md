# Sudoku
Sudoku solver written in Python 3.9.1. Includes functionality for reading a sudoku puzzle from a file, finding the solution if it exists, and determining whether that solution is unique. To execute, simply run main.py. This script will open and solve each sudoku puzzle in the data directory. Alternatively, the sudoku_solver.py module can be imported into other projects.

# Input Format
Input files must only contain the digits 0-9 and newlines. A value of zero indicates an empty grid cell.
```
604305201
000000000
015000760
000403002
002050100
700201000
026000810
000000000
503102604
```

# Example Usage
```
solver = SudokuSolver()
solver.init_grid_from_file(file_path)
solver.solve()
```
Using the example input data above, the following output is produced.
```
---------
674395281
238716459
915824763
851463972
362957148
749281536
426539817
197648325
583172694
---------
This sudoku has a unique solution.
```

# Implementation Details
The solve function uses a brute force recursive method of finding solutions. It works by going through the grid and every time a zero is encountered, setting it to each possible value and checking if the grid is still valid. If so, it calls the function recursively and continues searching for the next zero. When the grid becomes invalid, the recursion just unwinds and keeps going, eventually exhausting all possible solutions. The reason for using a brute force approach is for correctness/completeness. Although many sudoku puzzles are solvable by simple strategies (eg there is only one place in this box for a 1), advanced sudokus often require more complex strategies (eg x-wing, swordfish). And even if these advanced strategies were implemented, it would be difficult to determine if the algorithm was correct for every type of puzzle.
