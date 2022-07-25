import numpy as np
from scipy.spatial.distance import pdist, squareform
import matplotlib.pyplot as plt
import random


#algoritmo che conta il numero di foglie
#def leaves_num(T):
   # scorre l'albero con un ciclo for è per ogni percorso dal nodo cerca di scorrere lungo l'albero
   # salva su una variabile "from" il nodo da cui arriva e se i nodi ad essa collegati sono solo quello di arrivo allora è una foglia

def connected()

    for
    collegamenti = [
        (cost, to)
        for to, cost in graph[nodefrom].items() 
    ]

def minimum_spanning_tree(X, copy_X=True):
    """X are edge weights of fully connected graph"""
    if copy_X:
        X = X.copy()

    if X.shape[0] != X.shape[1]:
        raise ValueError("X needs to be square matrix of edge weights")
    n_vertices = X.shape[0]
    spanning_edges = []

    # initialize with node 0:
    visited_vertices = [0]
    num_visited = 1
    # exclude self connections:
    diag_indices = np.arange(n_vertices)
    X[diag_indices, diag_indices] = np.inf

    while num_visited != n_vertices:
        new_edge = np.argmin(X[visited_vertices], axis=None)
        # 2d encoding of new_edge from flat, get correct indices
        new_edge = divmod(new_edge, n_vertices)
        new_edge = [visited_vertices[new_edge[0]], new_edge[1]]
        # add edge to tree
        spanning_edges.append(new_edge)
        visited_vertices.append(new_edge[1])
        # remove all edges inside current tree
        X[visited_vertices, new_edge[1]] = np.inf
        X[new_edge[1], visited_vertices] = np.inf
        num_visited += 1
    return np.vstack(spanning_edges)


def test_mst():
    P = np.random.uniform(size=(50, 2))
    print(P)

    X = squareform(pdist(P))
    edge_list = minimum_spanning_tree(X)
    plt.scatter(P[:, 0], P[:, 1])

    for edge in edge_list:
        i, j = edge
        plt.plot([P[i, 0], P[j, 0]], [P[i, 1], P[j, 1]], c='r')
    plt.show()

graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 1, 'E': 4},
    'C': {'A': 3, 'B': 1, 'F': 5},
    'D': {'B': 1, 'E': 1},
    'E': {'B': 4, 'D': 1, 'F': 1},
    'F': {'C': 5, 'E': 1, 'G': 1},
    'G': {'F': 1},
}

if __name__ == "__main__":
    len = 100000000 #infinity

    nodefrom = 'A'



    print(collegamenti)
    
    test_mst()


