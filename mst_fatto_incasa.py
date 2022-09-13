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