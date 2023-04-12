from repo import Graph, RepositoryException


class DAG:

    def __init__(self, graph):
        self.graph = graph
        self.sorted_graph = []
        self.the_queue = []
        self.count = {}
        self.highest_cost = 0
        self.highest_path = []

    def sort(self):
        for key in self.graph.Din:
            self.count[key] = len(self.graph.Din[key])
            if self.count[key] == 0:
                self.the_queue.append(key)
        while len(self.the_queue):
            x = self.the_queue.pop(0)
            self.sorted_graph.append(x)
            for y in self.graph.Dout(x):
                self.count[y] = self.count[y]-1
                if self.count[y] == 0:
                    self.the_queue.append(y)
        if len(self.sorted_graph) < self.graph.count_vertices():
            self.sorted_graph = None

        return self.sorted_graph

    def highest_cost_path(self, vertex1, vertex2):
        current_path = []
        current_cost = 0

    def rec_search(self, vertex1, vertex2, crt_path, crt_cost):
        current_path = crt_path
        for x in self.graph.Din[vertex2]:
            if x != vertex1:
                current_path.append(x)
                self.rec_search(vertex1, vertex2, current_path, crt_cost+self.graph.check_cost(x, current_path[-2]))
            else:
                if crt_cost+self.graph.check_cost(x, current_path[-1]) > self.highest_cost:
                    self.highest_cost = crt_cost+self.graph.check_cost(x, current_path[-1])
                    self.highest_path = current_path.reverse()+[x]
