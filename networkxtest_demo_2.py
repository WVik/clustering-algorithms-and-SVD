import networkx as nx
import matplotlib.pyplot as plt
G=nx.Graph()
file = open("./dataset.txt")
for line in file:
    content = line.strip().split()
    fr = int(content[0])
    to = int(content[1])
    G.add_edge(fr,to)

nx.draw(G, node_size=30)
plt.show()
