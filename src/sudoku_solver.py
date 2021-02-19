# This class provides functionality for solving sudoku puzzles, in which a partially filled 
# 9x9 grid of numbers is given and the task is to fill in the rest of the grid cells without
# duplicating any numbers in a row, column, or 3x3 box.
class SudokuSolver:

	# For sudoku grids which have multiple solutions, the solve function will stop after reaching
	# this limit. Be careful when modifying this, since empty or sparsely populated grids can have
	# a huge number of solutions.
	solution_limit = 2

	def __init__(self):
		self.grid = []
		self.solutions = -1

	# String must be completely numeric with length 81, no newlines or other whitespace.
	# The first nine numbers refer to the first row, the second nine refer to the second row, etc.
	# Zero is used to indicate an empty grid cell.
	# Example: 050079000000000500092000060080000407020600010070250080000040000008020000730001000
	def init_grid_from_string(self, grid_string: str) -> None:
		self.grid = []
		assert len(grid_string) == 81, 'Input string must be of length 81'
		for s in grid_string:
			assert s.isnumeric(), 'Input string must only contain digits 0-9'
			self.grid.append(int(s))

	# File can contain only numbers and newlines, no other whitespace.
	# The first nine numbers refer to the first row, the second nine refer to the second row, etc.
	# Zero is used to indicate an empty grid cell.
	# Example:
	# 050079000
	# 000000500
	# 092000060
	# 080000407
	# 020600010
	# 070250080
	# 000040000
	# 008020000
	# 730001000
	def init_grid_from_file(self, file_path: str) -> None:
		grid_string = ''
		with open(file_path, 'r') as file:
			grid_string = file.read().replace('\n', '')
		self.init_grid_from_string(grid_string)

	# Returns the value of the specified grid cell.
	# Note that there is no bounds checking, so index out of range exceptions are possible.
	# Due to the high number of calls to this function, bounds checking was causing a noticeable
	# increase in execution time.
	def get_cell(self, row: int, column: int) -> int:
		index = (row * 9) + column
		return self.grid[index]

	# Sets the value of the specified grid cell.
	# Note that there is no bounds checking, so index out of range exceptions are possible.
	# Due to the high number of calls to this function, bounds checking was causing a noticeable
	# increase in execution time.
	def set_cell(self, row: int, column: int, value: int) -> None:
		index = (row * 9) + column
		self.grid[index] = value

	# The following three functions are very similar. An attempt was made to share some of the code
	# by assembling the row, column, or box into a list and passing it to another function which 
	# detected duplicates. However this solution was slower, so the decision was made to use this
	# faster but less pretty method.

	# Returns true if there are no duplicates in this row (except zero).
	def is_row_valid(self, row: int) -> bool:
		value_flags = [False] * 9
		for column in range(9):
			cell_value = self.get_cell(row, column)
			if cell_value != 0:
				if value_flags[cell_value - 1]:
					return False
				value_flags[cell_value - 1] = True
		return True

	# Returns true there are no duplicates in this column (except zero).
	def is_column_valid(self, column: int) -> bool:
		value_flags = [False] * 9
		for row in range(9):
			cell_value = self.get_cell(row, column)
			if cell_value != 0:
				if value_flags[cell_value - 1]:
					return False
				value_flags[cell_value - 1] = True
		return True

	# Returns true if there are no duplicates in this box (except zero).
	def is_box_valid(self, box: int) -> bool:
		# Box 0 is rows 0-2, columns 0-2.
		# Box 1 is rows 0-2, columns 3-5.
		# Box 2 is rows 0-2, columns 6-8.
		# Box 3 is rows 3-5, columns 0-2. Etc.
		row_begin = 3 * int(box / 3)
		column_begin = 3 * int(box % 3)
		value_flags = [False] * 9
		for row in range(row_begin, row_begin + 3):
			for column in range(column_begin, column_begin + 3):
				cell_value = self.get_cell(row, column)
				if cell_value != 0:
					if value_flags[cell_value - 1]:
						return False
					value_flags[cell_value - 1] = True
		return True

	# Returns true if there are no duplicates in if this cell's row, column, or box (except zero).
	def is_cell_valid(self, row: int, column: int) -> bool:
		box = (3 * int(row / 3)) + (int(column / 3))
		if (not self.is_row_valid(row) or
			not self.is_column_valid(column) or
			not self.is_box_valid(box)):
			return False
		return True

	# Finds solutions to the sudoku grid, if they exist. Prints any solutions that are found.
	# The solution is not stored, ie after execution the grid will be back in the unsolved state.
	def solve(self) -> None:
		self.solutions = 0
		self.__solve_recursive()
		self.print_solution_count()

	# This is where the main solve logic is. It is a brute force recursive method of finding
	# solutions. It works by going through the grid and every time a zero is encountered,
	# setting it to each possible value and checking if the grid is still valid. If so,
	# it calls the function recursively and continues searching for the next zero.
	# When the grid becomes invalid, the recursion just unwinds and keeps going, eventually
	# exhausting all possible solutions. The reason for using a brute force approach is 
	# for correctness/completeness. Although many sudoku puzzles are solvable by simple 
	# strategies (eg there is only one place in this box for a 1), advanced sudokus often
	# require more complex strategies (eg x-wing, swordfish). And even if these advanced
	# strategies were implemented, it would be difficult to determine if the algorithm was
	# correct for every type of puzzle.
	def __solve_recursive(self) -> None:
		if self.solutions >= self.solution_limit:
			return
		for row in range(9):
			for column in range(9):
				if self.get_cell(row, column) == 0:
					# Found a zero. Now try setting it to each digit 1-9.
					for value in range(1, 10):
						self.set_cell(row, column, value)
						if self.is_cell_valid(row, column):
							# This digit is valid. Now recursively keep solving.
							self.__solve_recursive()
					# Revert the cell to zero before returning.
					self.set_cell(row, column, 0)
					return
		# If it got here, the puzzle is complete (no zeros left in the grid).
		self.solutions += 1
		self.print_grid()

	# Prints the contents of the grid, with newlines after each row.
	def print_grid(self) -> None:
		print('---------')
		if not self.grid:
			print('No grid data present, call init_grid_from_string or init_grid_from_file.')
			return
		for row in range(9):
			row_cells = ''
			for column in range(9):
				row_cells += str(self.get_cell(row, column))
			print(row_cells)
		print('---------')

	# Prints information on the solution count, ie whether a solution exists or is unique.
	def print_solution_count(self) -> None:
		if self.solutions == -1:
			print('Solution count unknown, solve has not been called yet.')
		elif self.solutions == 0:
			print('This sudoku has no solution.')
		elif self.solution_limit > 1:
			if self.solutions == 1:
				print('This sudoku has a unique solution.')
			else:
				message = 'This sudoku has multiple solutions, ' + \
					f'found {self.solutions} (capped at {self.solution_limit}).'
				print(message)
		else:
			message = 'This sudoku has at least one solution, ' + \
				'increase solution_limit to 2 or more to determine solution uniqueness.'
			print(message)