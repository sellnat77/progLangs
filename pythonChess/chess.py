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
				currBoard[row][col] = (pawn,boardCols[col],boardRows[row],playerOne)
			elif row > 5:
				currBoard[row][col] = (pawn,boardCols[col],boardRows[row],playerTwo)
			else:
				currBoard[row][col] = (pawn,boardCols[col],boardRows[row],'E')


def print_board():
	count = 0
	for point in currBoard:
		for loc in point:
			if count % 8 == 0:
				print()
			print("{0}: ( {1},{2} )|{3}\t".format(loc[0], loc[1], loc[2], loc[3]),end="")
			count += 1

def moves_king(board,player,tup):
	col, row = tup
	
	#if same team
	#if enemy piece
	
	
def moves_queen(board,player,tup):
	col, row = tup
	
	#if same team
	#if enemy piece
	
def moves_knight(board,player,tup):	
	col, row = tup
	
	#if same team
	#if enemy piece

def moves_pawn(board,player,tup):
	allMoves = []
	col, row = tup
	
	#if same piece
		#if not playerOne
	#if enemy diagonal
	#if enemy in front
		#if (col, row+1).unit is not playerTwo
	#fwd = (col,row+1),(col,row+1)
		#Check if not past the board
		#if col+1 or col -1 is not > 8 or < 0
	#diag = (col+1,row+1),(col-1,row+1)
	
	if player == playerOne:
		
		allMoves.append((col,row+1))
		allMoves.append((col,row+2))
	else:
		allMoves.append((col,row-1))
		allMoves.append((col,row-2))
		
	return allMoves
	
def moves_rook(board,player,tup):
	col, row = tup
	
	#if same team
	#if enemy piece
	
def moves_bishop(board,player,tup):
	col, row = tup
	
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
			unit, col, row, locPlayer = point
			if player == locPlayer:
				yield((unit,(col,row)))
	
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
			
init_board()
print_board()

print("Requesting player 2")
possible_moves(currBoard,playerTwo)
print("Requesting player 1")
possible_moves(currBoard,playerOne)