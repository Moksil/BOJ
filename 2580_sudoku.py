def print_map(board):
	for i in range(len(board)):
		for j in range(len(board)):
			if j != len(board) - 1:
				print(board[i][j], end=' ')
			else:
				print(board[i][j], end = '\n')

def check(board, row, col, val):
	for i in range(9):
		if board[row][i] == val:
			return False
		if board[i][col] == val:
			return False
	area_row = (row // 3) * 3
	area_col = (col // 3) * 3
	for i in range(area_row, area_row + 3):
		for j in range(area_col, area_col + 3):
			if (row != i and col != j) and val == board[i][j]:
				return False
	board[row][col] = val;
	return True

def get_unsorved_cord(board):
	lst = []
	for row in range(9):
		for col in range(9):
			if board[row][col] == 0:
				lst.append([row, col])
	return lst

def sudoku_dfs(board, unsorved_lst, depth):
	if depth == len(unsorved_lst):
		return True
	cord = unsorved_lst[depth]
	ret = False
	for i in range(1, 10):
		if check(board, cord[0], cord[1], i):
			if sudoku_dfs(board, unsorved_lst, depth + 1):
				ret = True
			else:
				board[cord[0]][cord[1]] = 0
				ret = False
	return ret
			
board = []
for _ in range(9):
	board.append(list(map(int, input().split())))

unsorved = get_unsorved_cord(board)
sudoku_dfs(board, unsorved, 0)
print_map(board)


# result : OK