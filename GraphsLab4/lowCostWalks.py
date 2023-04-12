from functools import lru_cache

from repo import Graph, RepositoryException


class LowCostWalks:
    """
    Write a program that, given a graph with costs and two vertices, finds
    the lowest cost walk between the given vertices,
    or prints a message if there are negative cost cycles accessible from the starting vertex.
    The program will use a matrix defined as d[x,k]=the cost of the lowest cost walk
    from s to x and of length at most k, where s is the starting vertex.
    """

    def __init__(self, graph):
        self.graph = graph
        self.Walks = [[]] * self.graph.count_vertices()
        self.lowestWalk = []
        self.lowestCost = None

    def search(self, start_vertex, end_vertex):
        """


        :return:
        """
        if start_vertex == end_vertex:
            raise RepositoryException("Start and end vertices cannot be the same")
        else:
            self.recursive_search(start_vertex, end_vertex, 0, 0, [])

    # @lru_cache(maxsize=None)
    def recursive_search(self, start_vertex, end_vertex, crt_cost, crt_len, visited):
        """

        :return:
        """
        if len(visited) > 0:
            crt_cost += self.graph.check_cost(visited[-1], start_vertex)
        new_visited = visited + [start_vertex]
        for vertex in self.graph.list_out_vert(start_vertex):
            # check negative cost cycle
            if vertex in new_visited:
                if vertex != new_visited[-2] and vertex != new_visited[-1]:
                    cycle_sum = 0
                    cycle_sum += self.graph.check_cost(vertex, new_visited[-1])
                    i = len(new_visited) - 1
                    while new_visited[i] != vertex:
                        cycle_sum += self.graph.check_cost(new_visited[i], new_visited[i - 1])
                        i -= 1
                    if cycle_sum < 0:
                        raise RepositoryException("Negative cost cycle exists")
            else:
                # if at the end, check if lowest cost
                if vertex == end_vertex:
                    if self.lowestCost is None or self.lowestCost > crt_cost + self.graph.check_cost(new_visited[-1],
                                                                                                     end_vertex):
                        self.lowestCost = crt_cost + self.graph.check_cost(new_visited[-1], end_vertex)
                        self.lowestWalk = new_visited + [end_vertex]

                else:
                    if self.lowestCost is None or self.lowestCost > crt_cost + self.graph.check_cost(new_visited[-1],
                                                                                                     vertex):
                        self.recursive_search(vertex, end_vertex, crt_cost, crt_len + 1, new_visited)
