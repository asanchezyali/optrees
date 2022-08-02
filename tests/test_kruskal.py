from optrees import Graph, kruskal


def test_kruskal_graph_1():
    graph_tuples_list = [
        ("a", "b", 1),
        ("a", "d", 4),
        ("a", "e", 3),
        ("b", "d", 4),
        ("b", "e", 2),
        ("c", "e", 4),
        ("c", "f", 5),
        ("d", "e", 4),
        ("e", "f", 7),
    ]
    msf_graph_tuples_list = [
        ("a", "b", 1),
        ("a", "d", 4),
        ("b", "e", 2),
        ("c", "e", 4),
        ("c", "f", 5),
    ]
    graph = Graph("G")
    graph.from_list(graph_tuples_list)

    mst_graph = Graph("MST")
    mst_graph.from_list(msf_graph_tuples_list)

    min_spanning_forest = kruskal(graph)
    assert min_spanning_forest.vertices_count == mst_graph.vertices_count
    assert min_spanning_forest.edges_count == mst_graph.edges_count
    assert sum(edge.weight for edge in min_spanning_forest.edges.values()) == sum(
        edge.weight for edge in mst_graph.edges.values()
    )


def test_kruskal_graph_2():
    graph_tuples_list = [
        ("a", "b", 1),
        ("a", "c", 2),
        ("b", "c", 3),
        ("b", "d", 4),
        ("c", "d", 5),
        ("c", "e", 6),
        ("d", "e", 7),
        ("d", "f", 8),
        ("e", "f", 9),
        ("e", "g", 10),
        ("f", "g", 11),
        ("f", "h", 12),
        ("g", "h", 13),
        ("g", "i", 14),
        ("h", "i", 15),
        ("h", "j", 16),
        ("i", "j", 17),
        ("i", "k", 18),
        ("j", "k", 19),
        ("j", "l", 20),
        ("k", "l", 21),
        ("k", "m", 22),
        ("l", "m", 23),
        ("l", "n", 24),
        ("m", "n", 25),
        ("m", "o", 26),
        ("n", "o", 27),
        ("n", "p", 28),
        ("o", "p", 29),
        ("o", "q", 30),
        ("p", "q", 31),
    ]
    mst_graph_tuples_list = [
        ("a", "b", 1),
        ("a", "c", 2),
        ("b", "d", 4),
        ("c", "e", 6),
        ("d", "f", 8),
        ("e", "g", 10),
        ("f", "h", 12),
        ("g", "i", 14),
        ("h", "j", 16),
        ("i", "k", 18),
        ("j", "l", 20),
        ("k", "m", 22),
        ("l", "n", 24),
        ("m", "o", 26),
        ("n", "p", 28),
        ("o", "q", 30),
    ]
    graph = Graph("G")
    graph.from_list(graph_tuples_list)
    msf_graph = Graph("MST")
    msf_graph.from_list(mst_graph_tuples_list)
    min_spanning_forest = kruskal(graph)
    assert min_spanning_forest.vertices_count == msf_graph.vertices_count
    assert min_spanning_forest.edges_count == msf_graph.edges_count
    assert min_spanning_forest == msf_graph
