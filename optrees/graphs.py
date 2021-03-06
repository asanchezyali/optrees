from __future__ import annotations

import numpy as np


class Vertex:

    def __init__(self, label: str):
        self.__label = label
        self.__neighbors = dict()
        self.__edges = dict()
        self.__loops = dict()

    @property
    def label(self) -> str:
        return self.__label

    @property
    def neighbors(self) -> dict:
        return self.__neighbors

    def add_neighbor(self, vertex: Vertex, weight: float = None):
        if self is not vertex:
            self.__neighbors[vertex.label] = vertex
            edge = Edge(label='{}-{}'.format(self.label, vertex.label), lvertex=self, rvertex=vertex)
            edge.weight = weight
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
        if edge not in self.__edges.values() and edge.label not in self.__edges.keys() and not edge.loop:
            self.__edges[edge.label] = edge
        elif edge.loop and edge.label not in self.__edges.keys() and edge not in self.__edges.values():
            self.__loops[edge.label] = edge
            self.__edges[edge.label] = edge
        elif edge.loop and edge.label in self.__edges.keys() and edge in self.__edges.values():
            pass
        else:
            raise ValueError('This edge already exists')

    def edge(self, label: str) -> str:
        return self.edges.get(label)

    @property
    def loops(self) -> dict:
        return self.__loops

    def loop(self, label: str) -> str:
        return self.loops.get(label)


class Edge:

    def __init__(self, label: str, lvertex: Vertex, rvertex: Vertex, weight: float = None, orientation: str = None):
        orientations = {'lr': {'start': lvertex, 'end': rvertex}, 'rl': {'start': rvertex, 'end': lvertex}}
        self.__label = label
        self.__lvertex = lvertex
        self.__rvertex = rvertex
        self.__weight = weight
        self.__start = None if orientation not in ['lr', 'rl'] else orientations.get(orientation).get('start')
        self.__end = None if orientation not in ['lr', 'rl'] else orientations.get(orientation).get('end')
        self.__loop = True if lvertex == rvertex else False

        lvertex.add_edge(self)
        rvertex.add_edge(self)

    @property
    def label(self) -> str:
        return self.__label

    @property
    def lvertex(self) -> Vertex:
        return self.__lvertex

    @property
    def rvertex(self) -> Vertex:
        return self.__rvertex

    @property
    def weight(self) -> float:
        return self.__weight

    @weight.setter
    def weight(self, weight: float):
        self.__weight = weight

    @property
    def start(self) -> Vertex:
        return self.__start

    @property
    def end(self) -> Vertex:
        return self.__end

    @property
    def loop(self) -> bool:
        return self.__loop


class Graph:

    def __init__(self, name: str):
        self.__name = name
        self.__vertices = dict()
        self.__edges = dict()

    @property
    def name(self) -> str:
        return self.__name

    @property
    def vertices(self) -> dict:
        return self.__vertices

    @property
    def edges(self) -> dict:
        return self.__edges

    def add_edges(self, edges):
        # TODO: Usar listas de tripletas (label, vertex_left, vertex_right, weight, orientation).
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

    # TODO: Definir una funci??n para remover vertices:
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

    # TODO: Definir una funci??n para remover aristas.
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

    # TODO: Mejorar esta funci??n para detectar los nodos que no tienen ni entradas ni salidas.
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


class NotOrientedGraph():

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
