import networkx as nx
import matplotlib.pyplot as plt
# https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.tree.mst.minimum_spanning_tree.html

G = nx.Graph()
G.add_node('A', pos=(1, 1))
G.add_node('B', pos=(2, 2))
G.add_node('C', pos=(1, 0))
G.add_node('D', pos=(0, 1))
G.add_node('E', pos=(0, 0))
G.add_edge('A', 'B', weight=1)
G.add_edge('A', 'C', weight=3)
G.add_edge('B', 'C', weight=2)
G.add_edge('B', 'D', weight=4)
G.add_edge('C', 'D', weight=3)
G.add_edge('C', 'E', weight=6)
G.add_edge('D', 'E', weight=7)
G.add_edge('E', 'A', weight=1)
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
