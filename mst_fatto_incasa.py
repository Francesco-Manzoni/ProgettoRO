import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict
from ctypes import sizeof
import heapq


def mst_prim(GRAFO, starting_vertex):
    graph = GRAFO.adj._atlas
    # defaultdict restituisce set() nel caso in cui la chiave non e' nel dizionario
    # lista di adiacenza
    mst = defaultdict(set)

    # all'inizio apro solo starting_vertex
    visited = set([starting_vertex])  # 'F':{}
    # archi incidenti allo starting_vertex
    edges = [
        (cost['weight'], starting_vertex, to)
        for to, cost in graph[starting_vertex].items()
    ]
    # crea coda heap basata su min costo vertici
    heapq.heapify(edges)

    while edges:
        # estaggo il minimo
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            # aggiungi nodo ai visitati
            visited.add(to)

            # esapndi albero
            mst[frm].add(to)
            # aggiungi archi incidenti al nuovo nodo

            for to_next, cost in graph[to].items():
                # tenedo conto dei gia' visitati
                if to_next not in visited:
                    # aggiungo arco ulteriore valutato alla heap che si riordina per costo
                    heapq.heappush(edges, (cost['weight'], to, to_next))

    return mst


G = nx.Graph()
G.add_node(1, pos=(4, 1))
G.add_node(2, pos=(2, 1))
G.add_node(3, pos=(3, 3))
G.add_node(7, pos=(4, 6))
G.add_node(6, pos=(5, 4))
G.add_node(4, pos=(6, 1))
G.add_node(5, pos=(7, 4))

# 1
G.add_edge(1, 2, weight=12)
G.add_edge(1, 7, weight=12)
G.add_edge(1, 3, weight=10)
G.add_edge(1, 4, weight=50)
G.add_edge(1, 5, weight=50)
G.add_edge(1, 6, weight=50)


# 2
G.add_edge(2, 4, weight=12)
G.add_edge(2, 3, weight=8)
G.add_edge(2, 5, weight=50)
G.add_edge(2, 6, weight=50)
G.add_edge(2, 7, weight=50)

# 3
G.add_edge(3, 4, weight=11)
G.add_edge(3, 6, weight=3)
G.add_edge(3, 7, weight=9)
G.add_edge(3, 5, weight=50)
G.add_edge(3, 6, weight=50)

# 4
G.add_edge(4, 5, weight=10)
G.add_edge(4, 6, weight=11)
G.add_edge(4, 7, weight=50)

# 5
G.add_edge(5, 7, weight=9)
G.add_edge(5, 6, weight=6)
G.add_edge(5, 7, weight=50)

# 6
G.add_edge(6, 7, weight=7)

nx.minimmum

T = mst_prim(G, 3)
