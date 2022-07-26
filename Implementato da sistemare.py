# ordinato con funzione plot
from collections import defaultdict
from ctypes import sizeof
import heapq
import networkx as nx
import matplotlib.pyplot as plt
import random
import heapq


# https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.tree.mst.minimum_spanning_tree.html
# https://networkx.org/documentation/stable/tutorial.html

# heapq : priority queue algorithm.

#------------------------------

# mst prim di Sack
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

#------------------------------
def find_leaf(g):
    leaf_nodes = []
    for node in g.nodes():
        if nx.degree(g, node) == 1:
            leaf_nodes.append(node)
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


def plotGraph(Grafo,testo):
    pos = nx.get_node_attributes(Grafo, 'pos')
    plt.title(testo)
    nx.draw(Grafo, pos = positions, with_labels=True)
    labels = nx.get_edge_attributes(Grafo, 'weight')
    nx.draw_networkx_edge_labels(Grafo,pos = positions, edge_labels=labels)
    plt.show()   
    print(nx.tree.branching_weight(Grafo))


def LCMST(V, k):
    T = nx.minimum_spanning_tree(V,algorithm='prim')
    
    while len(find_leaf(T)) < k:
        L = find_leaf(T)

        max_len = float('inf')

        V_L = remove_nodes(V, L)
        for v in V_L:
            L1 = L.copy()
            # sono tutte le foglie di partenza + un nodo (che non era foglia)
            L1.append(v)

            T1 = nx.minimum_spanning_tree(remove_nodes(V, L1),algorithm='prim')
            for w in L1:
                # find nearest node in remove_nodes(V, L1) from w
                # remove w from L1
                L1_temp = L1.copy()
                L1_temp.remove(w)
                u = nearest_node(remove_nodes(V, L1_temp), w)

                T1.add_node(u)

                peso = remove_nodes(V, L1_temp).get_edge_data(w, u)['weight']
                T1.add_edge(w, u, weight=peso)
            if nx.tree.branching_weight(T1) < max_len:
                max_len = nx.tree.branching_weight(T1)
                T = T1.copy()
                plotGraph(T,'Step con nodo '+ str(u))
                
    return T



positions = {1:(4,1), 2:(2,1),3:(3,3),4:(6, 1),5:(7, 4),6:(5, 4),7:(4, 6)}
all_nodes= [1,2,3,4,5,6,7]


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
plotGraph(G,'Grafo iniziale')



#stavo implementando un convertitore di grafo per passare al formato di Sack
def Converti_formato_grafo(grafo):
    X = grafo.adj
    #accedo al Nested Dict
    tmp_Graph = {}
    for i in X.keys():   
        for j in X[i].keys():   
            for z in X[i][j].keys():
             h=(X[i][j]['weight'])

    return tmp_Graph
            
            
            
            


# Leaf Constrained Minimum Spannning Tree

T = LCMST(G, 6)
print(T)
print(find_leaf(T))
plotGraph(T,'Finale')


