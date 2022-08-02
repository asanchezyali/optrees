from optrees import Vertex

class BasicEdge:
    def __init__(self, left_vertex, right_vertex, weight=None, orientation='-', label=None):
        self.__left_vertex = left_vertex
        self.__right_vertex = right_vertex
        self.__weight = weight
        self.__orientation = self.validate_and_get_orientation(orientation)
        self.__label = label if label else f'{left_vertex.label} {orientation} {right_vertex.label}'
        self.__start = (
            None
            if orientation not in ['->', '<-']
            else (left_vertex if orientation == '->' else right_vertex)
        )
        self.__end = (
            None
            if orientation not in ['->', '<-']
            else (right_vertex if orientation == '->' else left_vertex)
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
            return label_equal and left_vertex_equal and right_vertex_equal and orientation_equal
        return False

    def __contains__(self, other):
        if isinstance(other, Vertex):
            return other.label in [self.__left_vertex.label, self.__right_vertex.label]
        return False

    @staticmethod
    def validate_and_get_orientation(orientation: str) -> bool:
        if orientation in ['->', '<-', '-']:
            return orientation
        else:
            raise ValueError('The orientation is not valid.')

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
        self.__orientation = self.validate_and_get_orientation(orientation)

    @property
    def start(self) -> Vertex:
        return self.__start

    @property
    def end(self) -> Vertex:
        return self.__end


class Edge(BasicEdge):
    def __init__(self, left_vertex, right_vertex, weight=None, orientation='-', label=None):
        super().__init__(left_vertex, right_vertex, weight, orientation, label)
