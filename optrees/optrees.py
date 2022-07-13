import numpy as np
from graphs import NotOrientedGraph, Vertex


def prim(graph: NotOrientedGraph, initial_vertex: Vertex) -> NotOrientedGraph:
    """This algorithms to solve the problem of the minimum spanning tree is
    Prim's algorithm. Developed for the first time by the Czech
    mathematician Vojtêch Jarnık, it would not be until later, in 1957,
    when it would appear published independently under the authorship of
    the American computer engineer Robert C. Prim. It is he who gave him
    fame and by whose surname is known today. Created during his time at
    Bell Labs, Prim was trying address the problem of how to connect
    networks, be they telecommunications or transport and distribution,
    through a reduced or cheap number of connections.

    The solution to the problem proposed by Prim is based on the idea of
    connecting sequential nodes sequentially until you reach them all.
    Having as input an unmanaged graph, the algorithm starts to build the
    tree from a node arbitrarily selected as starting point Next iterate
    selecting in each stage the lowest cost arc (one any if there are
    several) that joins a node of the tree with another that is not yet in
    it; incorporating said arc and the destination node to the tree. The
    process is repeated until all the nodes are added, obtaining as a
    result an expansion tree whose cost will be minimal.

    Args:
        ``graph``:
        ``initial_vertex``:

    Returns:
        *NotOrientedGraph*: It is a graph called tree expansion with minimal
        cost.

    """
    # Indices:
    start_vertex, end_vertex, weight = range(3)

    # Initialize empty edges array and empty minimum spanning tree:
    minimum_spanning_tree = dict()
    visited_vertices = list()
    edges = list()
    min_edge = (None, None, np.infty)

    # Arbitrarily choose initial vertex from graph:
    vertex = initial_vertex

    # Run prim's algorithm until we create an minimum spanning tree that
    # contains every vertex from the graph:
    while len(visited_vertices) < graph.num_vertices - 1:

        # Mark this vertex as visited:
        visited_vertices.append(vertex)

        # Set of potential edges:
        edges += vertex.edges

        # Find edge with the smallest weight to a vertex that has not yet
        # been visited:
        for edge in edges:
            inequality = edge[weight] < min_edge[weight]
            membership = edge[end_vertex] not in visited_vertices
            if inequality and membership:
                min_edge = edge

        # Get the start and end node from minimum edge:
        start_min_edge = min_edge[start_vertex]
        end_min_edge = min_edge[end_vertex]
        min_weight = min_edge[weight]

        # Add the minimum edge to minimum spanning tree:
        if minimum_spanning_tree.get(start_min_edge.id):
            edge = (end_min_edge.id, min_weight)
            minimum_spanning_tree[start_min_edge.id].append(edge)
        else:
            edge = [(end_min_edge.id, min_weight)]
            minimum_spanning_tree[start_min_edge.id] = edge

        # Remove min weight edge form list of edges:
        edges.remove(min_edge)

        # Start at new vertex and reset min edge:
        vertex = end_min_edge
        min_edge = (None, None, np.infty)

    # Return the optimal tree:
    return NotOrientedGraph(minimum_spanning_tree)
