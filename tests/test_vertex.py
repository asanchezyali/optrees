from optrees import Vertex

def test_default_initial_vertex():
    vertex_a = Vertex('a')
    assert vertex_a.label == 'a'
    assert vertex_a.edges == dict()
    assert vertex_a.neighbors == dict()

def test_delete_vertex():
    vertex_a = Vertex('a')
    del vertex_a
    try:
        vertex_a
        check_exists = True
    except NameError:
        check_exists = False
    assert check_exists == False

def test_str():
    vertex_a = Vertex('a')
    assert vertex_a.__str__() == vertex_a.label

def test_repr():
    vertex_a = Vertex('a')
    assert vertex_a.__repr__() == f'Vertex({vertex_a.label})'

def test_eq():
    vertex_a = Vertex('a')
    vertex_b = Vertex('a')
    assert vertex_a == vertex_b

def test_label():
    vertex_a = Vertex('a')
    assert vertex_a.label == 'a'

def test_add_neighbor():
    vertex_a = Vertex('a')
    vertex_b = Vertex('b')
    vertex_a.add_neighbor(vertex_b)
    assert vertex_a.neighbors == {'b': vertex_b}
    assert vertex_b.neighbors == {'a': vertex_a}

def test_amount_of_neighbors():
    vertex_a = Vertex('a')
    vertex_b = Vertex('b')
    vertex_a.add_neighbor(vertex_b)
    assert vertex_a.amount_of_neighbors() == 1
    assert vertex_b.amount_of_neighbors() == 1

def test_amount_of_edges():
    vertex_a = Vertex('a')
    vertex_b = Vertex('b')
    vertex_a.add_neighbor(vertex_b)
    assert vertex_a.amount_of_edges() == 1
    assert vertex_b.amount_of_edges() == 1

def test_is_isolated():
    vertex_a = Vertex('a')
    assert vertex_a.is_isolated() == True
    vertex_b = Vertex('b')
    vertex_a.add_neighbor(vertex_b)
    assert vertex_a.is_isolated() == False
    assert vertex_b.is_isolated() == False