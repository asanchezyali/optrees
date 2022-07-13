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
            vertex.add_edge(edge)
            vertex.__neighbors[self.label] = self
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
        self.__edges[edge.label] = edge
        
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
