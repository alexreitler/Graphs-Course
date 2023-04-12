from repo import *
from connCompSearch import BFSCompSearch
from lowCostWalks import LowCostWalks
from DAG import DAG
import random


class UI:
    """
    This is the Main UI function
    """
    def __init__(self, repo):
        self._repo = repo

    def console(self):
        """
        This function lets the user choose one of the listed options
        :return: nothing
        """
        while True:
            print("0. Read&Write")
            print("1. Check number of vertices")
            print("2. Check number of edges")
            print("3. Create random graph")
            print("4. Add vertex")
            print("5. Check vertex existence")
            print("6. Delete vertex")
            print("7. Add edge")
            print("8. Check edge existence")
            print("9. Delete edge")
            print("10. Add / Change Cost")
            print("11. Vertex Degree")
            # print("12. List outbound")
            print("13. List inbound")
            print("14. Find connected components")
            print("15. Find lowest cost walk")
            print("16. Check if DAG and sort")
            print("17. Find highest cost path")
            print("18. Exit")
            try:
                user_input = int(input("Choose  an option (number between 0 and 16):"))
                if user_input == 0:
                    self.file_io()
                elif user_input == 1:
                    self.count_vertices()
                elif user_input == 2:
                    self.count_edges()
                elif user_input == 3:
                    self.create_random()
                elif user_input == 4:
                    self.add_vertex()
                elif user_input == 5:
                    self.check_vertex()
                elif user_input == 6:
                    self.del_vertex()
                elif user_input == 7:
                    self.add_edge()
                elif user_input == 8:
                    self.check_edge()
                elif user_input == 9:
                    self.del_edge()
                elif user_input == 10:
                    self.change_cost()
                elif user_input == 11:
                    self.list_degree()
                elif user_input == 12:
                    self.list_outbound()
                elif user_input == 13:
                    self.list_inbound()
                elif user_input == 14:
                    self.conn_comps()
                elif user_input == 15:
                    self.walk_search()
                elif user_input == 16:
                    self.check_dag()
                elif user_input == 17:
                    self.highest_cost_path()
                elif user_input == 18:
                    break
                elif user_input == 19:
                    self.print_graph(self._repo)

            except ValueError as ve:
                print("Please write an integer" + str(ve))
            # except Exception as e:
            #    print(e)
            input("Press Enter to continue...")

    def count_vertices(self):
        """
        This function prints the number of vertices
        :return: nothing
        """
        print(self._repo.count_vertices())

    def count_edges(self):
        """
        This function returns the number of edges
        :return: nothing
        """
        print(self._repo.count_edges())

    def add_vertex(self):
        """
        Adds a vertex using add_vertex from repo
        :return: nothing
        """
        vertex = int(input("Vertex:"))
        self._repo.add_vertex(vertex)

    def check_vertex(self):
        """
        This function checks existence of a vertex
        :return: nothing, and result is printed in console
        """
        vertex = int(input("Vertex:"))
        print(self._repo.check_vertex(vertex))

    def del_vertex(self):
        """
        This function deletes a vertex
        :return: nothing
        """
        vertex = int(input("Vertex:"))
        self._repo.delete_vertex(vertex)

    def add_edge(self):
        """
        This function adds an edge using add_edge repo function
        :return: nothing
        """
        vertex1 = int(input("Vertex1:"))
        vertex2 = int(input("Vertex2:"))
        self._repo.add_edge(vertex1, vertex2)

    def check_edge(self):
        """
        This function checks existence of an edge
        :return: nothing, result is printed in console
        """
        vertex1 = int(input("Vertex1:"))
        vertex2 = int(input("Vertex2:"))
        print(self._repo.check_edge(vertex1, vertex2))

    def del_edge(self):
        """
        This function deletes an edge
        :return: nothing
        """
        vertex1 = int(input("Vertex1:"))
        vertex2 = int(input("Vertex2:"))
        self._repo.delete_edge(vertex1, vertex2)

    def change_cost(self):
        """
        This function modifies the cost of an edge
        :return: nothing
        """
        vertex1 = int(input("Vertex1:"))
        vertex2 = int(input("Vertex2:"))
        cost = int(input("Cost:"))
        self._repo.add_cost(vertex1, vertex2, cost)

    def list_inbound(self):
        """
        This function prints inbound vertices of given vertex
        :return: nothing
        """
        vertex = int(input("Vertex:"))
        iterator = EdgeIterator(self._repo.list_in_vert(vertex))
        for vertex in iterator:
            print(vertex, end=" ")
        print()

    def list_inbound_nr(self, vertex):
        """
        This function prints the inbound degree of a vertex
        :param vertex: integer
        :return: nothing
        """
        print(len(self._repo.list_in_vert(vertex)))

    def list_outbound(self):
        """
        This function prints outbound vertices of given vertex
        :return: nothing
        """
        vertex = int(input("Vertex:"))
        iterator = EdgeIterator(self._repo.list_out_vert(vertex))
        for vertex in iterator:
            print(vertex, end=" ")
        print()

    def list_outbound_nr(self, vertex):
        """
        This function prints the outbound degree of a vertex
        :param vertex: integer
        :return: nothing
        """
        print(len(self._repo.list_out_vert(vertex)))

    def list_degree(self):
        """
        This function prints the inbound and outbound degrees of a vertex
        :return: False if vertex does not exist
        """
        vertex = int(input("Vertex:"))
        if not self._repo.check_vertex(vertex):
            print("Vertex does not exist")
            return False
        print("Inbound:")
        self.list_inbound_nr(vertex)
        print("Outbound:")
        self.list_outbound_nr(vertex)

    def conn_comps(self):
        conn_search = BFSCompSearch(self._repo)
        result = conn_search.search()
        print("There are", len(result), "connected components")
        for comp in result:
            self.print_graph(comp)

    def walk_search(self):
        walk_search = LowCostWalks(self._repo)
        start_vertex = int(input("Input start vertex:"))
        end_vertex = int(input("Input end vertex:"))
        walk_search.search(start_vertex, end_vertex)
        print("Lowest cost: ", walk_search.lowestCost)
        print("Lowest walk: ", walk_search.lowestWalk)

    def check_dag(self):
        dag = DAG(self._repo)
        sorted_graph = dag.sort()
        if sorted_graph is not None:
            print("It is a DAG, sorted:", sorted_graph, "\n")
        else:
            print("Not a Dag\n")

    def highest_cost_path(self):
        dag = DAG(self._repo)
        vertex1 = int(input("Give the first vertex:"))
        vertex2 = int(input("Give the second vertex:"))
        dag.highest_cost_path(vertex1, vertex2)
        if dag.highest_path is None or len(dag.highest_path) == 0:
            print("No path")
        else:
            print("The path is ", dag.highest_path, " with cost: ", dag.highest_cost)

    @staticmethod
    def print_graph(graph):
        """
        This function prints the whole graph. Do not use this.
        :return: nothing
        """
        print(graph.Dcost)
        print(graph.Din)

    def file_io(self):
        """
        This function lets the user choose IO operations
        :return: nothing
        """
        while True:
            print("0. Read small graph")
            print("1. Read original 1k")
            print("2. Read original 10k")
            print("3. Read original 100k")
            print("4. Read modified 1k")
            print("5. Read modified 10k")
            print("6. Read modified 100k")
            print("7. Write 1k")
            print("8. Write 10k")
            print("9. Write 100k")
            print("10. Exit")
            try:
                user_input = int(input("Choose  an option (number between 1 and 10):"))
                if user_input == 0:
                    self.readsmall()
                    break
                if user_input == 1:
                    self.read1k()
                    break
                elif user_input == 2:
                    self.read10k()
                    break
                elif user_input == 3:
                    self.read100k()
                    break
                elif user_input == 4:
                    self.read1k_modified()
                    break
                elif user_input == 5:
                    self.read10k_modified()
                    break
                elif user_input == 6:
                    self.read100k_modified()
                    break
                elif user_input == 7:
                    self.write1k()
                elif user_input == 8:
                    self.write10k()
                elif user_input == 9:
                    self.write100k()
                elif user_input == 10:
                    break

            except ValueError as ve:
                print("Please write an integer" + str(ve))
            except Exception as e:
                print(e)

    def readsmall(self):
        """
        This function reads a graph from file graph1k.txt
        :return: nothing
        """
        self.file_read_original("graph.txt")

    def read1k(self):
        """
        This function reads a graph from file graph1k.txt
        :return: nothing
        """
        self.file_read_original("graph1k.txt")

    def read10k(self):
        """
        This function reads a graph from file graph10k.txt
        :return: nothing
        """
        self.file_read_original("graph10k.txt")

    def read100k(self):
        """
        This function reads a graph from file graph100k.txt
        :return: nothing
        """
        self.file_read_original("graph100k.txt")

    def read1k_modified(self):
        """
        This function reads a graph from file graph1knew.txt
        :return: nothing
        """
        self.file_read_original("graph1knew.txt")

    def read10k_modified(self):
        """
        This function reads a graph from file graph10knew.txt
        :return: nothing
        """
        self.file_read_original("graph10knew.txt")

    def read100k_modified(self):
        """
        This function reads a graph from file graph100knew.txt
        :return: nothing
        """
        self.file_read_original("graph100knew.txt")

    def write1k(self):
        """
        This function writes the graph to graph1knew.txt
        :return: nothing
        """
        self.file_write("graph1knew.txt")

    def write10k(self):
        """
        This function writes the graph to graph10knew.txt
        :return: nothing
        """
        self.file_write("graph10knew.txt")

    def write100k(self):
        """
        This function writes the graph to graph100knew.txt
        :return: nothing
        """
        self.file_write("graph100knew.txt")

    def create_random(self):
        """
        This function generates a random Graph after reading number of vertices and Edges from the console
        :return:
        """
        vertex = int(input("Enter number of vertices:"))
        edge = int(input("Enter number of edges:"))
        if edge > vertex*(vertex+2):
            print("Graph impossible")
            return 0

        for i in range(vertex):
            self._repo.add_vertex(i)
        i = 0
        while i < edge:
            vertex1 = random.randint(0, vertex-1)
            vertex2 = random.randint(0, vertex-1)
            if not self._repo.check_edge(vertex1, vertex2):
                self._repo.add_edge(vertex1, vertex2)
                self._repo.add_cost(vertex1, vertex2, random.randint(1, 10))
                i += 1

    def file_read_original(self, file):
        """
        This function reads files in the original format
        :param file: the file to read from
        :return: nothing
        """
        try:
            f = open(file, "r")
            line = f.readline().split(" ")
            for i in range(int(line[0])):
                self._repo.add_vertex(i)
            for i in range(int(line[1])):
                line = f.readline().split(" ")
                try:
                    self._repo.add_edge(int(line[0]), int(line[1]))
                except RepositoryException as e:
                    pass
                self._repo.add_cost(int(line[0]), int(line[1]), int(line[2]))
            f.close()
        except IOError as e:
            print("An error occurred:\n")
            raise RepositoryException(e)

    def file_read_new(self, file):
        """
        This function reads a graph from files written by the program
        :param file: the file to read from
        :return: nothing
        """
        try:
            f = open(file, "r")
            line = f.readline().split(" ")
            while len(line) > 1:
                self._repo.add_edge(line[0], line[1])
                self._repo.add_cost(line[0], line[1], line[2])
                line = f.readline().split(" ")
            line = f.readline().split(" ")
            line = f.readline().split(" ")
            for element in line:
                self._repo.add_vertex(element)
            f.close()
        except IOError as e:
            raise RepositoryException(e)

    def file_write(self, file):
        """
        Writes Graph to file like this:
        Three values on each row, the first two represent the ends of an edge, the third is the cost
        Then if there are any remaining vertices with no edges, they are listed at the end of the file
        :param file: the file to write to
        :return: nothing
        """
        try:
            f = open(file, "w")
            for key in VertexIterator(self._repo):
                for vertex in self._repo.list_out_vert(key):
                    f.write(str(key)+" "+str(vertex)+" "+str(self._repo.check_cost(key, vertex)+"\n"))
            f.write("\n")
            for vertex in self._repo.list_isolated_vert():
                f.write(str(vertex)+" ")
            f.write("\n")
            f.close()
        except IOError as e:
            raise RepositoryException(e)
