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

def test_add_neighbor_without_weight():
    vertex_a = Vertex('a')
    vertex_b = Vertex('b')
    vertex_a.add_neighbor(vertex_b)
    assert vertex_b.label in vertex_a.neighbors.keys()
    assert vertex_b in vertex_a.neighbors.values()
    assert vertex_a.label in vertex_b.neighbors.keys()
    assert vertex_a in vertex_b.neighbors.values()
    assert 'a-b' in vertex_a.edges.keys()
    assert 'a-b' in vertex_b.edges.keys()

def test_add_neighbor_with_weight():
    pass


        
    
    