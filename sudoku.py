def solve(bo):
    find = emptyCase(bo)
    if not find: # if find is None or 0
        return True
    else:
        row, col = find

    for i in range(1,10):

        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo): # check chaque chiffres de 1 à 9 
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num :
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num :
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num :
                return False

    return True


def showGrid(grid):
	
	for row in range (len(grid)):

		if row % 3 == 0 :
			print(" - - - - - - - - - - - - - -")

		for col in range(len(grid)):

			if col % 3 == 0:
				print(" | ", end="")
			
			if col == 8 :
				print(str(grid[row][col]) + " | ")
			else:
				print(str(grid[row][col]) + " ", end="")

	print(" - - - - - - - - - - - - - -")



def emptyCase(grid):
	for row in range(len(grid)):
		for col in range(len(grid)):
			if grid[row][col] == 0:
				return (row, col)

	return 0

grid = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

print("\nThe initial grid is :\n")
showGrid(grid)

solve(grid)

print("\nThe final grid is :\n")
showGrid(grid)


