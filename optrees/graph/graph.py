from typing import List, Tuple

from optrees.graph.basic_objects import Edge, Vertex
from optrees.helpers.lists import item_check_exists


class BasicGraph:
    def __init__(self, label: str):
        self.__label = label
        self.__vertices: dict = {}
        self.__edges: dict = {}
        self.__vertices_count = 0
        self.__edges_count = 0
        self.__weight_sum = 0.0

    def __del__(self):
        print(f'Graph {self.label} is deleted.')

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.__label})'

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
    def weight_sum(self) -> float:
        return self.__weight_sum

    def add_vertex(self, vertex: Vertex):
        if vertex.label in self.__vertices.keys():
            raise ValueError('The vertex is already in the graph.')
        self.__vertices[vertex.label] = vertex
        self.__vertices_count += 1

    def add_vertices(self, vertices: List[Vertex]):
        for vertex in vertices:
            self.add_vertex(vertex)

    def add_edge(self, edge: Edge):
        if edge.label in self.__edges.keys():
            raise ValueError('The edge is already in the graph.')
        if edge.left_vertex.label not in self.__vertices.keys():
            self.add_vertex(edge.left_vertex)
        if edge.right_vertex.label not in self.__vertices.keys():
            self.add_vertex(edge.right_vertex)
        self.__edges[edge.label] = edge
        self.__edges_count += 1
        self.__weight_sum += edge.weight

    def add_edges(self, edges: List[Edge]):
        for edge in edges:
            self.add_edge(edge)

    def remove_vertex(self, vertex: Vertex):
        if vertex.label not in self.__vertices.keys():
            raise ValueError('The vertex is not in the graph.')
        for edge in vertex.edges.values():
            self.remove_edge(edge)
        del self.__vertices[vertex.label]
        self.__vertices_count -= 1

    def remove_vertices(self, vertices: List[Vertex]):
        for vertex in vertices:
            self.remove_vertex(vertex)

    def remove_edge(self, edge: Edge):
        if edge.label not in self.__edges.keys():
            raise ValueError('The edge is not in the graph.')
        del self.__edges[edge.label]

    def remove_edges(self, edges: List[Edge]):
        for edge in edges:
            self.remove_edge(edge)


class Graph(BasicGraph):
    def __init__(self, label: str):
        super().__init__(label)

    @staticmethod
    def get_edges_dicts_list(
        edges_tuples_list: List[Tuple[str, str, str, float, str]]
    ) -> List[dict]:
        left_vertex, right_vertex, weight, orientation, label = range(5)
        edges_dicts = list()
        for edge_tuple in edges_tuples_list:
            if len(edge_tuple) <= 1 or len(edge_tuple) > 5:
                raise ValueError(f'The edge tuple {edge_tuple} is invalid.')
            edges_dicts.append(
                {
                    'left_vertex': edge_tuple[left_vertex],
                    'right_vertex': edge_tuple[right_vertex],
                    'weight': edge_tuple[weight]
                    if item_check_exists(edge_tuple, weight)
                    else 0,
                    'orientation': edge_tuple[orientation]
                    if item_check_exists(edge_tuple, orientation)
                    else '-',
                    'label': edge_tuple[label]
                    if item_check_exists(edge_tuple, label)
                    else None,
                }
            )
        return edges_dicts

    def from_list(self, edges_tuples: List[Tuple[str, str, str, float, str]]):
        edges_dicts = self.get_edges_dicts_list(edges_tuples)
        for edge_dict in edges_dicts:
            if edge_dict.get('left_vertex') not in self.vertices.keys():
                self.add_vertex(Vertex(edge_dict['left_vertex']))
            if edge_dict.get('right_vertex') not in self.vertices.keys():
                self.add_vertex(Vertex(edge_dict['right_vertex']))
            edge_dict.update(
                {
                    'left_vertex': self.vertices[edge_dict['left_vertex']],
                    'right_vertex': self.vertices[edge_dict['right_vertex']],
                }
            )
            self.add_edge(Edge(**edge_dict))

    def adjacency_matrix(self) -> List[List[float]]:
        pass


class GraphReader:
    def __init__(self, file_path: str):
        self.__file_path = file_path

    def read(self) -> Graph:
        read_graph_label = 0
        read_graph_vertices = 1
        left_vertex, right_vertex, weight, orientation, label = range(5)
        with open(self.__file_path) as file:
            lines = file.readlines()
            graph = Graph(lines[read_graph_label].strip())
            for line in lines[read_graph_vertices:]:
                edge_tuple = line.strip().split()
                if len(edge_tuple) <= 1 or len(edge_tuple) > 5:
                    raise ValueError(f'The edge tuple {edge_tuple} is invalid.')
                if edge_tuple[left_vertex] not in graph.vertices.keys():
                    graph.add_vertex(Vertex(edge_tuple[left_vertex]))
                if edge_tuple[right_vertex] not in graph.vertices.keys():
                    graph.add_vertex(Vertex(edge_tuple[right_vertex]))
                edge_dict = {
                    'left_vertex': graph.vertices[edge_tuple[left_vertex]],
                    'right_vertex': graph.vertices[edge_tuple[right_vertex]],
                    'weight': edge_tuple[weight]
                    if item_check_exists(edge_tuple, weight)
                    else 0,
                    'orientation': edge_tuple[orientation]
                    if item_check_exists(edge_tuple, orientation)
                    else '-',
                    'label': edge_tuple[label]
                    if item_check_exists(edge_tuple, label)
                    else None,
                }
                graph.add_edge(Edge(**edge_dict))
        return graph

    def write(self, graph: Graph):
        with open(self.__file_path, 'w') as file:
            file.write(f'{graph.label}\n')
            for edge in graph.edges.values():
                file.write(
                    f'{edge.left_vertex.label} {edge.right_vertex.label} {edge.weight} {edge.orientation} {edge.label}\n'
                )
