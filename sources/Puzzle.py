# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    puzzle.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mressier <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/09/17 14:15:22 by mressier          #+#    #+#              #
#    Updated: 2018/09/17 14:15:24 by mressier         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from PuzzleMovement import PuzzleMovement

class PuzzleIndex:
	def __init__(self, line, column):
		self.line = line
		self.column = column

	def __str__(self):
		return 'line: ' + str(self.line) + ', col: ' + str(self.column)

class Puzzle:
	
	"""" Represent a NPuzzle grid """

	def __init__(self, puzzle):
		self.puzzle = puzzle
		self.size = len(puzzle)
	
	def __str__(self):
		string = ''
		for line in self.puzzle:
			if len(string) is not 0:
				string += '\n'
			for piece in line:
				string += str(piece)
				string += ' '
		return string

	def get_index(self, value):
		for lineIndex in range(self.size):
			for colIndex in range(self.size):
				if self.puzzle[lineIndex][colIndex] is value:
					return PuzzleIndex(lineIndex, colIndex)
		return None

	'get the possible movement of the empty piece on the puzzle'
	def get_available_movements(self):
		zeroIndex = self.get_index(0)

		if zeroIndex is None:
			return

		available_movements = []
		if zeroIndex.line > 0:
			available_movements.append(PuzzleMovement.up)
		if zeroIndex.column > 0:
			available_movements.append(PuzzleMovement.left)
		if zeroIndex.line + 1 < self.size:
			available_movements.append(PuzzleMovement.down)
		if zeroIndex.column + 1 < self.size:
			available_movements.append(PuzzleMovement.right)
		return available_movements

	'Apply movement on empty piece on the puzzle'
	def apply_movement(self, move):
		zeroIndex = self.get_index(0)

		if zeroIndex is None:
			return

		options = {
			PuzzleMovement.up: self.up,
			PuzzleMovement.down: self.down,
			PuzzleMovement.left: self.left,
			PuzzleMovement.right: self.right,
		}

		options[move](zeroIndex)

	def up(self, index):
		if index.line > 0:
			self.puzzle[index.line][index.column] = self.puzzle[index.line - 1][index.column]
			self.puzzle[index.line - 1][index.column] = 0
	
	def down(self, index):
		if index.line + 1 < self.size:
			self.puzzle[index.line][index.column] = self.puzzle[index.line + 1][index.column]
			self.puzzle[index.line + 1][index.column] = 0
	
	def left(self, index):
		if index.column > 0:
			self.puzzle[index.line][index.column] = self.puzzle[index.line][index.column - 1]
			self.puzzle[index.line][index.column - 1] = 0
	
	def right(self, index):
		if index.column + 1 < self.size:
			self.puzzle[index.line][index.column] = self.puzzle[index.line][index.column + 1]
			self.puzzle[index.line][index.column + 1] = 0

puzzle = Puzzle([
	[1, 0, 3],
	[4, 5, 6],
	[7, 8, 2]
])

print puzzle
print str(puzzle.get_available_movements()) + '\n'

puzzle.apply_movement(PuzzleMovement.up)
print puzzle
print str(puzzle.get_available_movements()) + '\n'

puzzle.apply_movement(PuzzleMovement.left)
print puzzle
print str(puzzle.get_available_movements()) + '\n'