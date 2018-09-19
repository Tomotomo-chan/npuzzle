
from Puzzle import Puzzle
from Node import Node
from Env import Env
from Heuristiques import *
import sys
import copy

class Solver:

    def __init__(self):
        self.fn_last_min = sys.maxint
        
    count = 0

    def find_tree_solution(self, node):
        print "--- working node ---"
        print node
        print "---"
        Solver.count += 1
        print Solver.count
        if node is None:
            return None
        available_movements = node.puzzle.get_available_movements(Puzzle.empty_piece)
        for m in available_movements:
            # print m
            tmp_puz = copy.deepcopy(node.puzzle)
            tmp_puz.apply_movement(Puzzle.empty_piece, m)
            # print "--- tmp puz ---"
            # print tmp_puz
            # print "---"
            if not self.puzzle_already_exist(tmp_puz):
                tmp_node = Node(node, tmp_puz, m)
                Env.all_nodes.append(tmp_node)
                print "--- node created ---"
                print m
                print tmp_node
                print "---"
                if self.is_solution(tmp_node):
                    print Solver.count
                    return tmp_node
        node.toggle_open(False)
        # for n in Env.all_nodes:
        #     print "---"
        #     print n.puzzle
        return self.find_tree_solution(self.find_node_fn_min())


    def find_node_fn_min(self):
        tmp_node = None
        for n in Env.all_nodes:
            if not n.open:
                continue
            if tmp_node is None:
                tmp_node = n
            elif n.fn < tmp_node.fn:
                tmp_node = n
            elif n.fn == tmp_node.fn and n.dist_heuristic < tmp_node.dist_heuristic:
                tmp_node = n
        return tmp_node



    def puzzle_already_exist(self, puzzle):
        for n in Env.all_nodes:
            if n.puzzle.hash == puzzle.hash:
                return True
        return False

    def is_solution(self, node):
        return node.dist_heuristic is 0

    def get_puzzle_solution(self, heuristic):
        heuristiques.change_heuristique(heuristic)

        return self.find_tree_solution(Env.all_nodes[0])

solver = Solver()
