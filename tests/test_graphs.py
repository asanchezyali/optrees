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
        check_exists = True
    except NameError:
        check_exists = False
    assert check_exists == False

def test_label():
    vertex_a = Vertex('a')
    assert vertex_a.label == 'a'

def test_neighbors():
    vertex_a = Vertex('a')
    vertex_b = Vertex('b')
    vertex_c = Vertex('c')
    vertex_a.add_neighbor(vertex_b)
    vertex_a.add_neighbor(vertex_c)
    assert vertex_a.neighbors == {'b': vertex_b, 'c': vertex_c}
    assert vertex_b.neighbors == {'a': vertex_a}
    assert vertex_c.neighbors == {'a': vertex_a}

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
    assert edge_ab.orientation == '-'
    assert edge_ab.start == None
    assert edge_ab.end == None
    assert edge_ab.left_vertex == vertex_a
    assert edge_ab.right_vertex == vertex_b
    assert edge_ab.loop == False

def test_add_weighted_and_oriented_neighbors():
    vertex_a = Vertex('a')
    vertex_b = Vertex('b')
    vertex_a.add_neighbor(vertex_b, weight=1.0, orientation='->')
    edge_ab = vertex_a.edge('a->b')
    assert vertex_b.label in vertex_a.neighbors.keys()
    assert vertex_b in vertex_a.neighbors.values()
    assert vertex_a.label in vertex_b.neighbors.keys()
    assert vertex_a in vertex_b.neighbors.values()
    assert 'a->b' in vertex_a.edges.keys()
    assert 'a->b' in vertex_b.edges.keys()
    assert vertex_a.loops == dict()
    assert vertex_b.loops == dict()
    assert edge_ab.label == 'a->b'
    assert edge_ab.weight == 1.0
    assert edge_ab.orientation == '->'
    assert edge_ab.start == vertex_a
    assert edge_ab.end == vertex_b
    assert edge_ab.left_vertex == vertex_a
    assert edge_ab.right_vertex == vertex_b
    assert edge_ab.loop == False

def test_add_unweighted_and_oriented_neighbors():
    vertex_a = Vertex('a')
    vertex_b = Vertex('b')
    vertex_a.add_neighbor(vertex_b, orientation='->')
    edge_ab = vertex_a.edge('a->b')
    assert vertex_b.label in vertex_a.neighbors.keys()
    assert vertex_b in vertex_a.neighbors.values()
    assert vertex_a.label in vertex_b.neighbors.keys()
    assert vertex_a in vertex_b.neighbors.values()
    assert 'a->b' in vertex_a.edges.keys()
    assert 'a->b' in vertex_b.edges.keys()
    assert vertex_a.loops == dict()
    assert vertex_b.loops == dict()
    assert edge_ab.label == 'a->b'
    assert edge_ab.weight == None
    assert edge_ab.orientation == '->'
    assert edge_ab.start == vertex_a
    assert edge_ab.end == vertex_b
    assert edge_ab.left_vertex == vertex_a
    assert edge_ab.right_vertex == vertex_b
    assert edge_ab.loop == False

def test_add_weighted_and_unoriented_neighbors():
    vertex_a = Vertex('a')
    vertex_b = Vertex('b')
    vertex_a.add_neighbor(vertex_b, weight=1.0)
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
    assert edge_ab.weight == 1.0
    assert edge_ab.orientation == '-'
    assert edge_ab.start == None
    assert edge_ab.end == None
    assert edge_ab.left_vertex == vertex_a
    assert edge_ab.right_vertex == vertex_b
    assert edge_ab.loop == False

def test_disconnect_neighbor():
    vertex_a = Vertex('a')
    vertex_b = Vertex('b')
    vertex_a.add_neighbor(vertex_b)
    vertex_a.disconnect_neighbor(vertex_b)
    assert vertex_b.label not in vertex_a.neighbors.keys()
    assert vertex_b not in vertex_a.neighbors.values()
    assert vertex_a.label not in vertex_b.neighbors.keys()
    assert vertex_a not in vertex_b.neighbors.values()
    assert 'a-b' not in vertex_a.edges.keys()
    assert 'a-b' not in vertex_b.edges.keys()
    assert vertex_a.loops == dict()
    assert vertex_b.loops == dict()

def test_get_neighbor():
    vertex_a = Vertex('a')
    vertex_b = Vertex('b')
    vertex_a.add_neighbor(vertex_b)
    assert vertex_a.get_neighbor(vertex_b.label) == vertex_b

def test_get_neighbor_none():
    vertex_a = Vertex('a')
    vertex_b = Vertex('b')
    vertex_a.add_neighbor(vertex_b)
    assert vertex_a.get_neighbor('c') == None

def test_remove_edge():
    vertex_a = Vertex('a')
    vertex_b = Vertex('b')
    vertex_a.add_neighbor(vertex_b)
    edge = vertex_a.edge('a-b')
    vertex_a.remove_edge(edge)
    assert vertex_b.label not in vertex_a.neighbors.keys()
    assert vertex_b not in vertex_a.neighbors.values()
    assert vertex_a.label not in vertex_b.neighbors.keys()
    assert vertex_a not in vertex_b.neighbors.values()
    assert 'a-b' not in vertex_a.edges.keys()
    assert 'a-b' not in vertex_b.edges.keys()
    assert vertex_a.loops == dict()
    assert vertex_b.loops == dict()