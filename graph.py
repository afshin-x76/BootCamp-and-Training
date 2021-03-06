class Element:
    def __init__(self, data):
        self.data = data

    def rename(self, new_name):
        self.data = new_name


class Graph:
    def __init__(self):
        self.adj_matrix = dict()
        self.final = []
        self.count = 0

    def add_node(self, node):
        if node in self.adj_matrix.keys():
            raise ValueError(f"{node} node exist")
        self.adj_matrix[node] = []

    def add_vertice(self, node_a, node_b):
        if not node_a in self.adj_matrix.keys():
            self.adj_matrix[node_a] = []
        if (node_a in self.adj_matrix[node_b]):
            raise ValueError(f"{node_a} and{node_b} are connected")
        self.adj_matrix[node_a].append(node_b)

    def deg_node(self, node):

        try:
            return len(self.adj_matrix[node])
        except Exception as e:
            raise e

    def __is_connected(self, start):
        if not self.adj_matrix[start]:
            return False
        for node in self.adj_matrix[start]:
            if node in self.keys:
                self.keys.remove(node)
            self.__is_connected(node)
        if not self.keys:
            return True
        else:
            return False

    def is_connected(self):
        self.keys = [i for i in self.adj_matrix.keys()]
        self.keys.remove("a")
        return self.__is_connected("a")


    def find_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in self.adj_matrix.keys():
            return None
        for node in self.adj_matrix[start]:
            if node not in path:
                newpath = self.find_path(node, end, path)
                if newpath:
                    if newpath not in self.final:
                        self.count += 1
                        self.final.append(newpath)
                    newpath =[]
        temp = []
        for i in self.final:
            if type(i[0]) != list:
                temp.append(i)

        return temp


    def shortest_path(self, start, end, path=[]):  # DFS
        paths = self.find_path(start, end)
        short = self.final[0]
        for i in paths:
            if len(i) < len(short):
                short = i
        return short

    def __str__(self):
        return str(self.adj_matrix)

    def rename_node(self, old_name, new_name):
        if old_name in self.adj_matrix.keys():
            for i in self.adj_matrix.keys():
                if i == old_name:
                    self.adj_matrix[new_name] = self.adj_matrix.pop(old_name)
                elif old_name in self.adj_matrix[i]:
                    self.adj_matrix[i].remove(old_name)
                    self.adj_matrix[i].append(new_name)
                
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
g.add_node("f")
g.add_node("j")
g.add_node("k")
g.add_node("l")
g.add_node("x")
g.add_node("n")
g.add_node("m")
g.add_node("s")






g.add_vertice("a", "b")
g.add_vertice("a", "e")
g.add_vertice("a", "f")
g.add_vertice("f", "k")
g.add_vertice("b", "j")
g.add_vertice("j", "l")
g.add_vertice("b", "x")
g.add_vertice("x", "k")
g.add_vertice("k", "n")
g.add_vertice("n", "m")





g.add_vertice("b", "c")
g.add_vertice("b", "d")

# print(g)

print(g.find_path("a", "m"))
print(g.shortest_path("a", "m"))
g.rename_node("d", "z")
# print(g)
print(g.is_connected())
