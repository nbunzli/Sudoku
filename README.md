# Sudoku
Sudoku solver written in Python 3.9.1. Includes functionality for reading a sudoku puzzle from a file, finding the solution if it exists, and determining whether that solution is unique.

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
