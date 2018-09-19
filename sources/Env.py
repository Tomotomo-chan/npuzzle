
class Env:

    def __init__(self):
        self.size = 0
        self.all_nodes = []
        self.open_nodes = []
        self.closed_nodes = []

    def close_node(self, node):
        self.open_nodes.remove(node)
        self.closed_nodes.append(node)

    def add_open_node(self, node):
        self.all_nodes.append(node)
        self.open_nodes.append(node)

env = Env()