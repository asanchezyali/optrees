from typing import Tuple
from optrees import Vertex, Edge
from optrees.helpers.lists import item_check_exists


class BasicGraph:
    def __init__(self, label: str):
        self.__label = label
        self.__vertices = dict()
        self.__edges = dict()
        self.__vertices_count = 0
        self.__edges_count = 0
        self.__weight_sum = 0

    def __del__(self):
        print(f"Graph {self.label} is deleted.")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__label})"

    def __eq__(self, other):
        if isinstance(other, BasicGraph):
            return (
                self.__vertices.keys() == other.__vertices.keys()
                and self.__edges.keys() == other.__edges.keys()
            )
        return False

    def __contains__(self, other):
        if isinstance(other, Vertex):
            return other.label in self.__vertices.keys()
        elif isinstance(other, Edge):
            return other.label in self.__edges.keys()
        else:
            return False

    @property
    def label(self) -> str:
        return self.__label

    @property
    def vertices(self) -> dict:
        return self.__vertices

    @property
    def edges(self) -> dict:
        return self.__edges

    @property
    def vertices_count(self) -> int:
        return self.__vertices_count

    @property
    def edges_count(self) -> int:
        return self.__edges_count

    @property
    def weight_sum(self) -> int:
        return self.__weight_sum

    def add_vertex(self, vertex: Vertex):
        if vertex.label in self.__vertices.keys():
            raise ValueError("The vertex is already in the graph.")
        self.__vertices[vertex.label] = vertex
        self.__vertices_count += 1

    def add_vertices(self, vertices: list[Vertex]):
        for vertex in vertices:
            self.add_vertex(vertex)

    def add_edge(self, edge: Edge):
        if edge.label in self.__edges.keys():
            raise ValueError("The edge is already in the graph.")
        if edge.left_vertex.label not in self.__vertices.keys():
            self.add_vertex(edge.left_vertex)
        if edge.right_vertex.label not in self.__vertices.keys():
            self.add_vertex(edge.right_vertex)
        self.__edges[edge.label] = edge
        self.__edges_count += 1
        self.__weight_sum += edge.weight

    def add_edges(self, edges: list[Edge]):
        for edge in edges:
            self.add_edge(edge)

    def remove_vertex(self, vertex: Vertex):
        if vertex.label not in self.__vertices.keys():
            raise ValueError("The vertex is not in the graph.")
        for edge in vertex.edges.values():
            self.remove_edge(edge)
        del self.__vertices[vertex.label]
        self.__vertices_count -= 1

    def remove_vertices(self, vertices: list[Vertex]):
        for vertex in vertices:
            self.remove_vertex(vertex)

    def remove_edge(self, edge: Edge):
        if edge.label not in self.__edges.keys():
            raise ValueError("The edge is not in the graph.")
        del self.__edges[edge.label]
        self.__edges_count -= 1

    def remove_edges(self, edges: list[Edge]):
        for edge in edges:
            self.remove_edge(edge)


class Graph(BasicGraph):
    def __init__(self, label: str):
        super().__init__(label)

    @staticmethod
    def get_edges_dicts_list(edges_tuples_list: list[Tuple]) -> dict:
        edges_dicts = list()
        for edge_tuple in edges_tuples_list:
            if len(edge_tuple) <= 1 or len(edge_tuple) > 5:
                raise ValueError(f"The edge tuple {edge_tuple} is invalid.")
            edges_dicts.append(
                {
                    "left_vertex": edge_tuple[0],
                    "right_vertex": edge_tuple[1],
                    "weight": edge_tuple[2] if item_check_exists(edge_tuple, 2) else 0,
                    "orientation": edge_tuple[3]
                    if item_check_exists(edge_tuple, 3)
                    else "-",
                    "label": edge_tuple[4]
                    if item_check_exists(edge_tuple, 4)
                    else None,
                }
            )
        return edges_dicts

    def from_list(self, edges_tuples: list[Tuple[str, str, str, float, str]]):
        edges_dicts = self.get_edges_dicts_list(edges_tuples)
        for edge_dict in edges_dicts:
            if edge_dict.get("left_vertex") not in self.vertices.keys():
                self.add_vertex(Vertex(edge_dict["left_vertex"]))
            if edge_dict.get("right_vertex") not in self.vertices.keys():
                self.add_vertex(Vertex(edge_dict["right_vertex"]))
            edge_dict.update(
                {
                    "left_vertex": self.vertices[edge_dict["left_vertex"]],
                    "right_vertex": self.vertices[edge_dict["right_vertex"]],
                }
            )
            self.add_edge(Edge(**edge_dict))
