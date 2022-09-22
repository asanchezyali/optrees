from optrees import prim


def test_prim_with_connected_graph_with_single_mst(connected_graph_with_single_mst):
    graph, mst_graph = connected_graph_with_single_mst
    min_spanning_tree = prim(graph)
    assert min_spanning_tree.vertices_count == mst_graph.vertices_count
    assert min_spanning_tree.edges_count == mst_graph.edges_count
    assert min_spanning_tree == mst_graph


def test_prim_with_connected_graph_with_multiple_mst(connected_graph_with_multiple_mst):
    graph, mst_graph = connected_graph_with_multiple_mst
    min_spanning_tree = prim(graph)
    assert min_spanning_tree.vertices_count == mst_graph.vertices_count
    assert min_spanning_tree.edges_count == mst_graph.edges_count
    assert min_spanning_tree.weight_sum == mst_graph.weight_sum


def test_prim_with_disconnected_graph(disconnected_graph):
    graph = disconnected_graph
    try:
        prim(graph)
        check_exist_min_spanning_tree = True
    except Exception:
        check_exist_min_spanning_tree = False
    assert check_exist_min_spanning_tree is False
