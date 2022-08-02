from optrees import Graph


def kruskal(graph: Graph):
    forests = {vertex: {vertex} for vertex in graph.vertices}
    edges = sorted(
        graph.edges.values(),
        key=lambda edge: edge.weight if edge.weight is not None else 0,
        reverse=True,
    )

    minimum_spanning_forest = Graph("MSF")
    while minimum_spanning_forest.edges_count < graph.vertices_count and len(edges) > 0:
        edge = edges.pop()
        if forests[edge.right_vertex.label] != forests[edge.left_vertex.label]:
            minimum_spanning_forest.add_edge(edge)

            new_tree = forests[edge.left_vertex.label].union(
                forests[edge.right_vertex.label]
            )
            for vertex in new_tree:
                forests[vertex] = new_tree

    return minimum_spanning_forest
