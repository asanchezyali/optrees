class Vertex:
    def __init__(self, label: str):
        self.__label = label
        self.__neighbors = dict()
        self.__edges = dict()

    def __del__(self):
        print(f'Vertex {self.label} is deleted.')

    @property
    def label(self) -> str:
        return self.__label

    @property
    def neighbors(self) -> dict:
        return self.__neighbors

    def add_neighbor(self, vertex: 'Vertex', weight: float = None, orientation: str = '-'):
        isSameVertex = self is vertex
        alreadyExists = vertex.label in self.neighbors.keys() and vertex.value in self.neighbors.values()
        if not isSameVertex and not alreadyExists:
            self.__neighbors[vertex.label] = vertex
            edge = Edge(
                label=f'{self.label}{orientation}{vertex.label}',
                left_vertex=self,
                right_vertex=vertex,
                weight=weight,
                orientation=orientation
            )
            self.add_edge(edge)
            vertex.add_edge(edge)
            vertex.__neighbors[self.label] = self
        else:
            raise ValueError('It is the same vertex or already exists.')

    def get_neighbor(self, label: str) -> 'Vertex':
        return self.neighbors.get(label)

    def get_weight(self, vertex: 'Vertex') -> float:
        return self.__edges.get(vertex.label).weight

    @property
    def edges(self) -> dict:
        return self.__edges

    def add_edge(self, edge: 'Edge'):
        self.__edges[edge.label] = edge
        
    def edge(self, label: str) -> str:
        return self.edges.get(label)

    def is_isolated(self) -> bool:
        return len(self.neighbors) == 0


class Edge:
    def __init__(
        self,
        left_vertex: Vertex,
        right_vertex: Vertex,
        label: str = None,
        weight: float = None,
        orientation: str = '-',
    ):
        orientations = {
            '->': {'start': left_vertex, 'end': right_vertex},
            '<-': {'start': right_vertex, 'end': left_vertex},
        }
        self.__label = label if label else f'{left_vertex.label}{orientation}{right_vertex.label}'
        self.__left_vertex = left_vertex
        self.__right_vertex = right_vertex
        self.__weight = weight
        self.__orientation = self.validate_and_get_orientation(orientation)
        self.__start = (
            None
            if orientation not in orientations.keys()
            else orientations.get(orientation).get('start')
        )
        self.__end = (
            None
            if orientation not in orientations.keys()
            else orientations.get(orientation).get('end')
        )
        left_vertex.add_edge(self)
        right_vertex.add_edge(self)

    def validate_and_get_orientation(self, orientation: str) -> bool:
        if orientation in ['->', '<-', '-']:
            return orientation
        else:
            raise ValueError('The orientation is not valid.')

    def __del__(self):
        print(f'Edge {self.label} is deleted.')

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

    @property
    def start(self) -> Vertex:
        return self.__start

    @property
    def end(self) -> Vertex:
        return self.__end

    @property
    def loop(self) -> bool:
        return self.__loop

    def is_vertex(self, vertex_label: str) -> bool:
        return self.left_vertex.label == vertex_label or self.right_vertex.label == vertex_label
