boardSize = 8
boardRows = [1,2,3,4,5,6,7,8]
boardCols = [1,2,3,4,5,6,7,8]
currBoard = [[None for _ in range(8)] for _ in range(8)]
playerOne = 'P1'
playerTwo = 'P2'
king = 'K'
queen = 'Q'
knight = 'Kn'
pawn = 'P'
rook = 'R'
bishop = 'B'

def init_board():
	for row in range(boardSize):
		for col in range(boardSize):
			if row < 2:
				currBoard[row][col] = (queen,boardCols[row],boardRows[col],playerOne)
			elif row > 5:
				currBoard[row][col] = (queen,boardCols[row],boardRows[col],playerTwo)
			else:
				currBoard[row][col] = (queen,boardCols[row],boardRows[col],'E')


def print_board():
	count = 0
	for point in currBoard:
		for loc in point:
			if count % 8 == 0:
				print()
			print("{0}: ( {1},{2} )|{3}\t".format(loc[0], loc[1], loc[2], loc[3]),end="")
			count += 1

def moves_king(board,player,tup):
	row, col = tup
	allMoves = []
	
	
	#if same team
	#if enemy piece
	
	#determine player
		#can move up,down,left,right
	
	if check_move(board,(row,col-1),player):
		allMoves.append((row,col-1))
	if check_move(board,(row,col+1),player):
		allMoves.append((row,col+1))
	if check_move(board,(row+1,col),player):
		allMoves.append((row+1,col))
	if check_move(board,(row-1,col),player):
		allMoves.append((row-1,col))
		
	return allMoves
	
	
	
def moves_queen(board,player,tup):
	row, col = tup
	allMoves = []
	
	#if same team
	#if enemy piece
	for j in range(0,boardSize):
		#check fwd
		if check_move(board,(row+j,col),player):
			allMoves.append((row+j,col))
		#check bckwd
		if check_move(board,(row-j,col),player):
			allMoves.append((row-j,col))
		#check diag rt fwd
		if check_move(board,(row+j,col+j),player):
			allMoves.append((row+j,col+j))
		#check diag lt fwd
		if check_move(board,(row+j,col-j),player):
			allMoves.append((row+j,col-j))
		#check diag rt bckwd
		if check_move(board,(row-j,col+j),player):
			allMoves.append((row-j,col+j))
		#check diag lt bckwd
		if check_move(board,(row-j,col-j),player):
			allMoves.append((row-j,col-j))
			
	return allMoves
	
	
def moves_knight(board,player,tup):	
	row, col = tup
	
	#if same team
	#if enemy piece

def moves_pawn(board,player,tup):
	allMoves = []
	row, col = tup
	
	#if same piece
		#if not playerOne
	#if enemy diagonal
	#if enemy in front
		#if (row, col+1).unit is not playerTwo
	#fwd = (col,row+1),(col,row+1)
		#Check if not past the board
		#if col+1 or col -1 is not > 8 or < 0
	#diag = (col+1,row+1),(col-1,row+1)
	
	if player == playerOne:
		
		allMoves.append((row,col+1))
		allMoves.append((row,col+2))
	else:
		allMoves.append((row,col-1))
		allMoves.append((row,col-2))
		
	return allMoves
	
def moves_rook(board,player,tup):
	row, col = tup
	
	#if same team
	#if enemy piece
	
def moves_bishop(board,player,tup):
	row, col = tup
	
	#if same team
	#if enemy piece
	
def moves_function(unit):
	return{
		king : moves_king,
		queen : moves_queen,
		knight : moves_knight,
		rook : moves_rook,
		bishop : moves_bishop,
		pawn : moves_pawn	
	}.get(unit,moves_pawn)

def player_pieces(board,player):
	#yields type of piece, pieces coordinates
	for rw in board:
		for point in rw:
			unit, row, col, locPlayer = point
			if player == locPlayer:
				yield((unit,(row,col)))
	
def possible_moves(board, player):
	count = 1
	for unit in player_pieces(board,player):
		piece,location = unit
		moves = moves_function(piece)
		
		print("Moves for player",player,"'s ",piece," at ",location)
		for mov in moves(board,player,location):
			if count % 2 == 0:
				print("")
			print("\tHeres a move!",count, end="")
			print(mov)
			count += 1
		print("")
	
	#use player pieces

def check_move(board, location, player):
	row, col = location
	row -= 1
	col -= 1
	
	
	
	if col > 7 or col < 0:
		return False
	if row > 7 or row < 0:
		return False
	#print (board[row][col])	
	unit,dcol,drow,occuPlayer = board[row][col]	
	#print("Trying to ",row,col)
	
	#print(occuPlayer,"--",player)
	
	if occuPlayer == 'E' or occuPlayer != player:
		return True
	else:
		return False

init_board()
print_board()

print("Requesting player 2")
possible_moves(currBoard,playerTwo)
print("Requesting player 1")
possible_moves(currBoard,playerOne)