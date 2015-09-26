import os
import csv
import sys 

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
		print ("\t".join(tempList))
		writer.writerows([tempList])

def read_board(boardFile):
	csvfile = open(boardFile, 'rt')
	reader = csv.reader(csvfile)
	tRow = 0
	tCol = 0
	
	for row in reader:
		if row:
			tCol = 0
			print("ROW:",row,"indx",tRow)
			for cell in row:
				print("CELL:",cell,"indx",tCol)
				vals = cell.split("|")
				#print(cell.split('|'))
				#print(vals[2])
				point = vals[1].split(",")
				#print(point)
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
				print("LOC:",loc)
			print("{0}: ( {1},{2} )|{3}\t".format(loc[0], loc[1], loc[2], loc[3]),end="")
			count += 1

def moves_king(board,player,tup):
	row, col = tup
	
	iRow = int(row)
	iCol = int(col)
	allMoves = []
	proposedMoves = [(iRow,iCol-1),(iRow,iCol+1),(iRow+1,iCol),(iRow-1,iCol)]
	
	
	for move in proposedMoves:
		case = check_move(board,move,player)
			
		if case == emptyCase:
			allMoves.append(move)
			
		elif case == captureEnemy:
			allMoves.append(move)
			badPaths.append(path)
		
	return allMoves
	
	
	
def moves_queen(board,player,tup):
	row, col = tup
	
	iRow = int(row)
	iCol =int(col)
	
	allMoves = []
	
	hitTeam = False
	badPaths = []
	path = [0,1,2,3,4,5,6,7]
	
	proposedMoves = []
	
	for j in range(1,boardSize):
		#Storing tracks to throw them out if same team blocking path
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
			
			
			#Stop this track
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
			#Stop this track
		k += 1
	
	#if same team
	#if enemy piece
	return allMoves

def moves_pawn(board,player,tup):
	allMoves = []
	row, col = tup
	
	iRow = int(row)
	iCol = int(col)
	
	proposedMoves = [(iRow-1,iCol),(iRow+1,iCol),\
					 (iRow-2,iCol),(iRow+2,iCol),\
					 (iRow+1,iCol+1),(iRow-1,iCol+1),\
					 (iRow+1,iCol-1),(iRow-1,iCol-1)]
	#if same piece
		#if not playerOne
	#if enemy diagonal
	#if enemy in front
		#if (row, col+1).unit is not playerTwo
	#fwd = (col,row+1),(col,row+1)
		#Check if not past the board
		#if col+1 or col -1 is not > 8 or < 0
	#diag = (col+1,row+1),(col-1,row+1)
	
	for move in proposedMoves:
		case = check_move(board,move,player)
		
		if case == wall:
			None
			#stop this track
			
		elif case == emptyCase:
			allMoves.append(move)
			
		elif case == captureEnemy:
			allMoves.append(move)
			
		elif case == sameTeam:
			None
			#Stop this track
	
	#if player == playerOne:
		
	#	allMoves.append((row,col+1))
	#	allMoves.append((row,col+2))
	#else:
	#	allMoves.append((row,col-1))
	#	allMoves.append((row,col-2))
		
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
		print("TRYING: ",move)
		
		path = k % 4
		print("PATH: ",path)
		case = check_move(board,move,player)
		
		if case == emptyCase and not path in badPaths:
			allMoves.append(move)
			
		elif case == captureEnemy and not path in badPaths:
			allMoves.append(move)
			badPaths.append(path)
			
		elif case == sameTeam:
			badPaths.append(path)
			#Stop this track
		k += 1
	#if same team
	#if enemy piece
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
			#Stop this track
		k+=1
	
	#if same team
	#if enemy piece
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
	
	
	
	if col < 0 or col > 7:
		return wall
	if row < 0 or row > 7:
		return wall
	#print (board[row][col])	
	unit,dcol,drow,occuPlayer = board[row][col]	
	#print("Trying to ",row,col)
	
	#print(occuPlayer,"--",player)
	
	if occuPlayer == 'E':
		return emptyCase
	elif occuPlayer != player:
		return captureEnemy
	elif occuPlayer == player:
		print("SAME TEAM")
		return sameTeam

read_board("board2.csv")
#init_board()
print_board(currBoard)

print("Requesting player 2")
possible_moves(currBoard,playerTwo)
print("Requesting player 1")
possible_moves(currBoard,playerOne)

write_board(currBoard)