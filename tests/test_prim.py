from optrees import Graph, prim


def test_prim_with_connected_graph():
    graph_tuples_list = [
        ('a', 'b', 1),
        ('a', 'c', 2),
        ('b', 'c', 3),
        ('b', 'd', 4),
        ('c', 'd', 5),
        ('c', 'e', 6),
        ('d', 'e', 7),
        ('d', 'f', 8),
        ('e', 'f', 9),
        ('e', 'g', 10),
        ('f', 'g', 11),
        ('f', 'h', 12),
        ('g', 'h', 13),
        ('g', 'i', 14),
        ('h', 'i', 15),
        ('h', 'j', 16),
        ('i', 'j', 17),
        ('i', 'k', 18),
        ('j', 'k', 19),
        ('j', 'l', 20),
        ('k', 'l', 21),
        ('k', 'm', 22),
        ('l', 'm', 23),
        ('l', 'n', 24),
        ('m', 'n', 25),
        ('m', 'o', 26),
        ('n', 'o', 27),
        ('n', 'p', 28),
        ('o', 'p', 29),
        ('o', 'q', 30),
        ('p', 'q', 31),
    ]
    mst_graph_tuples_list = [
        ('a', 'b', 1),
        ('a', 'c', 2),
        ('b', 'd', 4),
        ('c', 'e', 6),
        ('d', 'f', 8),
        ('e', 'g', 10),
        ('f', 'h', 12),
        ('g', 'i', 14),
        ('h', 'j', 16),
        ('i', 'k', 18),
        ('j', 'l', 20),
        ('k', 'm', 22),
        ('l', 'n', 24),
        ('m', 'o', 26),
        ('n', 'p', 28),
        ('o', 'q', 30),
    ]
    graph = Graph('G')
    graph.from_list(graph_tuples_list)
    mst_graph = Graph('MST')
    mst_graph.from_list(mst_graph_tuples_list)
    min_spanning_tree = prim(graph)
    assert min_spanning_tree.vertices_count == 17
    assert min_spanning_tree.edges_count == 16
    assert min_spanning_tree == mst_graph


def test_prim_with_disconnected_graph():
    graph_tuples_list = [
        ('a', 'b', 1),
        ('a', 'c', 2),
        ('b', 'c', 3),
        ('b', 'd', 4),
        ('c', 'd', 5),
        ('c', 'e', 6),
        ('d', 'e', 7),
        ('d', 'f', 8),
        ('e', 'f', 9),
        ('e', 'g', 10),
        ('f', 'g', 11),
        ('f', 'h', 12),
        ('g', 'h', 13),
        ('g', 'i', 14),
        ('h', 'i', 15),
        ('h', 'j', 16),
        ('i', 'j', 17),
        ('i', 'k', 18),
        ('j', 'k', 19),
        ('j', 'l', 20),
        ('k', 'l', 21),
        ('k', 'm', 22),
        ('l', 'm', 23),
        ('l', 'n', 24),
        ('m', 'n', 25),
        ('m', 'o', 26),
        ('n', 'o', 27),
        ('n', 'p', 28),
        ('o', 'p', 29),
        ('o', 'q', 30),
        ('r', 's', 31),
    ]
    graph = Graph('G')
    graph.from_list(graph_tuples_list)
    try:
        prim(graph)
        check_exist_min_spanning_tree = True
    # TODO: what is the execption that is reaised?
    except:
        check_exist_min_spanning_tree = False
    assert check_exist_min_spanning_tree is False
