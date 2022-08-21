from typing import Union


class BasicVertex:
    def __init__(self, label: str):
        self.__label = label
        self.__edges: dict = {}
        self.__neighbors: dict = {}

    def __del__(self):
        print(f'Vertex {self.label} is deleted.')

    def __str__(self):
        return self.__label

    def __repr__(self):
        return f'{self.__class__.__name__}({self.__label})'

    def __eq__(self, other):
        if isinstance(other, BasicVertex):
            label_equal = self.__label == other.__label
            edges_equal = self.__edges == other.__edges
            neighbors_equal = self.__neighbors == other.__neighbors
            return label_equal and edges_equal and neighbors_equal
        return False

    @property
    def label(self) -> str:
        return self.__label

    @property
    def edges(self) -> dict:
        return self.__edges

    @property
    def neighbors(self) -> dict:
        return self.__neighbors

    def add_neighbor(self, vertex, weight=None, orientation='-'):
        if not isinstance(vertex, BasicVertex):
            raise TypeError('The vertex is not valid.')
        same_vertex = self is vertex
        already_neighbor = (
            vertex.label in self.__neighbors.keys()
            and self.__neighbors[vertex.label] is vertex
        )
        if not same_vertex and not already_neighbor:
            self.__neighbors[vertex.label] = vertex
            vertex.__neighbors[self.label] = self
            edge = Edge(
                label=f'{self.label} {orientation} {vertex.label}',
                left_vertex=self,
                right_vertex=vertex,
                weight=weight,
                orientation=orientation,
            )
            self.__edges[edge.label] = edge
            vertex.__edges[edge.label] = edge
        else:
            raise ValueError('The vertex is already a neighbor.')


class Vertex(BasicVertex):
    def __init__(self, label: str):
        super().__init__(label)

    def amount_of_neighbors(self) -> int:
        return len(super().neighbors)

    def amount_of_edges(self) -> int:
        return len(super().edges)

    def is_isolated(self) -> bool:
        return self.amount_of_neighbors() == 0


class BasicEdge:
    def __init__(
        self, left_vertex, right_vertex, weight=0.0, orientation='-', label=None
    ):
        self.__left_vertex = left_vertex
        self.__right_vertex = right_vertex
        self.__weight = weight
        self.__orientation = self.__validate_and_get_orientation(orientation)
        self.__label = (
            label
            if label
            else f'{left_vertex.label} {orientation} {right_vertex.label}'
        )
        self.__start = (
            None
            if orientation not in ['->', '<-']
            else (left_vertex if orientation == '->' else right_vertex)
        )
        self.__start = self.__get_start_vertex(
            self.__orientation, self.__left_vertex, self.__right_vertex
        )
        self.__end = self.__get_end_vertex(
            self.__orientation, self.__left_vertex, self.__right_vertex
        )
        left_vertex._BasicVertex__edges[self.label] = self
        right_vertex._BasicVertex__edges[self.label] = self

    def __del__(self):
        print(f'Edge {self.label} is deleted.')

    def __str__(self) -> str:
        return self.__label

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.__label})'

    def __eq__(self, other):
        if isinstance(other, BasicEdge):
            label_equal = self.__label == other.__label
            left_vertex_equal = self.__left_vertex == other.__left_vertex
            right_vertex_equal = self.__right_vertex == other.__right_vertex
            orientation_equal = self.__orientation == other.__orientation
            return (
                label_equal
                and left_vertex_equal
                and right_vertex_equal
                and orientation_equal
            )
        return False

    def __contains__(self, other):
        if isinstance(other, Vertex):
            return other.label in [self.__left_vertex.label, self.__right_vertex.label]
        return False

    @staticmethod
    def __validate_and_get_orientation(orientation: str) -> str:
        if orientation in ['->', '<-', '-']:
            return orientation
        else:
            raise ValueError('The orientation is not valid.')

    @staticmethod
    def __get_start_vertex(
        orientation: str, left_vertex: Vertex, right_vertex: Vertex
    ) -> Union[None, Vertex]:
        return (
            None
            if orientation not in ['->', '<-']
            else (left_vertex if orientation == '->' else right_vertex)
        )

    @staticmethod
    def __get_end_vertex(
        orientation: str, left_vertex: Vertex, right_vertex: Vertex
    ) -> Union[None, Vertex]:
        return (
            None
            if orientation not in ['->', '<-']
            else (right_vertex if orientation == '->' else left_vertex)
        )

    @property
    def label(self) -> str:
        return self.__label

    @property
    def left_vertex(self) -> Vertex:
        return self.__left_vertex

    @property
    def right_vertex(self) -> Vertex:
        return self.__right_vertex

    @property
    def weight(self) -> float:
        return self.__weight

    @weight.setter
    def weight(self, weight: float):
        self.__weight = weight

    @property
    def orientation(self) -> str:
        return self.__orientation

    @orientation.setter
    def orientation(self, orientation: str):
        self.__orientation = self.__validate_and_get_orientation(orientation)

    @property
    def start(self) -> Vertex:
        return self.__start

    @property
    def end(self) -> Vertex:
        return self.__end


class Edge(BasicEdge):
    def __init__(
        self, left_vertex, right_vertex, weight=0.0, orientation='-', label=None
    ):
        super().__init__(left_vertex, right_vertex, weight, orientation, label)
