import argparse
import sys
import re


parser = argparse.ArgumentParser()
parser.add_argument("-e","--heuristic", choices=["One","Two","Tree"], default="One", help="choose the heurtistic")
parser.add_argument("-f", "--file", type=file, help="read map, if empty read stdin")
parser.add_argument("-g", "--graphic", action="store_true", help="if True use graphic NPuzzle")

args = parser.parse_args()

if args.file:
    map = args.file
else:
    map = sys.stdin

print '\n'

def parse:
    first = True
    size = 0
    puzzle


    for line in map:
        line_util = line.split('#')[0]
        parse_line(line_util, first)

    r = r"(\s*-?\d+)"

def parse_line(line, first):
    re 

