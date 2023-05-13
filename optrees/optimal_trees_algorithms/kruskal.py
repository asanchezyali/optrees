from optrees import Graph


def kruskal(graph: Graph):
    mst_graph = Graph("MSF")
    components = {vertex: {vertex} for vertex in graph.vertices}
    edges = sorted(
        graph.edges.values(),
        key=lambda edge: edge.weight if edge.weight is not None else 0,
        reverse=True,
    )
    while mst_graph.edges_count < graph.vertices_count and len(edges) > 0:
        edge = edges.pop()
        if components[edge.right_vertex.label] != components[edge.left_vertex.label]:
            mst_graph.add_edge(edge)
            new_components = components[edge.left_vertex.label].union(
                components[edge.right_vertex.label]
            )
            for vertex in new_components:
                components[vertex] = new_components
    return mst_graph
