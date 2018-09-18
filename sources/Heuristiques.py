
from Puzzle import Puzzle
from PuzzleGenerator import puzzle_generator

class Heuristiques:

    default_puzzle = None

    def manhatan(self, puzzle):
        if Heuristiques.default_puzzle == None or Heuristiques.default_puzzle.size != puzzle.size:
            Heuristiques.default_puzzle = puzzle_generator.generate_puzzle(puzzle.size)
        tot = 0
        for i in range(0,puzzle.size * puzzle.size ):
            start = puzzle.get_piece_index(i)
            end = Heuristiques.default_puzzle.get_piece_index(i)
            dist = abs(start.line - end.line) + abs(start.column - end.column)
            tot += dist
            print "for " + str(i) + " : " + str(dist)

        print '\n'
        print str(puzzle)
        print '\n'
        print str(Heuristiques.default_puzzle)

        return tot

    def melange(puzzle):
        if default_puzzle == None:
            default_puzzle = puzzle_generator.generate_puzzle(puzzle.size)
        return


heuristiques = Heuristiques()
polo = Puzzle([[1,2,3],[4,5,6],[7,8,0]])
print "distances totales : " + str(heuristiques.manhatan(polo))