from repo import Graph, RepositoryException


class Hamiltonian:
    def __init__(self, graph):
        self.graph = graph
        self.ham_cycle = []

    def search_hamiltonian(self):
        for x in self.graph.Din:
            current_cycle = [x]
            self.rec_search(x, current_cycle)
            break

    def rec_search(self, vertex, crt_cycle):
        for x in self.graph.Din[vertex]:
            if x == crt_cycle[0] and len(crt_cycle) == self.graph.count_vertices():
                self.ham_cycle = (crt_cycle + [x])[:]
            else:
                if x not in crt_cycle:
                    current_cycle = (crt_cycle + [x])[:]
                    self.rec_search(x, current_cycle)
