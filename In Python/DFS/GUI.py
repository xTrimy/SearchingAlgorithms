import networkx as nx
import scipy
import matplotlib.pyplot as plt

import DFS

def GUIrun(start, goal, graph, heuristic, path, total_cost, startSelection, goalSelection):
    print(start)
    start = startSelection.get()
    goal = goalSelection.get()
    path, total_cost = DFS.run(graph, start, goal)
    graphGUI(start,goal, graph, heuristic, path)


def graphGUI(start, goal , graph, heuristic, path):
    G = nx.DiGraph()
    graph_connections = []
    graph_connections_with_cost = {}

    for k, v in graph.items():
        for i in v:
            edge = (k+" "+str(heuristic[k]), i[0]+" "+str(heuristic[i[0]]))
            edges_with_costs = tuple(
                (k+" "+str(heuristic[k]), i[0]+" "+str(heuristic[i[0]])))
            graph_connections.append(edge)
            graph_connections_with_cost[edges_with_costs] = i[1]

    G.add_edges_from(graph_connections)

    pos = nx.kamada_kawai_layout(G)

    nx.draw_networkx_edge_labels(G, pos, edge_labels=graph_connections_with_cost,
                                 font_color='black')
    for i, (u, v, a) in enumerate(G.edges(data=True)):
        G[u][v]['color'] = 'black'

    for i, n in enumerate(path[:-1]):
        node_name = str(path[i]) + " " + str(heuristic[n])
        next_node_name = str(path[i+1]) + " " + \
            str(heuristic[path[i+1]])
        for i, (u, v, a) in enumerate(G.edges(data=True)):
            if u == node_name and v == next_node_name:
                G[u][v]['color'] = 'red'
            elif v == node_name and u == next_node_name:
                G[u][v]['color'] = 'red'

    for u in G.nodes:
        if(start == u.split()[0]):
            G.nodes[u]['color'] = 'cyan'
        elif(goal == u.split()[0]):
            G.nodes[u]['color'] = 'green'
        else:
            G.nodes[u]['color'] = 'gray'

    colors = [G[u][v]['color'] for u, v in G.edges]
    colors_nodes = [G.nodes[u]['color'] for u in G.nodes]

    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(),
                           edge_color=colors, arrows=False)
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color=colors_nodes)

    plt.show()
