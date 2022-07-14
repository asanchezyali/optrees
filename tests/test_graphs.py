from optrees import Vertex


def test_default_initial_vertex():
    vertex_a = Vertex('a')
    assert vertex_a.label == 'a'
    assert vertex_a.neighbors == dict()
    assert vertex_a.edges == dict()
    assert vertex_a.loops == dict()

def test_delete_vertex():
    vertex_a = Vertex('a')
    del vertex_a
    try:
        vertex_a
    except NameError:
        assert True

def test_add_unweighted_and_unoriented_neighbors():
    vertex_a = Vertex('a')
    vertex_b = Vertex('b')
    vertex_a.add_neighbor(vertex_b)
    edge_ab = vertex_a.edge('a-b')
    assert vertex_b.label in vertex_a.neighbors.keys()
    assert vertex_b in vertex_a.neighbors.values()
    assert vertex_a.label in vertex_b.neighbors.keys()
    assert vertex_a in vertex_b.neighbors.values()
    assert 'a-b' in vertex_a.edges.keys()
    assert 'a-b' in vertex_b.edges.keys()
    assert vertex_a.loops == dict()
    assert vertex_b.loops == dict()
    assert edge_ab.label == 'a-b'
    assert edge_ab.weight == None
    assert edge_ab.orientation == None
    assert edge_ab.start == None
    assert edge_ab.end == None
    assert edge_ab.left_vertex == vertex_a
    assert edge_ab.right_1vertex == vertex_b
    assert edge_ab.loop == False
