#------------------------
# Linux ssh x11 setup
import matplotlib
matplotlib.use('TkAgg')
#------------------------
# Import function
import networkx as nx
import matplotlib.pyplot as plt
#------------------------

#------------------------
# Read setup data
f = open("setup.txt", "r")

evi = {}
for line in f:
    line = line.strip('\n').split()
    evi.update({line[0] : line[1]})

f.close()
#------------------------

#------------------------
# Generate Graph
plt.figure(figsize=(10,10))
G = nx.generators.geometric.waxman_graph(int(evi['nodes']), beta =float(evi['beta']), alpha = float(evi['alpha']), domain=(0, 0, int(evi['area']), int(evi['area'])))
pos = nx.classes.function.get_node_attributes(G, name = 'pos')

#nx.draw(G, pos=pos, with_labels = True, font_weight = 'bold')
#plt.show()

#plt.savefig("graph.png")

# Save Node info
f = open("Node_Topo_List.txt", "w")

f.write(str(evi['nodes']) + '\n')

for i, n in enumerate(pos):
    f.write(str(int(n)) + ' ' +  str(pos[i][0]) + ' ' + str(pos[i][1]) + '\n')

f.close()

# Save Edge info
f = open("Edge_Topo_List.txt", "w")

f.write(str(len(G.edges())) + '\n')

for i, e in enumerate(G.edges()):
    f.write(str(i) + ' ' + str(e[0]) + ' ' + str(e[1]) + '\n')

f.close()
#------------------------










