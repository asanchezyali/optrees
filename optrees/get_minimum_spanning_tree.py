from optrees import Graph

from .optimal_trees_algorithms.boruvka import boruvka
from .optimal_trees_algorithms.kruskal import kruskal
from .optimal_trees_algorithms.prim import prim


def get_minimum_spanning_tree(graph: Graph, algorithm: str = "boruvka"):
    algorithms = {
        "boruvka": boruvka,
        "kruskal": kruskal,
        "prim": prim,
    }
    if algorithm in algorithms:
        return algorithms[algorithm](graph)
    else:
        raise ValueError(
            f"Algorithm {algorithm} not found. "
            f"Available algorithms: {list(algorithms.keys())}"
        )
