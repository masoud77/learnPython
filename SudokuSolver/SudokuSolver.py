from SudokuGrid import *

if __name__ == "__main__":
	sc1 = SudokuCell(6, 5, "7")
	sc2 = SudokuCell(5, 7, "5")
	sc3 = SudokuCell(0, 0, "_")

	print("1", sc1)
	print("2", sc2)
	print("3", sc3)

	sc3.pop('5')
	print(sc3)

	sc2.pop('5')
	print(sc2)

	sr1 = SudokuRow(5, "3_1___59_")
	print(sr1)
