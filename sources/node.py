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


class Node:

	'static variables'
	nb_node = 0
	nb_node_open = 0

	'non static'
	open = True
	parent = None
	puzzle = None

	dist_from_start = 0
	dist_heuristic = None

	""" g(n) pointeur distance heuristic """

	def __init__(self, parent, puzzle):
		self.parent = parent
		self.puzzle = puzzle
		self.hash = puzzle.__hash__()

		if parent is not None:
			self.dist_from_start = parent.dist_from_start + 1
			parent.toggleOpen(False)
		else:
			self.dist_from_start = 0
		self.dist_heuristic = 0 # TEMP : TO CALCUL

		Node.nb_node += 1
		self.toggleOpen(True)

	def __str__(self):
		return ('Etat: ' + ('open' if self.open else 'close') + '\n'
		+ 'dist from start: ' + str(self.dist_from_start) + '\n'
		+ 'dist heuristic: ' + str(self.dist_heuristic) + '\n'
		+ 'Puzzle: \n' + str(self.puzzle))

	def toggleOpen(self, value):
		if self.open != value:
			if value:
				Node.nb_node_open += 1
			else:
				Node.nb_node_open -= 1
		self.open = value

node = Node(None, ((1, 2, 3), (4, 5, 6), (7, 8, 0)))

print node