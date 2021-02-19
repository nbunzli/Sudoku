from sudoku_solver import SudokuSolver
import time

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

solve_sudoku('../data/empty_grid.txt')
solve_sudoku('../data/15_clues_no_solution.txt')
solve_sudoku('../data/60_clues_144_solutions.txt')
solve_sudoku('../data/23_clues_1_solution.txt')
solve_sudoku('../data/25_clues_1_solution.txt')
solve_sudoku('../data/29_clues_1_solution.txt')
