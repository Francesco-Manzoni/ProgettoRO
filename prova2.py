import networkx as nx
import matplotlib.pyplot as plt
# https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.tree.mst.minimum_spanning_tree.html
#https://networkx.org/documentation/stable/tutorial.html


 # per trovare nodi foglia
def find_leaf(g):
    leaf_nodes = []
    for node in g.nodes():
        if nx.degree(g, node) == 1:
            leaf_nodes.append(node)
    return leaf_nodes
  
    
def remove_nodes(grafo_partenza,lista_nodi_da_togliere):
    V_L = nx.Graph(grafo_partenza)
    for node in lista_nodi_da_togliere:
         V_L.remove_node(node)
    return V_L
    

def nearest_node(V, w):
    min_dist = float('inf')
    for v in V:
        if nx.shortest_path_length(V, w, v) < min_dist:
            min_dist = nx.shortest_path_length(V, w, v)
            u = v
    return u


# V = tutto il grafo
# T = mst (V)
# L = foglie di mst(V)
# V_L= V -L quindi tutto il grafo meno le foglie del risultato della prima MST
# L1 = L + 1 nodo proveniente da V-L
# u =

    
def LCMST(V,k):
    T = nx.minimum_spanning_tree(V)

    while len(find_leaf(T)) < k:
        L = find_leaf(T)

        max_len = float('inf')
        
        V_L = remove_nodes(V,L)
        for v in V_L:
            L1 = L.copy()
            L1.append(v) #sono tutte le foglie di partenza + un nodo (che non era foglia)

            T1 = nx.minimum_spanning_tree(remove_nodes(V, L1))
            for w in L1:
                #find nearest node in remove_nodes(V, L1) from w
                #remove w from L1
                L1_temp = L1.copy() 
                L1_temp.remove(w)
                u = nearest_node(remove_nodes(V, L1_temp), w)
                T1.add_edge(w, u, weight=nx.shortest_path_length(remove_nodes(V, L1_temp), w, u))
            if nx.shortest_path_length(T1, w, u) < max_len:
                max_len = nx.shortest_path_length(T1, w, u)
                T = T1.copy()
    return T



G = nx.Graph()
G.add_node(1, pos=(4, 1))
G.add_node(2, pos=(2, 1))
G.add_node(3, pos=(3, 3))
G.add_node(7, pos=(4, 6))
G.add_node(6, pos=(5, 4))
G.add_node(4, pos=(6, 1))
G.add_node(5, pos=(7, 4))

#1
G.add_edge(1, 2, weight=12)
G.add_edge(1, 7, weight=12)
G.add_edge(1, 3, weight=10)
G.add_edge(1, 4, weight=50)
G.add_edge(1, 5, weight=50)
G.add_edge(1, 6, weight=50)


#2
G.add_edge(2, 4, weight=12)
G.add_edge(2, 3, weight=8)
G.add_edge(2, 5, weight=50)
G.add_edge(2, 6, weight=50)
G.add_edge(2, 7, weight=50)

#3
G.add_edge(3, 4, weight=11)
G.add_edge(3, 6, weight=3)
G.add_edge(3, 7, weight=9)
G.add_edge(3, 5, weight=50)
G.add_edge(3, 6, weight=50)

#4
G.add_edge(4, 5, weight=10)
G.add_edge(4, 6, weight=11)
G.add_edge(4, 7, weight=50)

#5
G.add_edge(5, 7, weight=9)
G.add_edge(5, 6, weight=6)
G.add_edge(5, 7, weight=50)

#6
G.add_edge(6, 7, weight=7)






pos = nx.get_node_attributes(G, 'pos')
nx.draw(G, pos, with_labels=True)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()

# MST
mst = nx.minimum_spanning_tree(G)
pos = nx.get_node_attributes(mst, 'pos')
nx.draw(mst, pos, with_labels=True)
labels = nx.get_edge_attributes(mst, 'weight')
nx.draw_networkx_edge_labels(mst, pos, edge_labels=labels)
plt.show()
print(mst)




T = LCMST(G,5)
pos = nx.get_node_attributes(T, 'pos')
nx.draw(T, pos, with_labels=True)
labels = nx.get_edge_attributes(T, 'weight')
nx.draw_networkx_edge_labels(T, pos, edge_labels=labels)
plt.show()

                
                


    

