from sudoku_solver import SudokuSolver
import time
import os

# Example of using the SudokuSolver class to read a puzzle from a file and solve it.
# Also reports the execution time of the solve function.
def solve_sudoku(file_path: str) -> None:
	print(f'Solving sudoku at file path: {file_path}')
	solver = SudokuSolver()
	solver.init_grid_from_file(file_path)
	solver.print_grid()

	start_time = time.time()
	solver.solve()
	end_time = time.time()

	print(f'Solve function execution time: {end_time - start_time} seconds')
	print('*****************************************************************')
	print('*****************************************************************')


# Run the solver for each file in the data directory
directory_path = '../data/'
for filename in os.listdir(directory_path):
	solve_sudoku(directory_path + filename)
