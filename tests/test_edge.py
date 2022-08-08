from optrees import Edge, Vertex


def test_default_initial_edge():
    vertex_a = Vertex('a')
    vertex_b = Vertex('b')
    edge_ab = Edge(vertex_a, vertex_b)
    assert edge_ab.label == 'a - b'
    assert edge_ab.weight == None
    assert edge_ab.orientation == '-'
    assert edge_ab.start == None
    assert edge_ab.end == None
    assert edge_ab.left_vertex == vertex_a
    assert edge_ab.right_vertex == vertex_b


def test_delete_edge():
    edge_ab = Edge(Vertex('a'), Vertex('b'))
    del edge_ab
    try:
        edge_ab
        check_exists = True
    except NameError:
        check_exists = False
    assert check_exists is False


def test_label():
    edge_ab = Edge(Vertex('a'), Vertex('b'))
    assert edge_ab.label == 'a - b'

def test_repr():
    edge_ab = Edge(Vertex('a'), Vertex('b'))
    assert edge_ab.__repr__() == f'Edge({edge_ab.label})'

def test_eq():
    vertex_a = Vertex('a')
    vertex_b = Vertex('b')
    edge_ab_first = Edge(vertex_a, vertex_b)
    edge_ab_second = Edge(vertex_a, vertex_b)
    assert edge_ab_first == edge_ab_second


def test_vertex_in_edge():
    vertex_a = Vertex('a')
    vertex_b = Vertex('b')
    edge_ab = Edge(vertex_a, vertex_b)
    assert vertex_a in edge_ab
    assert vertex_b in edge_ab


def test_vertex_not_in_edge():
    vertex_a = Vertex('a')
    vertex_b = Vertex('b')
    vertex_c = Vertex('c')
    edge_ab = Edge(vertex_a, vertex_b)
    assert vertex_c not in edge_ab


def test_left_vertex():
    vertex_a = Vertex('a')
    vertex_b = Vertex('b')
    edge_ab = Edge(vertex_a, vertex_b)
    assert edge_ab.left_vertex == vertex_a


def test_right_vertex():
    vertex_a = Vertex('a')
    vertex_b = Vertex('b')
    edge_ab = Edge(vertex_a, vertex_b)
    assert edge_ab.right_vertex == vertex_b


def test_weight():
    vertex_a = Vertex('a')
    vertex_b = Vertex('b')
    edge_ab = Edge(vertex_a, vertex_b, weight=1.0)
    assert edge_ab.weight == 1.0


def test_setter_weight():
    vertex_a = Vertex('a')
    vertex_b = Vertex('b')
    edge_ab = Edge(vertex_a, vertex_b, weight=1.0)
    edge_ab.weight = 2.0
    assert edge_ab.weight == 2.0


def test_orientation():
    vertex_a = Vertex('a')
    vertex_b = Vertex('b')
    edge_ab = Edge(vertex_a, vertex_b)
    assert edge_ab.orientation == '-'
    edge_ab_positive = Edge(vertex_a, vertex_b, orientation='->')
    assert edge_ab_positive.orientation == '->'
    edge_ab_negative = Edge(vertex_a, vertex_b, orientation='<-')
    assert edge_ab_negative.orientation == '<-'

def test_setter_orientation():
    vertex_a = Vertex("a")
    vertex_b = Vertex("b")
    edge_ab = Edge(vertex_a, vertex_b)
    edge_ab.orientation = '->'
    assert edge_ab.orientation == '->'
    edge_ab.orientation = '<-'
    assert edge_ab.orientation == '<-'
    edge_ab.orientation = '-'
    assert edge_ab.orientation == '-'
    try:
        edge_ab.orientation = '<>'
        check_exists = True
    except ValueError:
        check_exists = False
    assert check_exists is False


def test_start():
    vertex_a = Vertex('a')
    vertex_b = Vertex('b')
    edge_ab_positive = Edge(vertex_a, vertex_b, orientation='->')
    assert edge_ab_positive.start == vertex_a
    edge_ab_negative = Edge(vertex_a, vertex_b, orientation='<-')
    assert edge_ab_negative.start == vertex_b


def test_end():
    vertex_a = Vertex('a')
    vertex_b = Vertex('b')
    edge_ab_positive = Edge(vertex_a, vertex_b, orientation='->')
    assert edge_ab_positive.end == vertex_b
    edge_ab_negative = Edge(vertex_a, vertex_b, orientation='<-')
    assert edge_ab_negative.end == vertex_a
