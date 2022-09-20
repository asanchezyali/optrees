import numpy as np

from optrees import Graph


def boruvka(graph: Graph):
    mst_graph = Graph('MST')
    components = {vertex: {vertex} for vertex in graph.vertices}
    while mst_graph.vertices_count < graph.vertices_count:
        min_edges = {}
        for vertex in graph.vertices.values():
            min_weight = np.Infinity
            min_edge = None
            for edge in vertex.edges.values():
                if (
                    components[edge.right_vertex.label]
                    != components[edge.left_vertex.label]
                ):
                    if edge.weight < min_weight:
                        min_weight = edge.weight
                        min_edge = edge
            if min_edge is not None:
                min_edges[min_edge.label] = min_edge
        for edge in min_edges.values():
            mst_graph.add_edge(edge)
            new_components = components[edge.left_vertex.label].union(
                components[edge.right_vertex.label]
            )
            for vertex in new_components:
                components[vertex] = new_components
    return mst_graph
