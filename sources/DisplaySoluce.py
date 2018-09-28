from Node import *
from Heuristiques import *
from Env import *
from Log import *

def get_soluce_nodes(last_node):
	nodes = []
	node = last_node
	while (node):
		nodes.append(node)
		node = node.parent
	return reversed(nodes)

def soluce_to_string(soluce):
	string = ""
	for node in soluce:
		string += "\n" + node.movement + "\n" if node.movement is not None else ""
		string += str(node.puzzle)
		string += "\n"
	return string

def displaySoluce(all, last_node):
	log.default("\n_____Solution found_____")
	log.default("Heuristic : " + heuristiques.current_heuristique)
	log.default("Number of moves : " + str(last_node.dist_from_start))
	log.default("Total node created : " + str(env.nodes_count))
	log.default("Max opened nodes : " + str(env.max_opened_nodes))

	soluce = get_soluce_nodes(last_node)
	if all:
		log.default(soluce_to_string(soluce))
	else:
		log.file(soluce_to_string(soluce))
	return
