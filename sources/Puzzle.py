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
from PuzzleIndex import PuzzleIndex

class Puzzle:

	empty_piece = 0
	
	"""" Represent a NPuzzle grid """

	def __init__(self, puzzle):
		self.puzzle = puzzle
		self.size = len(puzzle)
		self.hash = puzzle.__hash__
	
	def __str__(self):
		string = ''
		for line in self.puzzle:
			if len(string) is not 0:
				string += '\n'
			for piece in line:
				string += str(piece)
				string += ' '
		return string

	'Get the index of the piece with the given value if it exist'
	def get_piece_index(self, value):
		for line_index in range(self.size):
			for col_index in range(self.size):
				if self.puzzle[line_index][col_index] is value:
					return PuzzleIndex(line_index, col_index)
		return None

	'Get the movement available on the piece of value in the puzzle'
	def get_available_movements(self, piece_value):
		piece_index = self.get_piece_index(piece_value)

		if piece_index is None:
			return

		available_movements = []
		if piece_index.line > 0:
			available_movements.append(PuzzleMovement.up)
		if piece_index.column > 0:
			available_movements.append(PuzzleMovement.left)
		if piece_index.line + 1 < self.size:
			available_movements.append(PuzzleMovement.down)
		if piece_index.column + 1 < self.size:
			available_movements.append(PuzzleMovement.right)
		return available_movements

	'Apply movement on the empty piece of the puzzle'
	def apply_movement(self, piece_value, move):
		piece_index = self.get_piece_index(piece_value)

		if piece_index is None:
			return

		options = {
			PuzzleMovement.up: self.up,
			PuzzleMovement.down: self.down,
			PuzzleMovement.left: self.left,
			PuzzleMovement.right: self.right,
		}

		options[move](piece_index)

	'Move the piece at index up'
	def up(self, index):
		if index.line > 0:
			self.puzzle[index.line][index.column] = self.puzzle[index.line - 1][index.column]
			self.puzzle[index.line - 1][index.column] = 0
	
	'Move the piece at index down'
	def down(self, index):
		if index.line + 1 < self.size:
			self.puzzle[index.line][index.column] = self.puzzle[index.line + 1][index.column]
			self.puzzle[index.line + 1][index.column] = 0
	
	'Move the piece at index to the left'
	def left(self, index):
		if index.column > 0:
			self.puzzle[index.line][index.column] = self.puzzle[index.line][index.column - 1]
			self.puzzle[index.line][index.column - 1] = 0
	
	'Move the piece at index to the right'
	def right(self, index):
		if index.column + 1 < self.size:
			self.puzzle[index.line][index.column] = self.puzzle[index.line][index.column + 1]
			self.puzzle[index.line][index.column + 1] = 0

## EXAMPLES
puzzle = Puzzle([
	[1, 0, 3],
	[4, 5, 6],
	[7, 8, 2]
])

print puzzle
puzzle.apply_movement(Puzzle.empty_piece, PuzzleMovement.down)
print puzzle
print str(puzzle.get_available_movements(Puzzle.empty_piece))
