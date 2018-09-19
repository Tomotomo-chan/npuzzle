
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
        
    count = 0

    def find_tree_solution(self, node):
        # print "--- working node ---"
        # print node
        # print "---"
        Solver.count += 1
        # print Solver.count
        if node is None:
            return None
        
        # if Solver.count == 10:
        #     sys.exit()

        available_movements = node.puzzle.get_available_movements(Puzzle.empty_piece)
        for m in available_movements:
            if node.movement and m is puzzle_movement.opposite(node.movement):
                continue
            # print m
            tmp_puz = copy.deepcopy(node.puzzle)
            tmp_puz.apply_movement(Puzzle.empty_piece, m)
            if not self.puzzle_already_exist(tmp_puz):
                tmp_node = Node(node, tmp_puz, m)
                env.add_open_node(tmp_node)
                # print "--- node created ---"
                # print m
                # print tmp_node
                # print "---"
                if self.is_solution(tmp_node):
                    print Solver.count
                    return tmp_node
        env.close_node(node)
        # for n in env.all_nodes:
        #     print "---"
        #     print n.puzzle
        return self.find_tree_solution(self.find_node_fn_min())


    def find_node_fn_min(self):
        tmp_node = None
        for n in env.open_nodes:
            if tmp_node is None:
                tmp_node = n
            elif n.fn < tmp_node.fn:
                tmp_node = n
            elif n.fn == tmp_node.fn and n.dist_heuristic < tmp_node.dist_heuristic:
                tmp_node = n
        return tmp_node



    def puzzle_already_exist(self, puzzle):
        for n in env.all_nodes:
            if n.puzzle.hash == puzzle.hash:
                return True
        return False

    def is_solution(self, node):
        return node.dist_heuristic is 0

    def get_puzzle_solution(self, heuristic):
        heuristiques.change_heuristique(heuristic)

        if self.is_solution(env.all_nodes[0]):
            return env.all_nodes[0]



        return self.find_tree_solution(env.all_nodes[0])

solver = Solver()
