import sys
import re
from Node import Node
from Env import env
from Puzzle import Puzzle

def parse_map(map):
    first = True
    
    puzzle = []

    for line in map:
        line_util = line.split('#')[0]
        if line_util == None or line_util == "":
            continue
        if first is not True:
            puzzle.append(parse_line(line_util))
            if (len(puzzle) > env.size):
                sys.stderr.write("Error: parsing map. Too many lines " + '\n')
                sys.exit()
        else:
            first = False
            parse_line(line_util)

    if (len(puzzle) < env.size):
        sys.stderr.write("Error: parsing map. Not Enought Lines " + '\n')
        sys.exit()

    parse_map_value(puzzle)
    env.all_nodes.append(Node(None, Puzzle(puzzle), None))

def to_int(char):
    return int(char)

def parse_line(line):
    if (len(re.findall(r"([^\d\s]+)", line)) > 0):
        sys.stderr.write("Error: parsing line (bad character found) " + line + '\n')
        sys.exit()

    m = re.findall(r"(\s*-?\d+)", line)
    if (parse_line.first is True):
        parse_line.first = False
        if len(m) != 1:
            sys.stderr.write("Error: parsing map. First Line must be the map size " + '\n')
            sys.exit()
        env.size = int(m[0])
    else:
        if len(m) < env.size:
            sys.stderr.write("Error: parsing map. not enought numbers at line : " + line + '\n')
            sys.exit()
        elif len(m) > env.size:
            sys.stderr.write("Error: parsing map. too many numbers at line : " + line + '\n')
            sys.exit()
        return [ to_int(num) for num in m ]

parse_line.first = True


def parse_map_value(puzzle):
    value = [0] * (env.size * env.size)
    for line in puzzle:
        for num in line:
            if num >= env.size * env.size:
                sys.stderr.write("Error: parsing map. value find to high : " + str(num) + '\n')
                sys.exit()
            if value[num] == 1:
                sys.stderr.write("Error: parsing map. value find multiple time : " + str(num) + '\n')
                sys.exit()
            value[num] = 1
    return

