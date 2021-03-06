class Graph:
    def __init__(self):
        self.adj_matrix = dict()

    def add_node(self, node):
        if node in self.adj_matrix.keys():
            raise ValueError(f"{node} node exist")
        self.adj_matrix[node] = []

    def add_vertice(self, node_a, node_b):
        if not node_a in self.adj_matrix.keys():
            self.adj_matrix[node_a] = []
        if not node_b in self.adj_matrix.keys():
            self.adj_matrix[node_b] = []

        if (node_a in self.adj_matrix[node_b]) or (node_b in self.adj_matrix[node_a]):
            raise ValueError(f"{node_a} and{node_b} are connected")

        self.adj_matrix[node_a].append(node_b)
        self.adj_matrix[node_b].append(node_a)

    def deg_node(self, node):

        try:
            return len(self.adj_matrix[node])
        except Exception as e:
            raise e

    def is_connected(self):
        pass

    def find_path(self, node_a, node_b):
        pass

    def shortest_path(self, node_a, node_b):  # DFS
        pass

    def __str__(self):
        return str(self.adj_matrix)

    def rename_node(self, old_name, new_name):
        if old_name in self.adj_matrix:
            for i in self.adj_matrix.keys():
                if i == old_name:
                    self.adj_matrix[new_name] = [j for j in self.adj_matrix[old_name]]
                else:
                    if old_name in self.adj_matrix[i]:
                        for k in self.adj_matrix[i]:
                            if k==old_name:
                                print(k)

        else:
            raise ValueError(f"there is no {old_name} node in this graph")


class DirectedGraph(Graph):
    def add_vertice(self, node_a, node_b):
        if not node_a in self.adj_matrix.keys():
            self.adj_matrix[node_a] = []
        if not node_b in self.adj_matrix.keys():
            self.adj_matrix[node_b] = []

        if node_a in self.adj_matrix[node_b]:
            raise ValueError(f"{node_a} cinnected to {node_b}")

        self.adj_matrix[node_a].append(node_b)


g = Graph()

g.add_node("a")
g.add_node("b")
g.add_node("c")
g.add_node("d")
g.add_node("e")

g.add_vertice("a", "b")
g.add_vertice("a", "e")
g.add_vertice("c", "b")
g.add_vertice("c", "e")

print(g.deg_node("b"))
print(g)