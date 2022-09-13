# probabile complessità: primheap -> O(E+VlogV) + O(V^2*(V-k))

from collections import defaultdict
from ctypes import sizeof
import heapq
import networkx as nx
import matplotlib.pyplot as plt
import random
import heapq

# ------------------------------


def mst_prim(GRAFO, starting_vertex):
    graph = GRAFO.adj._atlas
    # defaultdict restituisce set() nel caso in cui la chiave non e' nel dizionario
    # lista di adiacenza
    mst = defaultdict(lambda: defaultdict(dict))

    # mst = {}

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

            mst[frm][to]['weight'] = cost


            # aggiungi archi incidenti al nuovo nodo

            for to_next, cost in graph[to].items():
                # tenedo conto dei gia' visitati
                if to_next not in visited:
                    # aggiungo arco ulteriore valutato alla heap che si riordina per costo
                    heapq.heappush(edges, (cost['weight'], to, to_next))

    return mst


def xor(x, y):
    return bool((x and not y) or (not x and y))


def find_leaf(g,r):
    leaf_nodes = []
    for node in g.nodes():
        if nx.degree(g, node) == 1:
            leaf_nodes.append(node)

    if r in leaf_nodes:
        leaf_nodes.remove(r)

    return leaf_nodes


def remove_nodes(grafo_partenza, lista_nodi_da_togliere):
    V_L = nx.Graph(grafo_partenza)
    for node in lista_nodi_da_togliere:
        V_L.remove_node(node)
    return V_L


def nearest_node(V, w):
    min_dist = float('inf')
    for v in V:
        if v != w:
            if nx.shortest_path_length(V, w, v) < min_dist:
                min_dist = nx.shortest_path_length(V, w, v)
                u = v
    return u


def shortest_connection_leaves(N,r):
    min_weight = float('inf')

    for f in find_leaf(N,r):
        for w in find_leaf(N,r):
            if f != w:

                # calcolo il peso della connessione tra due foglie
                peso_tmp = G.get_edge_data(f, w)['weight']

                # devo verificare che il nodo da cui stacco il collegamento non diventi un nodo foglia
                # ovvero è conncesso ad almeno a 2 nodi

                node_con_f = nearest_node(N, f)
               # verifico se il nodo adiacente è connesso almeno ad altri 2 nodi
                if (nx.degree(N, node_con_f) > 2):
                    peso_partenza = G.get_edge_data(f, node_con_f)['weight']
                else:
                    peso_partenza = float('inf')

               # --------------------------------------
                node_con_w = nearest_node(N, w)
                # verifico se il nodo adiacente è connesso almeno ad altri 2 nodi
                if (nx.degree(N, node_con_w) > 2):
                    peso_arrivo = G.get_edge_data(w, node_con_w)['weight']
                else:
                    peso_arrivo = float('inf')

                if(peso_arrivo != float('inf') and peso_partenza != float('inf')):
                    peso_tot = peso_tmp + min(peso_partenza, peso_arrivo)
                    if(peso_tot < min_weight):
                        min_weight = peso_tot
                        nodo_partenza = f
                        nodo_arrivo = w

                        if(peso_partenza >= peso_arrivo):
                            to_rem_start = f
                            to_remove = nearest_node(N, f)
                        else:
                            to_rem_start = w
                            to_remove = nearest_node(N, w)

                if(xor(peso_arrivo != float('inf'), peso_partenza != float('inf'))):
                    peso_tot = peso_tmp + min(peso_partenza, peso_arrivo)

                    if(peso_tot < min_weight):
                        min_weight = peso_tot
                        nodo_partenza = f
                        nodo_arrivo = w

                        if(peso_arrivo == float('inf')):
                            to_rem_start = nodo_partenza
                            to_remove = nearest_node(N, nodo_partenza)
                        else:
                            to_rem_start = nodo_arrivo
                            to_remove = nearest_node(N, nodo_arrivo)

    peso = G.get_edge_data(nodo_partenza, nodo_arrivo)['weight']
    N.add_edge(nodo_partenza, nodo_arrivo, weight=peso)
    N.remove_edge(to_rem_start, to_remove)

    return N


def plotGraph(Grafo, testo):
    pos = nx.get_node_attributes(Grafo, 'pos')
    plt.title(testo)
    nx.draw(Grafo, pos=positions, with_labels=True)
    labels = nx.get_edge_attributes(Grafo, 'weight')
    nx.draw_networkx_edge_labels(Grafo, pos=positions, edge_labels=labels)
    plt.show()
    print(nx.tree.branching_weight(Grafo))


def Kmin(Grafo, k, start_v):
    # T = nx.minimum_spanning_tree(Grafo, algorithm='prim')
    T = nx.Graph(mst_prim(Grafo, start_v))
    num_leaves = len(find_leaf(T,start_v))
    plotGraph(T, 'MST di radice ' + str(start_v))

    while (num_leaves > k):
        # ricerco la connessione che ha il valore minore e collego gli archi
        T = shortest_connection_leaves(T,start_v)

        num_leaves = len(find_leaf(T,start_v))
        print(num_leaves)

        plotGraph(T, 'Aggiornamento, numero di foglie: ' + str(num_leaves))

    return T


positions = {1: (5, 2), 2: (2, 1), 3: (3, 3), 4: (
    6, 1), 5: (7, 4), 6: (5, 4), 7: (4, 6),8: (1,1)}
all_nodes = [1, 2, 3, 4, 5, 6, 7,8]



G = nx.Graph()
G.add_node(1, pos=(4, 1))
G.add_node(2, pos=(2, 1))
G.add_node(3, pos=(3, 3))
G.add_node(4, pos=(6, 1))
G.add_node(5, pos=(7, 4))
G.add_node(6, pos=(5, 4))
G.add_node(7, pos=(4, 6))

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

# 4
G.add_edge(4, 5, weight=10)
G.add_edge(4, 6, weight=11)
G.add_edge(4, 7, weight=50)

# 5
G.add_edge(5, 7, weight=9)
G.add_edge(5, 6, weight=6)


# 6
G.add_edge(6, 7, weight=7)

# 8
G.add_edge(8, 2, weight=12)
G.add_edge(8, 7, weight=12)
G.add_edge(8, 3, weight=1)
G.add_edge(8, 4, weight=50)
G.add_edge(8, 5, weight=50)
G.add_edge(8, 6, weight=50)
G.add_edge(8, 1, weight=10) 

plotGraph(G, 'Grafo iniziale')





# Leaf Constrained Minimum Spannning Tree

# def Kmin(Grafo, k, start_v):
radice = 3
k = 3
T = Kmin(G, k, radice)
print(T.adj)

plotGraph(T, 'Finale, numero di foglie ' + str(len(find_leaf(T,radice)))+  ', costo totale: ' + str(nx.tree.branching_weight(T)))


