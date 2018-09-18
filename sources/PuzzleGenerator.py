# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    RandomizePuzzle.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mressier <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/09/18 10:53:01 by mressier          #+#    #+#              #
#    Updated: 2018/09/18 10:53:02 by mressier         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from Puzzle import *
from PuzzleIndex import *

class PuzzleGenerator:

	"""
	Generate a puzzle with a given size
	"""
	def generate_puzzle(self, size):
		if size < 2:
			return None
		
		basic_puzzle = self.generate_empty_puzzle(size)
		index = PuzzleIndex(0, 0)
		value = 1
		final_value = size * size

		while value < final_value:
			# fill first line
			# ----
			# ....
			# ....
			# ....
			while index.column < size and value_at_index(basic_puzzle, index) is 0 and value < final_value:
				basic_puzzle[index.line][index.column] = value
				value += 1
				index.column += 1
			
			# Go too far on right. Move left to the previous column.
			index.column -= 1
			# Move on the next line.
			index.line += 1

			# fill last column
			# xxxx
			# ...|
			# ...|
			# ...|
			while index.line < size and value_at_index(basic_puzzle, index) is 0 and value < final_value:
				basic_puzzle[index.line][index.column] = value
				value += 1
				index.line += 1
			
			# Go too down. Move up to the previous line.
			index.line -= 1
			# Move left to the previous column.
			index.column -= 1

			# fill last line
			# xxxx
			# ...x
			# ...x
			# ----
			while index.column >= 0 and value_at_index(basic_puzzle, index) is 0 and value < final_value:
				basic_puzzle[index.line][index.column] = value
				value += 1
				index.column -= 1
			
			# Go too far on left. Move right to the previous column.
			index.column += 1
			# Move up to the previous line
			index.line -= 1

			# fill first column
			# xxxx
			# |..x
			# |..x
			# xxxx
			while index.line >= 0 and value_at_index(basic_puzzle, index) is 0 and value < final_value:
				basic_puzzle[index.line][index.column] = value
				value += 1
				index.line -= 1
			
			# Go too far up. Move down to the next line.
			index.line += 1
			# Move right to the next column.
			index.column += 1

		return Puzzle(basic_puzzle)

	'Create a list of list of the given size fill of zero. It\'s an empty puzzle.'
	def generate_empty_puzzle(self, size):
		if size < 0:
			return None
		
		basic_puzzle = []
		for i in range(size):
			basic_puzzle.append([0] * size)
		return basic_puzzle

	"""
	Randomize a puzzle
	"""
	def randomize_puzzle(self, puzzle):
		return

""" global """
def value_at_index(puzzle, index):
	return puzzle[index.line][index.column]


generator = PuzzleGenerator()
for i in range(1,15):
	print generator.generate_puzzle(i)
	print "---"