import os
import csv

boardSize = 8
boardRows = [1,2,3,4,5,6,7,8]
boardCols = ['A','B','C','D','E','F','G','H']
currBoard = [[None for x in range(8)] for y in range(8)]
playerOne = 'P1'
playerTwo = 'P2'
king = 'K'
queen = 'Q'
knight = 'Kn'
pawn = 'P'
rook = 'R'
bishop = 'B'
captureEnemy = 0
emptyCase = 1
sameTeam = 2
wall = 3

def write_board(board):
	tempList = []
	os.remove("board.csv")
	csvfile = open("board.csv", 'w')
	writer = csv.writer(csvfile, dialect='excel', delimiter=",")
	
	for point in board:
		tempList.clear()
		for loc in point:
			tempList.append("{0}|{1},{2}|{3}".format(loc[0], loc[1], loc[2], loc[3]))
		writer.writerows([tempList])

def read_board(boardFile):
	csvfile = open(boardFile, 'rt')
	reader = csv.reader(csvfile)
	tRow = 0
	tCol = 0
	
	for row in reader:
		if row:
			tCol = 0
			for cell in row:
				vals = cell.split("|")
				point = vals[1].split(",")
				currBoard[tRow][tCol] = (vals[0],\
				point[0],\
				point[1],\
				vals[2])
				tCol += 1
			tRow += 1		
		
def init_board():
	for row in range(boardSize):
		for col in range(boardSize):
			if row < 2:
				currBoard[row][col] = (king,boardCols[row],boardRows[col],playerOne)
			elif row > 5:
				currBoard[row][col] = (king,boardCols[row],boardRows[col],playerTwo)
			else:
				currBoard[row][col] = (king,boardCols[row],boardRows[col],'E')


def print_board(board):
	count = 0
	for point in board:
		for loc in point:
			if count % 8 == 0:
				print("")
			print("{0}: ( {1},{2} )|{3}\t".format(loc[0], loc[1], boardCols[int(loc[2])-1], loc[3]),end="")
			count += 1

def moves_king(board,player,tup):
	row, col = tup
	
	iRow = int(row)
	iCol = int(col)
	allMoves = []
	proposedMoves = [(iRow,iCol-1),(iRow,iCol+1),(iRow+1,iCol),(iRow-1,iCol),\
	                 (iRow+1,iCol+1),(iRow+1,iCol-1),(iRow-1,iCol+1),(iRow-1,iCol-1)]
		
	for move in proposedMoves:
		case = check_move(board,move,player)
			
		if case == emptyCase:
			allMoves.append(move)
			
		elif case == captureEnemy:
			allMoves.append(move)
		
	return allMoves
	
	
	
def moves_queen(board,player,tup):
	row, col = tup
	
	iRow = int(row)
	iCol =int(col)
	
	allMoves = []
	
	badPaths = []
	path = [0,1,2,3,4,5,6,7]
	
	proposedMoves = []
	
	for j in range(1,boardSize):
		proposedMoves.append((iRow+j,iCol))
		proposedMoves.append((iRow-j,iCol))
		proposedMoves.append((iRow,iCol+j))
		proposedMoves.append((iRow,iCol-j))
		proposedMoves.append((iRow+j,iCol+j))
		proposedMoves.append((iRow+j,iCol-j))
		proposedMoves.append((iRow-j,iCol+j))
		proposedMoves.append((iRow-j,iCol-j))
	
	k = 0
	for move in proposedMoves:
		path = k
		path %= 8
		
		case = check_move(board,move,player)
			
		if case == emptyCase and not path in badPaths:
			allMoves.append(move)
			
		elif case == captureEnemy and not path in badPaths:
			allMoves.append(move)
			badPaths.append(path)
			
		elif case == sameTeam:
			badPaths.append(path)
		k += 1
			
	return allMoves
	
	
def moves_knight(board,player,tup):	
	row, col = tup
	iRow = int(row)
	iCol =int(col)
	
	allMoves = []
	badPaths = []
	
	proposedMoves = [(iRow-2,iCol-1),(iRow-2,iCol+1),(iRow+2,iCol-1),(iRow+2,iCol+1),(iRow-1,iCol+2),(iRow+1,iCol+2),(iRow+1,iCol-2),(iRow-1,iCol-2)]
	
	k = 0
	
	for move in proposedMoves:
		path = k % 8
		case = check_move(board,move,player)
		
		if case == emptyCase and not path in badPaths:
			allMoves.append(move)
			
		elif case == captureEnemy and not path in badPaths:
			allMoves.append(move)
			badPaths.append(path)
			
		elif case == sameTeam:
			badPaths.append(path)
		k += 1
	
	return allMoves

def moves_pawn(board,player,tup):
	allMoves = []
	proposedMoves = []
	row, col = tup
	
	iRow = int(row)
	iCol = int(col)
	
	if row == 1 or row == 6:
		if player == playerOne:
			proposedMoves.append((iRow+2,iCol))
		else:
			proposedMoves.append((iRow-2,iCol))
				
	if player == playerOne and iCol < 7:
		proposedMoves.append((iRow+1,iCol))
		unit,row,col,lookAheadRt = board[iRow+1][iCol+1]
		
		unit,row,col,lookAheadLt = board[iRow+1][iCol-1]
		if lookAheadRt == playerTwo:
			proposedMoves.append((iRow+1,iCol+1))
		if lookAheadLt == playerTwo:
			proposedMoves.append((iRow+1,iCol-1))
	
	elif player == playerTwo and (iCol < 7 or iCol >= 1):
		proposedMoves.append((iRow-1,iCol))
		unit,row,col,lookAheadRt = board[iRow-1][iCol+1]
		unit,row,col,lookAheadLt = board[iRow-1][iCol-1]
		if lookAheadRt == playerOne:
			proposedMoves.append((iRow-1,iCol+1))
		if lookAheadLt == playerOne:
			proposedMoves.append((iRow-1,iCol-1))
		
	for move in proposedMoves:
		row, col = move
		case = check_move(board,move,player)	
		
		if case == emptyCase:
			allMoves.append(move)
			
		elif case == captureEnemy:
			allMoves.append(move)
	
	return allMoves
	
def moves_rook(board,player,tup):
	row, col = tup
	
	iRow = int(row)
	iCol = int(col)
	allMoves = []
	badPaths = []
	proposedMoves = []
	
	for j in range(1,boardSize):
		proposedMoves.append((iRow+j,iCol))
		proposedMoves.append((iRow-j,iCol))
		proposedMoves.append((iRow,iCol+j))
		proposedMoves.append((iRow,iCol-j))
	
	k = 0
	for move in proposedMoves:		
		path = k % 4
		case = check_move(board,move,player)
		
		if case == emptyCase and not path in badPaths:
			allMoves.append(move)
			
		elif case == captureEnemy and not path in badPaths:
			allMoves.append(move)
			badPaths.append(path)
			
		elif case == sameTeam:
			badPaths.append(path)
		k += 1
	
	return allMoves
	
def moves_bishop(board,player,tup):
	row, col = tup
	
	iRow = int(row)
	iCol = int(col)
	allMoves = []
	badPaths = []
	
	proposedMoves = []
	
	for j in range(1,boardSize):
		proposedMoves.append((iRow+j,iCol+j))
		proposedMoves.append((iRow-j,iCol-j))
		proposedMoves.append((iRow-j,iCol+j))
		proposedMoves.append((iRow+j,iCol-j))
	
	k = 0
	for move in proposedMoves:
		path = k % 4
		
		case = check_move(board,move,player)
		
		if case == emptyCase and not path in badPaths:
			allMoves.append(move)
			
		elif case == captureEnemy and not path in badPaths:
			allMoves.append(move)
			badPaths.append(path)
			
		elif case == sameTeam:
			badPaths.append(path)
		k+=1
	
	return allMoves
	
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
	for unit in player_pieces(board,player):
		piece,location = unit
		moves = moves_function(piece)
		
		row,colVal = location
		locationVal = (row,boardCols[int(colVal)-1])
		
		print("Moves for player",player,"'s ",piece," at ",locationVal)
		row, col = location
		location = (int(row)-1,int(col)-1)
		
		for mov in moves(board,player,location):
			row, col = mov
			mov = (row+1,boardCols[col])
			print("\tPossible move: ", end="")
			print(mov)
		print("")

def check_move(board, location, player):
	row, col = location
	
	if col < 0 or col > 7:
		return wall
	if row < 0 or row > 7:
		return wall
	unit,dcol,drow,occuPlayer = board[row][col]	
	
	if occuPlayer == 'E':
		return emptyCase
	elif occuPlayer != player:
		return captureEnemy
	elif occuPlayer == player:
		return sameTeam

		
#MAIN
read_board("board2.csv")
print_board(currBoard)

print("\nRequesting player 2's possible moves")
possible_moves(currBoard,playerTwo)

print("\nRequesting player 1's possible moves")
possible_moves(currBoard,playerOne)