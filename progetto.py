from collections import defaultdict
import heapq

# heapq : priority queue algorithm.
#prova test update 

#pelle


def mst_prim(graph, starting_vertex):
    # defaultdict restituisce set() nel caso in cui la chiave non e' nel dizionario
    # lista di adiacenza
    mst = defaultdict(set)
    # all'inizio apro solo starting_vertex
    visited = set([starting_vertex]) #'F':{}
    # archi incidenti allo starting_vertex
    edges = [
        (cost, starting_vertex, to)
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
                    heapq.heappush(edges, (cost, to, to_next)) #aggiungo arco ulteriore valutato alla heap che si riordina per costo

    return mst

example_graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 1, 'E': 4},
    'C': {'A': 3, 'B': 1, 'F': 5},
    'D': {'B': 1, 'E': 1},
    'E': {'B': 4, 'D': 1, 'F': 1},
    'F': {'C': 5, 'E': 1, 'G': 1},
    'G': {'F': 1},
}

example_graph1 = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 1, 'E': 4,'H':10},
    'C': {'A': 3, 'B': 1, 'F': 5},
    'D': {'B': 1, 'E': 1},
    'E': {'B': 4, 'D': 1, 'F': 1},
    'F': {'C': 5, 'E': 1, 'G': 1}, 
    'G': {'F': 1},
    'H': {'B': 10},
}
print(mst_prim(example_graph,'F'))