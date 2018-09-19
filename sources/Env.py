
class Env:

	def __init__(self):
		self.size = 0
		self.all_nodes = []
		self.opened_nodes = []
		self.closed_nodes = []

	def close_node(self, node):
		self.opened_nodes.remove(node)
		self.closed_nodes.append(node)

	def add_open_node(self, node):
		if not self.node_exist(node):
			self.all_nodes.append(node)
			self.opened_nodes.append(node)
		return

	def node_exist(self, new_node):
		for node in self.opened_nodes + self.closed_nodes:
			 if node.puzzle.hash == new_node.puzzle.hash:
				 return True
		return False

env = Env()