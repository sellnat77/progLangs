boardSize = 8
boardRows = [1,2,3,4,5,6,7,8]
boardCols = ['A','B','C','D','E','F','G','H']
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
	row, col = tup
	
def moves_queen(board,player,tup):
	row, col = tup
	
def moves_knight(board,player,tup):
	row, col = tup
	
def moves_pawn(board,player,tup):
	row, col = tup
	
def moves_rook(board,player,tup):
	row, col = tup
	
def moves_bishop(board,player,tup):
	row, col = tup
	
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
	#generator
	
def possible_moves(board, player):
	#use player pieces
	




			
init_board()
print_board()