
class Env:

	def __init__(self):
		self.size = 0
		self.first_puzzle = None
		self.opened_nodes = {0: []} # {heuristique_value: [nodes_with_this_heuristic]}
		self.closed_nodes_count = 0
		self.nodes_count = 0

	def close_node(self, node):
		self.opened_nodes[node.fn].remove(node)
		self.closed_nodes_count += 1

	def add_open_node(self, node):
		self.opened_nodes.setdefault(node.fn, [])
		self.opened_nodes[node.fn].append(node)
		self.nodes_count += 1
		return

	def get_smaller_nodes(self):
		smaller = None
		for (value, nodes) in self.opened_nodes.items():
			if smaller is None and len(nodes) > 0:
				smaller = value
			elif value < smaller and len(nodes) > 0:
				smaller = value
		return self.opened_nodes[smaller]

env = Env()