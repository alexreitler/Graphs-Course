class RepositoryException(Exception):
    pass


class Graph:
    """
    Implementation of the Graph.
    Uses three dictionaries for storing values.
    Din and Dout have all existing vertices as keys, and a corresponding list of inbound / outbound vertices as values
    Dcost has a pairs of two vertices as keys, and integers as values
    """
    def __init__(self):
        self.Din = {}
        self.Dcost = {}

    def count_vertices(self):
        """
        Simply returns the number of vertices in the matrix
        :return: integer
        """
        number = len(self.Din.keys())
        return number

    def count_edges(self):
        """
        Returns number of edges in matrix
        :return: integer
        """
        number = 0
        for key in self.Din.keys():
            number += len(self.Din[key])
        return number

    def list_isolated_vert(self):
        """
        Returns a list of vertices with no inbound or outbound edges
        :return: a list of integers
        """
        vertex_list = []
        for key in self.Din:
            if not self.Din[key]:
                vertex_list.append(key)
        return vertex_list

    def list_in_vert(self, vertex):
        """
        Returns list of inbound edges of a vertex
        :param vertex: integer
        :return: a list of integers
        """
        return self.Din[vertex]

    def add_vertex(self, vertex):
        """
        Adds a vertex to the Graph
        Checks if vertex already exists
        :param vertex: integer
        :return: RepositoryException if vertex exists
        """
        if not self.check_vertex(vertex):
            self.Din[vertex] = []
        else:
            raise RepositoryException("Vertex exists")

    def check_vertex(self, vertex):
        """
        Checks if vertex already exists
        :param vertex: integer
        :return: RepositoryException if vertex exists
        """
        if vertex in self.Din:
            return True
        else:
            return False

    def delete_vertex(self, vertex):
        """
        Deletes a vertex from the Graph
        Checks if vertex doesn't exist
        Also deletes all edges connected to said vertex
        :param vertex: integer
        :return: RepositoryException if vertex doesn't exist
        """
        if self.check_vertex(vertex):

            for i in self.Din[vertex]:
                self.Dcost.pop((i, vertex))
                self.Din[i].remove(vertex)
            self.Din.pop(vertex)
        else:
            raise RepositoryException("Vertex does not exist")

    def check_cost(self, vertex1, vertex2):
        """
        This function return the cost of an edge
        :param vertex1: integer
        :param vertex2: integer
        :return: integer
        """
        if not (vertex1, vertex2) in self.Dcost:
            raise RepositoryException("Edge does not exist")
        else:
            return self.Dcost[(vertex1, vertex2)]

    def add_cost(self, vertex1, vertex2, cost):
        """
        This function add a cost to an edge
        Checks if edge exists
        :param vertex1: integer
        :param vertex2: integer
        :param cost: integer
        :return: RepositoryException if edge doesn't exist
        """
        if self.check_edge(vertex1, vertex2):
            self.Dcost[(vertex1, vertex2)] = cost
        else:
            raise RepositoryException("Edge does not exist")

    def delete_cost(self, vertex1, vertex2):
        """
        This function deletes a cost from an edge
        Checks if edge exists
        :param vertex1: integer
        :param vertex2: integer
        :return: RepositoryException if edge doesn't exist
        """
        if self.check_cost(vertex1, vertex2) is not False:
            self.Dcost.pop((vertex1, vertex2))
        else:
            raise RepositoryException("Edge does not exist")

    def check_edge(self, vertex1, vertex2):
        """
        This function checks if an edge exists
        :param vertex1: integer
        :param vertex2: integer
        :return: boolean
        """
        if self.check_vertex(vertex1) and self.check_vertex(vertex2):
            if vertex1 in self.Din[vertex2]:
                return True
            else:
                return False
        else:
            return False

    def add_edge(self, vertex1, vertex2):
        """
        This function adds an edge to the graph
        Checks if edge already exists
        :param vertex1: integer
        :param vertex2: integer
        :return: nothing
        """
        if not self.check_edge(vertex1, vertex2):
            self.Din[vertex2].append(vertex1)
            self.Din[vertex1].append(vertex2)
        else:
            raise RepositoryException("Edge exists")

    def delete_edge(self, vertex1, vertex2):
        """
        This function deletes an edge from the graph
        Checks if edge exists
        :param vertex1: integer
        :param vertex2: integer
        :return: nothing
        """
        if self.check_edge(vertex1, vertex2):
            self.Din[vertex2].remove(vertex1)
            self.Dcost.pop((vertex1, vertex2))
        else:
            raise RepositoryException("Edge does not exist")


class EdgeIterator:
    """
    This class is an iterator, iterating over a list representing inbound or outbound edges
    """
    def __init__(self, vertex_list):
        self.list = vertex_list
        self.value = 0
        self.end = len(vertex_list)

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.list[self.value]
        self.value += 1
        return current


class VertexIterator:
    """
    This class is an iterator, iterating over a list representing inbound or outbound edges
    """
    def __init__(self, graph):
        self.list = graph.Din
        self.value = 0
        self.end = len(self.list)

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.list[self.value]
        self.value += 1
        return current
