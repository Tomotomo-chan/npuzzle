
from Puzzle import Puzzle
from Node import Node
from Env import env
from Heuristiques import *
from PuzzleMovement import *
import sys
import copy

class Solver:

	def __init__(self):
		self.fn_last_min = sys.maxint

	def find_tree_solution(self):
		count = 0
		while (len(env.opened_nodes) is not 0):
			count += 1
			if count % 100 is 0:
				print str(count) + ' ' + str(len(env.opened_nodes)) + ' ' + str(len(env.closed_nodes)) + ' ' + str(len(env.all_nodes))

			node = self.find_viable_node_with_a_star()
			if node is None:
				return None

			if self.is_solution(node):
				return node

			available_movements = node.puzzle.get_available_movements(Puzzle.empty_piece)

			for move in available_movements:
		   		if node.movement and move is puzzle_movement.opposite(node.movement):
					continue
				new_puzzle = copy.deepcopy(node.puzzle)
				new_puzzle.apply_movement(Puzzle.empty_piece, move)
				
				new_node = Node(node, new_puzzle, move)
				env.add_open_node(new_node)
				# print "--- node created ---"
				# print move
				# print new_node
				# print "---"
			env.close_node(node)

		return None

	def find_viable_node_with_a_star(self):
		tmp_node = None
		for n in env.opened_nodes:
			if tmp_node is None:
				tmp_node = n
			elif n.fn < tmp_node.fn:
				tmp_node = n
			elif n.fn == tmp_node.fn and n.dist_heuristic < tmp_node.dist_heuristic:
				tmp_node = n
		return tmp_node

	def is_solution(self, node):
		return node.dist_heuristic is 0

	def get_puzzle_solution(self, heuristic):
		heuristiques.change_heuristique(heuristic)

		if self.is_solution(env.all_nodes[0]):
			return env.all_nodes[0]

		return self.find_tree_solution()

solver = Solver()
