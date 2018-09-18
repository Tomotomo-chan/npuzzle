# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    PuzzleCompare.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mressier <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/09/18 14:32:39 by mressier          #+#    #+#              #
#    Updated: 2018/09/18 14:32:47 by mressier         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from Puzzle import *

class PuzzleCompare:
	def get_parity_for_value(self, value, puzzle1, puzzle2):
		index1 = puzzle1.get_piece_index(value)
		index2 = puzzle2.get_piece_index(value)

		if index1 is None or index2 is None:
			return None
		
		return abs(index1.line - index2.line) + abs(index1.column - index2.column)

puzzle_compare = PuzzleCompare()

## EXAMPLE
from PuzzleGenerator import *

size = 7
puzzle = puzzle_generator.generate_puzzle(size)
random_puzzle = puzzle_generator.generate_random_puzzle(size)

print puzzle
print '----'
print random_puzzle
print '----'
print puzzle_compare.get_parity_for_value(0, puzzle, random_puzzle)