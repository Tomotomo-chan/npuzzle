from Node import *
from Heuristiques import *
from Env import *

def displaySoluce(all, last_node):
	print "\n_____One solution found_____"
	print "heuristic : " + heuristiques.current_heuristique
	print "number of moves : " + str(last_node.dist_from_start)
	print "total node created : " + str(env.all_nodes.__len__())
	node = last_node
	res = []
	file = open("soluce.txt","w")
	while (node):
		res.append(node)
		node = node.parent
	i = res.__len__()
	# while (i != 0):
	# 	print "\n" + str(res[i - i])
	# 	i -= 1
	while i != 0:
		if all:
			file.write(res[i-1].__str__())
			file.write('\n\n')
		else:
			print res[i-1]
			print '\n'
		i -= 1

	file.close()
