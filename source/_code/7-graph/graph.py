class Graph:
    def __init__(self):

        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])

    def add_vertex(self, vertex):

        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):

        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def delete_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def delete_vertex(self, vertex):
        if vertex not in self.adj_list:
            return False
        for other_vertex in self.adj_list[vertex]:
            self.adj_list[other_vertex].remove(vertex)
        del self.adj_list[vertex]
        return True


graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "C")
print("before delete vertex: ")
graph.print_graph()
graph.delete_vertex("D")
graph.delete_vertex("C")
print("after delete vertex: ")
graph.print_graph()
