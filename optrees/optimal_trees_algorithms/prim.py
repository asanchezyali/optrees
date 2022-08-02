import numpy as np
from optrees import Graph

def prim(graph: Graph):
    mst_graph = Graph('MST')
    while mst_graph.vertices_count < graph.vertices_count:
        for vertex in graph.vertices.values():
            if vertex not in mst_graph:
                min_weight = np.infty
                min_edge = None
                for edge in vertex.edges.values():
                    if mst_graph.vertices_count > 0:
                        bridge = edge.right_vertex in mst_graph or edge.left_vertex in mst_graph
                    else:
                        bridge = True
                    if (edge.weight < min_weight) and bridge:
                        min_weight = edge.weight
                        min_edge = edge
                if min_edge is not None:
                    mst_graph.add_edge(min_edge)
                else:
                    raise ValueError('The graph is not connected.')
    return mst_graph