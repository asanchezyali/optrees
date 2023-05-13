## Documentation for the boruvka function

The `boruvka(graph: Graph)` function implements the Boruvka algorithm to find the minimum spanning tree of a connected
undirected graph. It takes as input a `Graph` object and returns another `Graph` object representing the minimum spanning
tree.

### Input Parameters:

- `graph: Graph`: A `Graph` object representing the connected undirected graph on which to find the minimum spanning tree.

### Return Value:

- `mst_graph: Graph`: A `Graph` object representing the minimum spanning tree of the input graph.

### Usage Example:

```python
from optrees import Graph, boruvka

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
    ("e", "f", 7),
]
graph = Graph("G")
graph.from_list(edges)

# Find the minimum spanning tree
mst_graph = boruvka(graph)

# Print the result
print(mst_graph)
```
