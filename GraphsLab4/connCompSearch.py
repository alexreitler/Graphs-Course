from repo import Graph, RepositoryException


class BFSCompSearch:
    """


    """
    def __init__(self, graph):
        self.graph = graph
        self.comps = []

    def search(self):
        """

        :return:
        """
        print("Searching connected components....\n")
        searched = []
        to_search_all = list(self.graph.Din.keys())
        for vertex in to_search_all:
            if vertex not in searched:
                component = Graph()
                component.add_vertex(vertex)
                to_search_crt = self.graph.list_in_vert(vertex)
                searched.append(vertex)
                while len(to_search_crt) != 0:
                    while len(to_search_crt) and to_search_crt[0] in searched:
                        to_search_crt.pop(0)
                    if len(to_search_crt):
                        component.add_vertex(to_search_crt[0])
                        to_search_crt.extend(self.graph.Din[to_search_crt[0]])
                        searched.append(to_search_crt.pop(0))
                for key in list(component.Din.keys()):
                    for vertex2 in self.graph.Din[key]:
                        try:
                            component.add_edge(key, vertex2)
                        except RepositoryException as e:
                            pass
                self.comps.append(component)
        return self.comps
