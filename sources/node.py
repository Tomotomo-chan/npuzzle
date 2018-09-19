# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    node.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mressier <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/09/17 11:53:51 by mressier          #+#    #+#              #
#    Updated: 2018/09/17 11:53:56 by mressier         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from Heuristiques import heuristiques

class Node:

	""" g(n) pointeur distance heuristic """

	def __init__(self, parent, puzzle, movement):
		self.parent = parent
		self.puzzle = puzzle
		self.open = True
		self.movement = movement

		if parent is not None:
			self.dist_from_start = parent.dist_from_start + 1
		else:
			self.dist_from_start = 0

		self.dist_heuristic = heuristiques.calcul_heuristique(puzzle)
		self.fn = self.dist_heuristic + self.dist_from_start

	def __str__(self):
		return ('Etat: ' + ('open' if self.open else 'close') + '\n'
		+ 'dist from start: ' + str(self.dist_from_start) + '\n'
		+ 'dist heuristic: ' + str(self.dist_heuristic) + '\n'
		+ 'hash: ' + str(self.puzzle.hash) + '\n'
		+ 'Puzzle: \n' + str(self.puzzle))



## EXAMPLE
# node = Node(None, [], None)
# print node