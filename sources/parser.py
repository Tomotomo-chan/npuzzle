import argparse
import sys



parser = argparse.ArgumentParser()
parser.add_argument("-e","--heuristic", choices=["One","Two","Tree"], default="One", help="choose the heurtistic")
parser.add_argument("-f", "--file", type=file, help="read map, if empty read stdin")

args = parser.parse_args()

line_num = 0

if args.file:
    map = args.file
else:
    map = sys.stdin
for line in map:
    if (line_num == 0):
        if (line)

    print line,

r = r"(-?\d+)( *#.*)?"