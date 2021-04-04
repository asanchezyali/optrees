from __future__ import annotations
import numpy as np


class Vertex:

    def __init__(self, label):
        self.__label = label
        self.__neighbors = dict()
        self.__edges = dict()

    @property
    def label(self) -> str:
        return self.__label

    @property
    def neighbors(self) -> dict:
        return self.__neighbors

    def add_neighbor(self, vertex: Vertex, weight: float = None):
        if self is not vertex:
            self.__neighbors[vertex.label] = vertex
            edge = Edge()
            edge.lvertex = self
            edge.rvertex = vertex
            edge.weight = weight
            edge.label = '{}-{}'.format(self.label, vertex.label)
            self.add_edge(edge)
        else:
            raise ValueError('It is the same vertex.')

    # TODO: Implement the delete method to neighbors.
    def del_neighbor(self):
        pass

    def neighbor(self, label: str) -> Vertex:
        return self.neighbors.get(label)

    @property
    def edges(self) -> dict:
        return self.__edges

    def add_edge(self, edge: Edge):
        if edge not in self.__edges.values() and edge.label not in self.__edges.keys():
            self.__edges[edge.label] = edge
        else:
            raise ValueError('This edge already exists.')

    def edge(self, label: str) -> str:
        return self.edges.get(label)


class Edge:

    def __init__(self, label, lvertex: Vertex = None, rvertex: Vertex = None, weight: float = None):
        self.__label = label
        self.__lvertex = lvertex
        self.__rvertex = rvertex
        self.__weight = weight

    @property
    def label(self) -> str:
        return self.__label

    @property
    def lvertex(self) -> Vertex:
        return self.__lvertex

    @lvertex.setter
    def lvertex(self, vertex: Vertex):
        if self.__lvertex is None:
            self.__lvertex = vertex
            vertex.add_edge(self)
        else:
            raise ValueError('This edge already has left vertex.')

    @property
    def rvertex(self) -> Vertex:
        return self.__rvertex

    @rvertex.setter
    def rvertex(self, vertex: Vertex):
        if self.__rvertex is None:
            self.__rvertex = vertex
            vertex.add_edge(self)
        else:
            raise ValueError('This edge already has right vertex.')

    @property
    def weight(self) -> float:
        return self.__weight

    @weight.setter
    def weight(self, weight: float):
        self.__weight = weight


class OrientedEdge(Edge):
    def __init__(self, label, start: Vertex = None, end: Vertex = None, weight: float = None):
        super().__init__(label=label, lvertex=start, rvertex=end, weight=weight)
        self.__start = super(OrientedEdge, self).lvertex
        self.__end = super(OrientedEdge, self).rvertex

    @property
    def start(self) -> Vertex:
        return self.__start

    @start.setter
    def start(self, vertex: Vertex):
        if self.__start is None:
            super(OrientedEdge, type(self)).lvertex.fset(self, vertex)
            self.__start = vertex
        else:
            raise ValueError('This edge already has start vertex.')

    @property
    def end(self) -> Vertex:
        return self.__end

    @end.setter
    def end(self, vertex: Vertex):
        if self.__end is None:
            super(OrientedEdge, type(self)).rvertex.fset(self, vertex)
            self.__end = vertex
        else:
            raise ValueError('This edge already has end vertex.')


class OrientedGraph:

    def __init__(self, name=None):
        self.__name = name
        self.__vertices = dict()
        self.__edges = dict()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def vertices(self):
        return self.__vertices

    @property
    def edges(self):
        return self.__edges

    def add_edges(self, edges):
        # TODO: Usar listas de tripletas (vertex_left, vertex_right, weight).
        vertex_left, vertex_right, weight = range(3)

        pass

    def add_vertex(self, neighbors=None):
        pass




class OrientedGraph2(object):
    """ This class defines the general structure for a graph. Initializes a
    graph object. If no dictionary or None is given, an empty dictionary will be
    used.

        Args:
            ``graph``: Dictionary with the relations among nodes. The keys
            of the dictionary are the node of the graph.  The corresponding
            values are list with nodes, which are connecting by an edge.

        Examples:
            For define a graph you should write a *dict* like this:

            .. code-block:: python

                graph = {
                    'a': [('c', 0)],
                    'b': [('c', 1), ('e', 3)],
                    'c': [('a', 3), ('b', 3), ('d', 2), ('e', 1)],
                    'f': None
                }

            contains the label from vertex neighbour and  weight for edge.
            When the value is None, then the node is isolated."""

    def __init__(self, graph: dict = None):
        # The class has the following information:
        self.vertices = dict()
        self.num_vertices = 0

        if graph is not None:
            self.add_structure(graph)

    def __contains__(self, vertex_id: str) -> bool:
        """ This method allow you to consult if a vertex belong to the graph.

        Args:
            ``vertex_id``: It is a vertex id.

        Returns:
            *bool*: It is a boolean.

        """
        return vertex_id in self.vertices.keys()

    def __iter__(self) -> iter:
        """ This method allows you to iterate over the nodes of the graph.

        Returns:
            *iter*: It is a list iterable of nodes.

        """
        return iter(self.vertices.values())

    # Adding new vertices to the graph:
    def add_vertex(self, vertex_id: str) -> Vertex:
        """ This method allows adding new vertices to the graph.

        Args:
            ``vertex_id`` (str): It is a string that is a vertex id.

        Returns:
            *Vertex*: It is a vertex object.
        """
        # Push a new vertex:
        self.num_vertices += 1
        new_vertex = Vertex(vertex_id)
        self.vertices[vertex_id] = new_vertex
        return new_vertex

    # TODO: Definir una función para remover vertices:
    def remove_vertex(self):
        pass

    # Consult a vertex by its id:
    def get_vertex(self, vertex_id: str) -> Vertex:
        """ This method allows you to obtain a vertex for id.

        Args:
            ``vertex_id`` (str): It is a string that is a vertex id.

        Returns:
            *Vertex*: It is a vertex object.
        """
        # Get the vertex:
        if vertex_id in self.vertices:
            return self.vertices.get(vertex_id)

    def get_vertices(self) -> list:
        """ This method allow you to consult all vertices in the graph.

        Returns:
            *list*: It is a list with all id vertices of the graph.
        """
        return list(self.vertices.keys())

    def add_edge(self, edge: tuple, weight: float = 0):
        """ This method allow you to add new edges to the graph.

        Args:
            ``edge`` (tuple): It is a tuple with the following structure:

            .. code-block:: python

                            edge = ('a', 'b')

            where entrances are vertex ids.
            ``weighing`` (float): It is a float with the weight between
            nodes of the edge.

        """
        # Rename the index for the list of vertices:
        (start_vertex, end_vertex) = range(2)

        # Consulting if there exist the vertex in the graph:
        if edge[start_vertex] in self.vertices:
            vertex_one = self.get_vertex(edge[start_vertex])
        else:
            vertex_one = self.add_vertex(edge[start_vertex])

        # Consulting if there exist the vertex in the graph:
        if edge[end_vertex] in self.vertices:
            vertex_two = self.get_vertex(edge[end_vertex])
        else:
            vertex_two = self.add_vertex(edge[end_vertex])

        vertex_one.add_neighbour(vertex_two, weight)
        vertex_two.add_neighbour(vertex_one, weight)

    # TODO: Definir una función para remover aristas.
    def remove_edge(self):
        pass

    def get_edges(self) -> tuple:
        """ This method is to find the edges of a graph.

        Returns:
            *edges*: list of tuples. The tuples are edges of the graph.
        """
        edges = list()
        vertices = self.vertices.values()

        # Consulting of the edges:
        for vertex in vertices:
            neighbours = vertex.neighbors()
            for neighbour_id in neighbours:
                # Weight:
                weight = vertex.get_weighing(neighbour_id)
                # Edges:
                edges.append((vertex.id, neighbour_id, weight))
        return edges, self

    def add_structure(self, graph: dict) -> None:
        """ Initializes a graph object. If no dictionary or None is given,
        an empty dictionary will be used.

        Args:
            ``graph``: Dictionary with the relations among nodes.  The keys
            of the dictionary are the node of the graph. The corresponding
            values are list with nodes, which are connecting by an edge.

        Examples:
            For define a graph you should write a dict like this:

            .. code-block:: python

                graph = {
                    'a': [('c', 0)],
                    'b': [('c', 1), ('e', 3)],
                    'c': [('a', 3), ('b', 3), ('d', 2), ('e', 1)],
                    'f': None
                }

            where the tuples contains the label from vertex end and weight
            for edge.
        """
        (vertex_id, weight) = range(2)

        # Push a structure to graph:
        for start_vertex in graph:
            if graph[start_vertex] is not None:
                for end_vertex in graph[start_vertex]:
                    edge = (start_vertex, end_vertex[vertex_id])
                    weighing = end_vertex[weight]
                    self.add_edge(edge, weighing)
            else:
                self.add_vertex(start_vertex)

    # TODO: Mejorar esta función para detectar los nodos que no tienen ni entradas ni salidas.
    def isolated_vertex(self) -> list:
        """ This method is allows you to find the isolated nodes in a graph.

        Returns:
            *list*: Returns a list with isolated nodes in a graph.
        """
        isolated = list()

        # Consulting the isolated nodes:
        for vertex in self.vertices.values():
            if not vertex.neighbors():
                isolated.append(vertex.id)
        return isolated

    # TODO: Encontrar nodos colgantes.

    def adjacency_matrix(self) -> tuple:
        vertices = self.vertices.values()
        size = len(vertices)
        matrix = np.zeros((size, size))

        for i, row_vertex in enumerate(vertices):
            for j, col_vertex in enumerate(vertices):
                if col_vertex.id in row_vertex.neighbors():
                    matrix[i, j] = 1
                    matrix[j, i] = 1
                else:
                    matrix[i, j] = 0
                    matrix[j, i] = 0

        indices = self.vertices.keys()
        return matrix, list(indices)

    def weight_matrix(self) -> tuple:
        vertices = self.vertices.values()
        matrix = list()
        for row_vertex in vertices:
            row = list()
            for col_vertex in vertices:
                if col_vertex.id in row_vertex.neighbors():
                    row.append(row_vertex.get_weighing(col_vertex.id))
                else:
                    row.append(np.infty)
            matrix.append(row)
        indices = self.vertices.keys()
        return np.matrix(matrix), list(indices)


class NotOrientedGraph(OrientedGraph):

    def get_edges(self) -> tuple:
        """
        This method is to find the edges of a graph.

        Returns:
            edges: list of tuples. The tuples are edges of the graph.
        """

        edges = list()
        vertices = self.vertices.values()

        # Consulting of the edges:
        for vertex in vertices:
            neighbours = vertex.neighbors()
            for neighbour_id in neighbours:
                # Weight:
                weight = vertex.get_weighing(neighbour_id)
                # Edges:
                edges.append((vertex.id, neighbour_id, weight))

        return edges, NotOrientedGraph


