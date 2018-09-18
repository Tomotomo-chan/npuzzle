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
from parser import parse_map
from PuzzleGenerator import puzzle_generator
from environment import Env
from node import Node
from Puzzle import Puzzle
import sys


""" Add arguments parsing """

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
#parser.add_argument("-e","--heuristic", choices=["One","Two","Tree"], default="One", help="choose the heurtistic")
group.add_argument("-f", "--file", type=file, help="read map from file")
group.add_argument("-i", "--stdin", action="store_true", help="read map on standard input")
args = parser.parse_args()

""" Create the first node from differents sources store it in the Env class """

if args.file:
    parse_map(args.file)
elif args.stdin:
    parse_map(sys.stdin)
else:
    Env.size = 4
    Env.first_node = Node(None, puzzle_generator.generate_random_puzzle(4), None)




