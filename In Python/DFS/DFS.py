

def run(graph, startingNode, destinationNode):
    visited = []
    distance = {}
    parent = {}
    bfs_traversal_output = []
    stack = []
    for city in graph.keys():
        parent[city] = None
        distance[city] = -1

    startingCity = startingNode
    visited.append(startingCity)
    distance[startingCity] = 0
    stack.append(startingCity)

    while stack:
        u = stack.pop(-1)
        bfs_traversal_output.append(u)

        for v in graph[u]:
            node = v[0]
            if node not in visited:
                visited.append(node)
                parent[node] = u
                stack.append(node)

    g = destinationNode
    path = []
    while g is not None:
        path.append(g)
        g = parent[g]

    path.reverse()
    total_cost = 0
    for i, k in enumerate(path[:-1]):
        for j in graph[k]:
            if(path[i+1] == j[0]):
                total_cost += j[1]

    return path, total_cost
