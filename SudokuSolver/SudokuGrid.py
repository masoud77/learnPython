class SudokuCell:

	def __init__ (self, row, col, value):
		self.row = row
		self.col = col
		if value == "_":
			self.value = list(range(1, 10))
			self.state = "empty"
		else:
			self.value = value
			self.state = "init"

	def __str__(self):
		print_str = "SudokuCell Details:\n\tRow: {}\n\tCol: {}\n\tValues: {}\n\tState: {}\n".format(self.row, self.col, self.value, self.state)
		return print_str

	def __repr__(self):
		value = "_" if len(self.value) > 1 else self.value
		repr_str = "SudokuCell({}, {}, \"{}\")".format(self.row, self.col, value)
		return repr_str

	def pop(self, number):
		'''If the number is present in the value list, remove it from the value list"
  		return None
