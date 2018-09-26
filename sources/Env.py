
class Env:

	def __init__(self):
		self.size = 0
		self.all_nodes = []
		self.opened_nodes = {}
		self.closed_nodes = []

	def close_node(self, node):
		self.opened_nodes[node.fn].remove(node)
		self.closed_nodes.append(node)

	def add_open_node(self, node):
		self.opened_nodes.setdefault(node.fn, [])
		self.opened_nodes[node.fn].append(node)
		self.all_nodes.append(node)
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