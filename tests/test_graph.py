from optrees import Edge, Graph, Vertex


def test_default_initial_graph():
    graph = Graph("G")
    assert graph.label == "G"
    assert graph.vertices == dict()
    assert graph.edges == dict()
    assert graph.vertices_count == 0
    assert graph.edges_count == 0


def test_delete_graph():
    graph = Graph("G")
    del graph
    try:
        graph
        check_exists = True
    except NameError:
        check_exists = False
    assert check_exists is False


def test_repr():
    graph = Graph("G")
    assert graph.__repr__() == f"Graph({graph.label})"


def test_label():
    graph = Graph("G")
    assert graph.label == "G"


def test_add_vertex():
    graph = Graph("G")
    vertex_a = Vertex("a")
    graph.add_vertex(vertex_a)
    assert graph.vertices == {"a": vertex_a}
    assert graph.vertices_count == 1
    try:
        graph.add_vertex(vertex_a)
        check_exists = True
    except ValueError:
        check_exists = False
    assert check_exists is False


def test_add_vertices():
    graph = Graph("G")
    vertex_a = Vertex("a")
    vertex_b = Vertex("b")
    graph.add_vertices([vertex_a, vertex_b])
    assert graph.vertices == {"a": vertex_a, "b": vertex_b}
    assert graph.vertices_count == 2
    try:
        graph.add_vertices([vertex_a, vertex_b])
        check_exists = True
    except ValueError:
        check_exists = False
    assert check_exists is False


def test_add_edge():
    graph = Graph("G")
    vertex_a = Vertex("a")
    vertex_b = Vertex("b")
    edge_ab = Edge(vertex_a, vertex_b)
    graph.add_edge(edge_ab)
    assert graph.edges == {"a - b": edge_ab}
    assert graph.edges_count == 1
    try:
        graph.add_edge(edge_ab)
        check_exists = True
    except ValueError:
        check_exists = False
    assert check_exists is False


def test_add_edges():
    graph = Graph("G")
    vertex_a = Vertex("a")
    vertex_b = Vertex("b")
    vertex_c = Vertex("c")
    edge_ab = Edge(vertex_a, vertex_b)
    edge_bc = Edge(vertex_b, vertex_c)
    graph.add_edges([edge_ab, edge_bc])
    assert graph.edges == {"a - b": edge_ab, "b - c": edge_bc}
    assert graph.edges_count == 2
    try:
        graph.add_edges([edge_ab, edge_bc])
        check_exists = True
    except ValueError:
        check_exists = False
    assert check_exists is False


def remove_vertex():
    graph = Graph("G")
    vertex_a = Vertex("a")
    vertex_b = Vertex("b")
    vertex_c = Vertex("c")
    edge_ab = Edge(vertex_a, vertex_b)
    edge_bc = Edge(vertex_b, vertex_c)
    graph.add_edges([edge_ab, edge_bc])
    graph.remove_vertex(vertex_b)
    assert graph.vertices == {"a": vertex_a, "c": vertex_c}
    assert graph.vertices_count == 2
    try:
        graph.remove_vertex(vertex_b)
        check_exists = True
    except ValueError:
        check_exists = False
    assert check_exists is False


def remove_vertices():
    graph = Graph("G")
    vertex_a = Vertex("a")
    vertex_b = Vertex("b")
    vertex_c = Vertex("c")
    edge_ab = Edge(vertex_a, vertex_b)
    edge_bc = Edge(vertex_b, vertex_c)
    graph.add_edges([edge_ab, edge_bc])
    graph.remove_vertices([vertex_b, vertex_c])
    assert graph.vertices == {"a": vertex_a}
    assert graph.vertices_count == 1
    try:
        graph.remove_vertices([vertex_b, vertex_c])
        check_exists = True
    except ValueError:
        check_exists = False
    assert check_exists is False


def remove_edge():
    graph = Graph("G")
    vertex_a = Vertex("a")
    vertex_b = Vertex("b")
    vertex_c = Vertex("c")
    edge_ab = Edge(vertex_a, vertex_b)
    edge_bc = Edge(vertex_b, vertex_c)
    graph.add_edges([edge_ab, edge_bc])
    graph.remove_edge(edge_bc)
    assert graph.edges == {"a - b": edge_ab}
    assert graph.edges_count == 1
    try:
        graph.remove_edge(edge_bc)
        check_exists = True
    except ValueError:
        check_exists = False
    assert check_exists is False


def remove_edges():
    graph = Graph("G")
    vertex_a = Vertex("a")
    vertex_b = Vertex("b")
    vertex_c = Vertex("c")
    edge_ab = Edge(vertex_a, vertex_b)
    edge_bc = Edge(vertex_b, vertex_c)
    graph.add_edges([edge_ab, edge_bc])
    graph.remove_edges([edge_bc, edge_ab])
    assert graph.edges == dict()
    assert graph.edges_count == 0
    try:
        graph.remove_edges([edge_bc, edge_ab])
        check_exists = True
    except ValueError:
        check_exists = False
    assert check_exists is False


def test_from_list():
    graph = Graph("G")
    edges_tuples = [("a", "b"), ("b", "c"), ("c", "a")]
    graph.from_list(edges_tuples)
    assert graph.edges_count == 3
    assert graph.vertices_count == 3
