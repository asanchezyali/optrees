class BasicVertex:
    def __init__(self, label: str):
        self.__label = label
        self.__edges = dict()
        self.__neighbors = dict()

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
        from optrees.graph.edge.edge import Edge
        if not isinstance(vertex, BasicVertex):
            raise TypeError('The vertex is not valid.')
        same_vertex = self is vertex
        already_neighbor = vertex.label in self.__neighbors.keys() and self.__neighbors[vertex.label] is vertex
        if not same_vertex and not already_neighbor:
            self.__neighbors[vertex.label] = vertex
            vertex.__neighbors[self.label] = self
            edge = Edge(
                label=f'{self.label} {orientation} {vertex.label}',
                left_vertex=self,
                right_vertex=vertex,
                weight=weight,
                orientation=orientation
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