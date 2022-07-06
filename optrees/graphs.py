from typing import List, Tuple

import numpy as np
from pyparsing import Optional


class Vertex:
    def __init__(self, label: str):
        self.__label = label
        self.__neighbors = dict()
        self.__edges = dict()
        self.__loops = dict()

    def __del__(self):
        """
        Delete the vertex.
        """
        print(f"Vertex {self.label} is deleted.")

    @property
    def label(self) -> str:
        """
        Returns the label of the vertex.
        """
        return self.__label

    @property
    def neighbors(self) -> dict:
        """
        Return the neighbors of the vertex.
        """
        return self.__neighbors

    def add_neighbor(self, vertex: "Vertex", weight: float = None):
        """
        Add a neighbor to the vertex.
        """
        if self is not vertex:
            self.__neighbors[vertex.label] = vertex
            edge = Edge(
                label=f"{self.label}-{vertex.label}",
                lvertex=self,
                rvertex=vertex,
            )
            edge.weight = weight
            self.add_edge(edge)
        else:
            raise ValueError("It is the same vertex.")

    def delete_neighbor(self, vertex_label: str):
        """
        Delete a neighbor from the vertex.
        """
        try:
            del self.__neighbors[vertex_label]
            for edge in self.__edges.values():
                if edge.is_vertex(vertex_label):
                    del self.__edges[edge.label]
                    del self.__loops[edge.label]
        except KeyError:
            raise KeyError(f"Vertex {vertex_label} does not exist.")

    def neighbor(self, label: str) -> "Vertex":
        """
        Return the neighbor vertex of the vertex.
        """
        return self.neighbors.get(label)

    def remove_edge(self, edge: "Edge"):
        """
        Remove an edge from the vertex.
        """
        if edge.label in self.__edges.keys():
            del self.__edges[edge.label]
        else:
            raise ValueError("This edge does not exist.")

    def get_weight(self, vertex: "Vertex") -> float:
        """
        Return the weight of the edge.
        """
        return self.__edges.get(vertex.label).weight

    @property
    def edges(self) -> dict:
        """
        Return the edges of the vertex.
        """
        return self.__edges

    def add_edge(self, edge: "Edge"):
        """
        Add an edge to the vertex.
        """
        if (
            not edge.loop
            and edge.label not in self.__edges.keys()
            and edge not in self.__edges.values()
        ):
            self.__edges[edge.label] = edge
        elif (
            edge.loop
            and edge.label not in self.__edges.keys()
            and edge not in self.__edges.values()
        ):
            self.__loops[edge.label] = edge
            self.__edges[edge.label] = edge
        elif (
            edge.loop
            and edge.label in self.__edges.keys()
            and edge in self.__edges.values()
        ):
            pass
        else:
            raise ValueError("This edge or loop already exists")

    def edge(self, label: str) -> str:
        """
        Return the edge of the vertex.
        """
        return self.edges.get(label)

    @property
    def loops(self) -> dict:
        """
        Return the loops of the vertex.
        """
        return self.__loops

    def loop(self, label: str) -> str:
        """
        Return the loop of the vertex.
        """
        return self.loops.get(label)

    def is_isolated(self) -> bool:
        """
        Return True if the vertex is isolated.
        """
        return len(self.neighbors) == 0


class Edge:
    def __init__(
        self,
        label: str,
        lvertex: Vertex,
        rvertex: Vertex,
        weight: float = None,
        orientation: str = None,
    ):
        orientations = {
            "lr": {"start": lvertex, "end": rvertex},
            "rl": {"start": rvertex, "end": lvertex},
        }
        self.__label = label
        self.__lvertex = lvertex
        self.__rvertex = rvertex
        self.__weight = weight
        self.__start = (
            None
            if orientation not in ["lr", "rl"]
            else orientations.get(orientation).get("start")
        )
        self.__end = (
            None
            if orientation not in ["lr", "rl"]
            else orientations.get(orientation).get("end")
        )
        self.__loop = True if lvertex == rvertex else False

        lvertex.add_edge(self)
        rvertex.add_edge(self)

    def __del__(self):
        """
        Delete the edge.
        """
        print(f"Edge {self.label} is deleted.")

    @property
    def label(self) -> str:
        """
        Return the label of the edge.
        """
        return self.__label

    @property
    def lvertex(self) -> Vertex:
        """
        Return the left vertex of the edge.
        """
        return self.__lvertex

    @property
    def rvertex(self) -> Vertex:
        """
        Return the right vertex of the edge.
        """
        return self.__rvertex

    @property
    def weight(self) -> float:
        """
        Return the weight of the edge.
        """
        return self.__weight

    @weight.setter
    def weight(self, weight: float):
        """
        Set the weight of the edge.
        """
        self.__weight = weight

    @property
    def start(self) -> Vertex:
        """
        Return the start vertex of the edge.
        """
        return self.__start

    @property
    def end(self) -> Vertex:
        """
        Return the end vertex of the edge.
        """
        return self.__end

    @property
    def loop(self) -> bool:
        """
        Return True if the edge is a loop.
        """
        return self.__loop

    def is_vertex(self, vertex_label: str) -> bool:
        """
        Return True if the vertex is the start or end vertex of the edge.
        """
        return self.lvertex.label == vertex_label or self.rvertex.label == vertex_label


class Graph:
    def __init__(self, name: str):
        self.__name = name
        self.__vertices = dict()
        self.__edges = dict()

    @property
    def name(self) -> str:
        """
        Return the name of the graph.
        """
        return self.__name

    @property
    def vertices(self) -> dict:
        """
        Return the vertices of the graph.
        """
        return self.__vertices

    @property
    def edges(self) -> dict:
        """
        Return the edges of the graph.
        """
        return self.__edges

    def add_edge(self, edge: Edge):
        """
        Add an edge to the graph.
        """
        if edge.label not in self.__edges.keys():
            self.__edges[edge.label] = edge
            self.__vertices[edge.lvertex.label] = edge.lvertex
            self.__vertices[edge.rvertex.label] = edge.rvertex
        else:
            raise ValueError("This edge already exists")

    def add_vertex(self, vertex: Vertex):
        """
        Add a vertex to the graph.
        """
        self.__vertices[vertex.label] = vertex

    def add_edges(self, edges: List[Edge]):
        """
        Add a list of edges to the graph.
        """
        for edge in edges:
            self.add_edge(edge)

    def build(self, edges: List[Tuple[str, str, str, float, str]]):
        """
        Builds a graph from a list of edges.
        """
        label, lvertex, rvertex, weight, orientation = range(
            5
        )  # ids of the elements in the list
        for edge in edges:
            if edge[label] not in self.__edges.keys():
                left_vertex = Vertex(edge[lvertex])
                right_vertex = Vertex(edge[rvertex])
                edge = Edge(
                    label=edge[label],
                    lvertex=left_vertex,
                    rvertex=right_vertex,
                    weight=edge[weight] if len(edge) > 3 else None,
                    orientation=edge[orientation] if len(edge) > 4 else None,
                )
                self.add_edge(edge)
                self.add_vertex(left_vertex)
                self.add_vertex(right_vertex)
            else:
                raise ValueError("This edge already exists")

    def is_vertex(self, vertex_label: str) -> bool:
        """
        Return True if the vertex is in the graph.
        """
        return vertex_label in self.__vertices.keys()

    def is_edge(self, edge_label: str) -> bool:
        """
        Return True if the edge is in the graph.
        """
        return edge_label in self.__edges.keys()

    def get_vertex(self, vertex_label: str) -> Optional[Vertex]:
        """
        Return the vertex of the graph.
        """
        return self.__vertices.get(vertex_label)

    def get_edge(self, edge_label: str) -> Edge:
        """
        Return the edge of the graph.
        """
        return self.__edges.get(edge_label)

    def remove_vertex(self, vertex_label: str):
        """
        Remove the vertex from the graph.
        """
        if self.is_vertex(vertex_label):
            del self.__vertices[vertex_label]
            for edge in self.__edges.values():
                if edge.is_vertex(vertex_label):
                    del self.__edges[edge.label]
                    edge.lvertex.remove_edge(edge)
                    edge.rvertex.remove_edge(edge)
                    break
        else:
            raise ValueError("This vertex does not exist")

    def remove_edge(self, edge_label: str):
        """
        Remove the edge from the graph.
        """
        if self.is_edge(edge_label):
            del self.__edges[edge_label]
            for edge in self.__edges.values():
                if edge.label == edge_label:
                    edge.lvertex.remove_edge(edge)
                    edge.rvertex.remove_edge(edge)
                    break
        else:
            raise ValueError("This edge does not exist")

    def get_isolate_vertices(self) -> list[Vertex]:
        """
        Return the list of vertices that are isolated.
        """
        return [vertex for vertex in self.__vertices.values() if vertex.is_isolated()]

    def adjacency_matrix(self) -> tuple:
        """
        Return the adjacency matrix of the graph.
        """
        vertices = self.__vertices.values()
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
        """
        Return the weight matrix of the graph.
        """
        vertices = self.vertices.values()
        matrix = list()
        for row_vertex in vertices:
            row = list()
            for col_vertex in vertices:
                if col_vertex.label in row_vertex.neighbors():
                    row.append(row_vertex.get_weight(col_vertex.label))
                else:
                    row.append(np.inf)
            matrix.append(row)
        indices = self.vertices.keys()
        return np.matrix(matrix), list(indices)


class GraphReader:
    """
    A class for reading a graph from a file.
    """

    def __init__(self):
        self.__graph = Graph()

    def read(self, file_path: str):
        """
        Reads a graph from a file.
        """
        with open(file_path) as file:
            lines = file.readlines()
            edges = list()
            for line in lines:
                edge = line.split()
                edges.append((edge[0], edge[1], edge[2], float(edge[3]), edge[4]))
            self.__graph.build(edges)

    def get_graph(self) -> Graph:
        """
        Return the graph.
        """
        return self.__graph


class GraphWriter:
    """
    A class for writing a graph to a file.
    """

    def __init__(self, graph: Graph):
        self.__graph = graph

    def write(self, file_path: str):
        """
        Writes a graph to a file.
        """
        with open(file_path, "w") as file:
            for edge in self.__graph.edges:
                file.write(
                    edge.label
                    + " "
                    + edge.lvertex.label
                    + " "
                    + edge.rvertex.label
                    + " "
                    + str(edge.weight)
                    + " "
                    + edge.orientation
                    + "\n"
                )

    def get_graph(self) -> Graph:
        """
        Return the graph.
        """
        return self.__graph


class GraphUtils:
    """
    A class for performing graph operations.
    """

    @staticmethod
    def read_graph(file_path: str) -> Graph:
        """
        Reads a graph from a file.
        """
        reader = GraphReader()
        reader.read(file_path)
        return reader.get_graph()

    @staticmethod
    def write_graph(graph: Graph, file_path: str):
        """
        Writes a graph to a file.
        """
        writer = GraphWriter()
        writer.write(file_path)
        return writer.get_graph()

    @staticmethod
    def get_isolate_vertices(graph: Graph) -> List[Vertex]:
        """
        Return the list of vertices that are isolated.
        """
        return graph.get_isolate_vertices()

    @staticmethod
    def get_weight_matrix(graph: Graph) -> tuple:
        """
        Return the weight matrix of the graph.
        """
        return graph.weight_matrix()

    @staticmethod
    def get_adjacency_matrix(graph: Graph) -> tuple:
        """
        Return the adjacency matrix of the graph.
        """
        return graph.adjacency_matrix()


class GraphAlgorithms:
    """
    A class for performing graph algorithms.
    """

    @staticmethod
    def dijkstra(graph: Graph, start_vertex: Vertex) -> list:
        """
        Return the list of vertices that are reachable from the start vertex.
        """
        distances = {vertex.label: np.inf for vertex in graph.vertices.values()}
        distances[start_vertex.label] = 0
        vertices = graph.vertices.values()
        while vertices:
            min_distance = np.inf
            vertex = None
            for vertex in vertices:
                if distances[vertex.label] < min_distance:
                    min_distance = distances[vertex.label]
                    nearest_vertex = vertex
            vertices.remove(nearest_vertex)
            for neighbor in nearest_vertex.neighbors():
                distance = (
                    nearest_vertex.get_weight(neighbor)
                    + distances[nearest_vertex.label]
                )
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
        return distances

    @staticmethod
    def floyd_warshall(graph: Graph) -> list:
        """
        Return the list of vertices that are reachable from any vertex.
        """
        distances = {vertex.label: np.inf for vertex in graph.vertices.values()}
        for vertex in graph.vertices.values():
            for neighbor in vertex.neighbors():
                distances[neighbor] = vertex.get_weight(neighbor)
        for k in graph.vertices.keys():
            for i in graph.vertices.keys():
                for j in graph.vertices.keys():
                    if distances[i] + distances[j] < distances[i]:
                        distances[i] = distances[i] + distances[j]
        return distances


class GraphTest:
    """
    A class for testing the graph algorithms.
    """

    def __init__(self, graph: Graph):
        self.__graph = graph

    def test(self):
        """
        Tests the graph algorithms.
        """
        print("Isolate vertices:")
        print(GraphUtils.get_isolate_vertices(self.__graph))

        print("\nWeight matrix:")
        print(GraphUtils.get_weight_matrix(self.__graph))

        print("\nAdjacency matrix:")
        print(GraphUtils.get_adjacency_matrix(self.__graph))

        print("\nDijkstra:")
        print(GraphAlgorithms.dijkstra(self.__graph, self.__graph.vertices[0]))

        print("\nFloyd-Warshall:")
        print(GraphAlgorithms.floyd_warshall(self.__graph))


if __name__ == "__main__":
    graph = GraphUtils.read_graph("graph.txt")
    GraphTest(graph).test()
