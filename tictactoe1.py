import time
import random


class TicTac:
	def __init__(self):
		self.board = [
				[" ", " ", " "],
				[" ", " ", " "],
				[" ", " ", " "]
				]
		self.back = []
						
	def reset_pos(self):
		self.board[self.back[0]][self.back[1]] = " "
		
	def insert(self, player):
		op = ["1", "3" , "2"]
		row = input("row = ")
		while row not in op:
			print('INVALID')
			row = input("y = ")
		coloumn = input("coloumn = ")
		while coloumn not in op:
			print("INVALID")
			coloumn = input("x = ")
		coloumn, row = int(coloumn), int(row)
		if self.board[row-1][coloumn-1] != " ":
			print("Already occupied, Try again !")
			return self.insert(player)
		self.back = [row-1, coloumn-1]
		self.board[row-1][coloumn-1] = player
	#	self.show_board()
		
	
	
	def varify(self) -> bool:
		bd = self.board
		for i in range(3):
			if "".join(self.board[i]) == "OOO" or "".join(self.board[i]) == "XXX":
				return True
		for i in range(3):
			row1 = f"{bd[0][i]}{bd[1][i]}{bd[2][i]}"
			if row1 == "OOO" or row1 == "XXX":
				return True
		cross = f"{bd[0][0]}{bd[1][1]}{bd[2][2]}"
		if cross == "XXX" or cross == "OOO":
			return True
		cross = f"{bd[2][0]}{bd[1][1]}{bd[0][2]}"
		if cross == "XXX" or cross == "OOO":
			return True
		return False
	
	def computer(self, p: str) -> None:
		
		for i in range(3):
			row1 = ''.join(self.board[i])
			if row1 == 'O O' or row1 == 'X X':
				self.board[i][1] = p
				return
			if row1 == 'OO ' or row1 == 'XX ':
				self.board[i][2] = p
				return
			if row1 == ' OO' or row1 == ' XX':
				self.board[i][0] = p
				return
			#print(row)
			
		for i in range(3):
			col = ""
			for n in range(3):
				col += self.board[n][i]
			
			if col == 'O O' or col == 'O O':
				self.board[1][i] = p
				return
			if col == 'OO ' or col == 'XX ':
				self.board[2][i] = p
				return
			if col == ' OO' or col == ' XX':
				self.board[0][i] = p
				return
			#print(col)
		cross = self.board[0][0] + self.board[1][1] + self.board[2][2]
		
		if cross == ' OO' or cross == ' XX':
			self.board[0][0] = p
			return	
		if cross == 'O O' or cross == 'O O':
			self.board[1][1] = p
			return
		if cross == 'OO ' or cross == 'XX ':
			self.board[2][2] = p
			return
		
		cross = self.board[0][2] + self.board[1][1] + self.board[2][0]
		
		if cross == 'OO ' or cross == 'XX ':
			self.board[2][0] = p
			return
		if cross == 'O O' or cross == 'O O':
			self.board[1][1] = p
			return
		if cross == ' OO' or cross == ' XX':
			self.board[0][2] = p
			return

		spots = []
		for i in range(3):
			for n in range(3):
				if self.board[i][n] == ' ':
					spots.append([i, n])
					
		a, b = random.choice(spots)
		
		self.board[a][b] = p
					
		

	def show_board(self):
		l = []
		for i in range(len(self.board)):
			for n in range(3):
				if self.board[i][n] != None:
					l.append(f"|{self.board[i][n]}")
				else:
					l.append("| ")
		print("  1   2   3")
		print("  __________")
		print(f"1 {' '.join(l[:3])} |")
		print("  ----------")
		print(f"2 {' '.join(l[3:6])} |")
		print("  ----------")
		print(f"3 {' '.join(l[6:9])} |")
		print("  ----------")
def play():
	n = 9
	B = TicTac()
	status = B.varify()
	p1 = "X"
	p2 = "O"
	print('Player1 is: X')
	print()
	print('Player2 is: O')
	print()
	print('LETS PLAY!!')
	print()
	while not status and n > 0:
		b = None
		if n % 2 == 0:
			print(f"Player1,its your turn")
			B.show_board()
			print()
			B.computer(p1)
			time.sleep(1)
		else:
			print(f"Player2,its your turn")
			B.show_board()
			print()
			B.insert(p2)
			
		
		print("**********************************")
		
		status = B.varify()
		n -= 1
		
		
	B.show_board()
		
	if status:
		if n % 2 == 0:
			return "BROO!!! You Won!!"
		else:
			return "LOL!! YOU SUCK!!"
	return "LOL!!!Its a tie..."
		
if __name__ == '__main__':
	print(play())
	

