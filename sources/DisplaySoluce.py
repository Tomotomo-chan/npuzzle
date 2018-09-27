from Node import *
from Heuristiques import *
from Env import *

def displaySoluce(all, last_node):
	print "\n_____One solution found_____"
	print "heuristic : " + heuristiques.current_heuristique
	print "number of moves : " + str(last_node.dist_from_start)
	print "total node created : " + str(len(env.all_nodes))
	node = last_node
	res = []
	file = open("soluce.txt","w")
	while (node):
		res.append(node)
		node = node.parent
	# i = len(res)
	# while (i != 0):
	# 	print "\n" + str(res[i - i])
	# 	i -= 1
	for state in reversed(res):
		if all:
			if state.movement:
				file.write(str(state.movement))
			file.write(str(state.puzzle))
			file.write('\n')
		else:
			if state.movement:
				print state.movement
			print state.puzzle
			print '\n'

	file.close()
