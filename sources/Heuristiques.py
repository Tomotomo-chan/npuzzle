
from Puzzle import Puzzle
from PuzzleGenerator import puzzle_generator
from PuzzleCompare import puzzle_compare

class Heuristiques:


    def __init__(self):
        self.current_heuristique = ""
        self.default_puzzle = None
        self.default_is_before_table = []

    """ PRIVATE METHODS """

    def create_before_table(self, puzzle):
        ret = []
        for i in range(puzzle.size**2):
            for j in range(i, puzzle.size**2):
                if i != j:
                    ret.append(
                        self.is_before(
                            puzzle.get_piece_index(i),
                            puzzle.get_piece_index(j)
                        )
                    )
        return ret

    def is_before(self,index1, index2):
        if index1.line == index2.line:
            return index1.column < index2.column
        return index1.line < index2.line


    def check_default(self , puzzle):
        if self.default_puzzle == None or self.default_puzzle.size != puzzle.size:
            self.default_puzzle = puzzle_generator.generate_puzzle(puzzle.size)
        if self.current_heuristique == HeuristiquesType.melange and len(self.default_is_before_table) == 0:
            self.default_is_before_table = self.create_before_table(self.default_puzzle)

    def change_heuristique(self, heuristique):
        if self.current_heuristique is not heuristique:
            self.current_heuristique = heuristique
            self.default_is_before_table = []

    """ PUBLIC METHODS """

    def manhattan(self, puzzle):
        self.change_heuristique(HeuristiquesType.manhattan)
        self.check_default(puzzle)
        tot = 0
        for i in range(puzzle.size * puzzle.size):
            dist = puzzle_compare.nb_move_needed_for_value(i, self.default_puzzle, puzzle)
            tot += dist
        return tot

    def melange(self, puzzle):
        self.change_heuristique(HeuristiquesType.melange)
        self.check_default(puzzle)

        return is_before_table
    
class HeuristiquesType:
    manhattan = "manhattan"
    melange = "melange"

heuristiques = Heuristiques()

polo = puzzle_generator.generate_random_puzzle(3)
print polo
print str(heuristiques.manhattan(polo))