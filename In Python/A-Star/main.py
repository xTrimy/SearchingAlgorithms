__author__ = "Mohamed Ashraf"

import networkx as nx
import scipy
import matplotlib.pyplot as plt
#####################################
import graph as g
import AStar
graph = g.graph
heuristic = g.heuristic
cost = g.cost
visited_nodes, optimal_nodes = AStar.run(graph, heuristic, cost, g.start,g.goal)

print(optimal_nodes)

G = nx.DiGraph()
graph_connections = []
graph_connections_with_cost = {}

for k, v in graph.items():
    for i in v:
        edge = (k+" "+str(heuristic[k]), i[0]+" "+str(heuristic[i[0]]))
        edges_with_costs = tuple((k+" "+str(heuristic[k]), i[0]+" "+str(heuristic[i[0]])))
        graph_connections.append(edge)
        graph_connections_with_cost[edges_with_costs] = i[1]


G.add_edges_from(graph_connections)

pos = nx.kamada_kawai_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=700, node_color='gray')

nx.draw_networkx_edge_labels(G, pos, edge_labels=graph_connections_with_cost,
                       font_color='black')
for i, (u, v, a) in enumerate(G.edges(data=True)):
    G[u][v]['color'] = 'black'


for i,n in enumerate(optimal_nodes[:-1]):
    node_name = str(optimal_nodes[i]) + " " + str(heuristic[n])
    next_node_name = str(optimal_nodes[i+1]) + " " + \
        str(heuristic[optimal_nodes[i+1]])
    for i, (u, v, a) in enumerate(G.edges(data=True)):
        if u == node_name and v == next_node_name:
            G[u][v]['color'] = 'red'
        elif v == node_name and u == next_node_name:
            G[u][v]['color'] = 'red'


colors = [G[u][v]['color'] for u, v in G.edges]

nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, edgelist=G.edges(),
                       edge_color=colors, arrows=False)
plt.show()

