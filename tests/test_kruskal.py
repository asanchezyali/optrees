from optrees import kruskal


def test_kruskal_graph_with_single_mst(connected_graph_with_single_mst):
    graph, mst_graph = connected_graph_with_single_mst
    min_spanning_tree = kruskal(graph)
    assert min_spanning_tree.vertices_count == mst_graph.vertices_count
    assert min_spanning_tree.edges_count == mst_graph.edges_count
    assert min_spanning_tree == mst_graph


def test_kruskal_graph_with_multiple_mst(connected_graph_with_multiple_mst):
    graph, mst_graph = connected_graph_with_multiple_mst
    min_spanning_tree = kruskal(graph)
    assert min_spanning_tree.vertices_count == mst_graph.vertices_count
    assert min_spanning_tree.edges_count == mst_graph.edges_count
    assert min_spanning_tree.weight_sum == mst_graph.weight_sum
