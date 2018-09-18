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
import sys

parser = argparse.ArgumentParser()
#parser.add_argument("-e","--heuristic", choices=["One","Two","Tree"], default="One", help="choose the heurtistic")
parser.add_argument("-f", "--file", type=file, help="read map, if empty read stdin")
args = parser.parse_args()

if args.file:
   parse_map(args.file)





