import collections
import numpy as np
import sys
import networkx as nx
from matplotlib import pyplot as plt
n = 300
k = 30

file = open("lcmstr300.10")
arr = np.genfromtxt(file, delimiter=' ', dtype=None)
graph = []
for i in range(n):
    data = {}
    for j in range(n):
        data[j] = arr[i][j]
    graph.append(data)

sort_graph = []
for dic in graph:
    data = sorted(dic.items(), key=lambda kv: (kv[1], kv[0]))
    data1 = collections.OrderedDict(data)
    sort_graph.append(data1)
# sort_graph[0]

centre = []
for i in range(k):
    index = 0
    min = 99
    for j in range(n):
        if j in centre:
            continue
        else:
            count = 0
            sum = 0
            for key, value in sort_graph[j].items():
                if key in centre:
                    continue
                else:
                    if(count < k):
                        sum = sum+value
                        count += 1
                    else:
                        break
            if(min > sum):
                min = sum
                index = j
    centre.append(index)
print(centre)


def minKey(key, mstSet):
    min = sys.float_info.max
    min_index = 0
    for v in range(n):
        #print("key value ",key[v], "of ", v)
        if (key[v] < min and mstSet[v] == False):
            min = key[v]
            min_index = v
            #print("selected ", key[v], "index ", v)
    return min_index


def primMST(x, graph, centre):
    tree = [[0 for x in range(n)] for y in range(n)]
    mstSet = [True]*n
    flag = [0]*n
    key = [sys.float_info.max]*n
    for a in range(0, k):
        mstSet[centre[a]] = False
    parent = [None] * n
    key[x] = 0.0
    parent[x] = -1
    for cout in range(k):
        u = minKey(key, mstSet)
        mstSet[u] = True
        #print("value of u ", u)

        for v in range(n):
            if(graph[u][v] > 0 and mstSet[v] == False and key[v] > graph[u][v]):
                parent[v] = u
                flag[v] = 1
                key[v] = graph[u][v]

    weight = 0.0
    for i in range(n):
        if(flag[i]):
            tree[parent[i]][i] = graph[parent[i]][i]
            tree[i][parent[i]] = graph[i][parent[i]]
    for i in range(n):
        for j in range(n):
            if(i <= j):
                weight += tree[i][j]
    # print(weight)
                # print(tree[i][j],end=",")
    # tree_plot(tree)
    return tree


def tree_plot(tree):
    l = []
    # file=open("b.txt")
    #arr = np.genfromtxt(file,delimiter=' ',dtype=None)
    arr = np.array(tree)
    # print(arr)
    for i in range(0, n):
        for j in range(0, n):
            if(arr[i][j] != 0.):
                l.append((i, j))
    # print(l)
    plt.figure(figsize=(10, 6))
    G = nx.DiGraph()
    G.add_edges_from(l)
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=205)
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='red')
    nx.draw_networkx_labels(G, pos)
    plt.show()


def make_tree():
    for i in range(n):
        if(leaf[i]):
            #print(i,end=" is leaf\n")
            min = sys.float_info.max
            temp = 0
            for values in centre:
                #print(values,end=" is int\n")
                #print(arr[i][values],end=" is weight\n")
                if(min > arr[i][values]):
                    min = arr[i][values]
                    # print(min)
                    temp = values
            #print(min,end="final min\n")
            tree[i][temp] = min
            tree[temp][i] = min


leaf = [1]*n
# print(intnode)
tree = primMST(centre[0], arr, centre)
for i in range(k):
    leaf[centre[i]] = 0
make_tree()
weight = 0.0
for i in range(n):
    for j in range(n):
        if(i <= j):
            weight += tree[i][j]
print(weight)
# tree_plot(tree)
