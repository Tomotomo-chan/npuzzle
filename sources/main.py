# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mressier <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/09/17 13:05:54 by mressier          #+#    #+#              #
#    Updated: 2018/09/17 13:05:55 by mressier         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import argparse
from Parser import parse_map
from PuzzleGenerator import puzzle_generator
from Env import env
from Node import Node
from Puzzle import Puzzle
from Solver import *
from Heuristiques import *
from PuzzleCompare import *
import sys
from Log import log

sys.setrecursionlimit(20000)

""" Add arguments parsing """

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
parser.add_argument("-m","--man", action="store_true")
group.add_argument("-f", "--file", type=file, help="read map from file")
group.add_argument("-i", "--stdin", action="store_true", help="read map on standard input")
args = parser.parse_args()

""" Create the first node from differents sources store it in the env class """

size = 0

if args.file:
    env.first_puzzle = parse_map(args.file)
elif args.stdin:
    env.first_puzzle = parse_map(sys.stdin) 
else:
    env.size = 4
    env.first_puzzle = puzzle_generator.generate_random_puzzle(env.size)

env.add_open_node(Node(None, env.first_puzzle, None))
heuristiques.init(env.size)

if puzzle_compare.is_solvable(env.first_puzzle, heuristiques.default_puzzle):
    print env.first_puzzle
    last_node_solution = solver.get_puzzle_solution(HeuristiquesType.manhattan)
    # """ chose de heuristic """
    # if (args.man):
    #     last_node_solution = solver.get_puzzle_solution(HeuristiquesType.manhattan)
    # else:
    #     last_node_solution = solver.get_puzzle_solution(HeuristiquesType.melange)
else:
    last_node_solution = None

if last_node_solution is None:
    log.error("Error: unsolvable map " + '\n')
    sys.exit(1)

print "--- Last Node ---"
print last_node_solution

sys.exit(0)

