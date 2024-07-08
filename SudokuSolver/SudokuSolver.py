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

	grid="""4_______5\n____416__\n_8163____\n___3__1__\n19____8_7\n_54__7__6\n825_1976_\n___8__59_\n61_57324_"""
	sg = SudokuGrid(grid)

	print(sg.getRowCells(1))
	print(sg.getColCells(0))

	print(sg)
	print(sg.getSquareCells(7, 7))
