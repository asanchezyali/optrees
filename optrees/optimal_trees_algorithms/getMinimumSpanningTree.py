from optrees import Graph

from .boruvka import boruvka
from .kruskal import kruskal
from .prim import prim


def getMinimumSpanningTree(graph: Graph, algorithm: str = "boruvka"):
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
