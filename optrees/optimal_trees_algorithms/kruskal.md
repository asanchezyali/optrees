## Documentation for function kruskal

The `kruskal(graph: Graph)` function implements Kruskal's algorithm to find the Minimum Spanning Tree of an undirected
and connected graph. It takes as input a `Graph` object and returns another `Graph` object that represents the Minimum
Spanning Tree.

### Input parameters:
- `graph: Graph`: A `Graph` object representing the undirected and connected graph on which to find the Minimum Spanning
Tree.

### Return value:
- `mst_graph: Graph`: A `Graph` object representing the Minimum Spanning Tree of the input graph.

### Example usage:
```python
from optrees import Graph, kruskal

# Create example graph
edges = [
    ("a", "b", 1),
    ("a", "d", 4),
    ("a", "e", 3),
    ("b", "d", 4),
    ("b", "e", 2),
    ("c", "e", 4),
    ("c", "f", 5),
    ("d", "e", 4),
    ("e", "f", 7)
]
graph = Graph("G")
graph.from_list(edges)

# Find Minimum Spanning Tree
mst_graph = kruskal(graph)

# Print result
print(mst_graph)
