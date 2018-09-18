import argparse
import sys
import re
from node import Node

parser = argparse.ArgumentParser()
parser.add_argument("-e","--heuristic", choices=["One","Two","Tree"], default="One", help="choose the heurtistic")
parser.add_argument("-f", "--file", type=file, help="read map, if empty read stdin")
parser.add_argument("-g", "--graphic", action="store_true", help="if True use graphic NPuzzle")

args = parser.parse_args()

if args.file:
    map = args.file
else:
    map = sys.stdin


class Env:
    size = 0
    first_node = None

def parse_map(map):
    first = True
    
    puzzle = []

    for line in map:
        line_util = line.split('#')[0]
        if first is not True:
            puzzle.append(parse_line(line_util))
            if (len(puzzle) > Env.size):
                sys.stderr.write("Error: parsing map. Too many lines ")
                sys.exit()
        else:
            first = False
            parse_line(line_util)

    if (len(puzzle) < Env.size):
        sys.stderr.write("Error: parsing map. Not Enought Lines ")
        sys.exit()

    parse_map_value(puzzle)
    Env.first_node = Node(None, puzzle, None )

def to_int(char):
    return int(char)

def parse_line(line):
    if (len(re.findall(r"([^\d\s]+)", line)) > 0):
        sys.stderr.write("Error: parsing line (bad character found) " + line)
        sys.exit()

    m = re.findall(r"(\s*-?\d+)", line)
    if (parse_line.first is True):
        parse_line.first = False
        if len(m) != 1:
            sys.stderr.write("Error: parsing map. First Line must be the map size ")
            sys.exit()
        Env.size = int(m[0])
    else:
        if len(m) < Env.size:
            sys.stderr.write("Error: parsing map. not enought numbers at line : " + line)
            sys.exit()
        elif len(m) > Env.size:
            sys.stderr.write("Error: parsing map. too many numbers at line : " + line)
            sys.exit()
        return [ to_int(num) for num in m ]

parse_line.first = True


def parse_map_value(puzzle):
    value = [0] * (Env.size * Env.size)
    for line in puzzle:
        for num in line:
            if num >= Env.size * Env.size:
                sys.stderr.write("Error: parsing map. value find to high : " + str(num))
                sys.exit()
            if value[num] == 1:
                sys.stderr.write("Error: parsing map. value find multiple time : " + str(num))
                sys.exit()
            value[num] = 1
    return

parse_map(map)
