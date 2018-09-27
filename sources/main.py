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
from DisplaySoluce import displaySoluce
import sys

""" Add arguments parsing """

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group2 = parser.add_mutually_exclusive_group()
group2.add_argument("-e1","--manhattan", action="store_true", help="heuristique manhattan")
group2.add_argument("-e2","--melange", action="store_true", help="heuristique melange")
group2.add_argument("-e3","--manhattan_square", action="store_true", help="heuristique manhattan square (default)")
group.add_argument("-f", "--file", type=file, help="read map from file")
group.add_argument("-i", "--stdin", action="store_true", help="read map on standard input")
parser.add_argument('map_size', type=int, nargs='?', default=3,
                    help='the size of the map we want to creat (default 3)')
parser.add_argument("-q","--quiet", action="store_true", help="if quiet, solution step by step will be store on soluce.txt")
args = parser.parse_args()

""" Create the first node from differents sources store it in the env class """

start_puzzle = None
size = 0

if args.file:
    start_puzzle = parse_map(args.file)
elif args.stdin:
    start_puzzle = parse_map(sys.stdin) 
else:
    env.size = args.map_size
    start_puzzle = puzzle_generator.generate_random_puzzle(env.size)

env.add_open_node( Node(None, start_puzzle, None))

heuristiques.init(env.size)

if puzzle_compare.is_solvable(env.all_nodes[0].puzzle, heuristiques.default_puzzle):
    print env.all_nodes[0].puzzle
    last_node_solution = solver.get_puzzle_solution(HeuristiquesType.manhattan)
    """ chose de heuristic """
    if args.manhattan:
        last_node_solution = solver.get_puzzle_solution(HeuristiquesType.manhattan)
    elif args.melange:
        last_node_solution = solver.get_puzzle_solution(HeuristiquesType.melange)
    else:
        last_node_solution = solver.get_puzzle_solution(HeuristiquesType.manhattan_square)
else:
    last_node_solution = None

if last_node_solution is None:
    sys.stderr.write("Error: unsolvable map " + '\n')
    sys.exit()


displaySoluce(args.quiet, last_node_solution)


