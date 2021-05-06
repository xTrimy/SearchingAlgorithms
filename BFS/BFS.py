
from queue import Queue


romaniaMap = {
    'Arad': {'Zerind': 75, 'Sibiu': 140},
    'Zerind': {'Arad': 75, 'Oradea':71},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Sibiu': {'Oradea': 151, 'Fagaras': 99, 'RimnicuVilcea': 80},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Mehadia': {'Lugoj': 70, 'Dobreta': 75},
    'Craiova': {'Dobreta': 120, 'RimnicuVilcea': 146, 'Pitesti': 138},
    'Pitesti': {'RimnicuVilcea': 97, 'Craiova': 138},
    'Fagaras': {'Bucharest': 211},
    'Dobreta': {'Craiova': 120},
    'Giurgiu': {'Bucharest':90},
    'RimnicuVilcea': {'Sibiu':80, 'Craiova':146, 'Pitesti':97},
    'Bucharest': {'Pitesti': 101, 'Giurgiu': 90}
}

def bfs(startingNode, destinationNode):
    visited = {}
    distance = {}
    parent = {}
    bfs_traversal_output = []
    queue = Queue()

    for city in romaniaMap.keys():
        visited[city] = False
        parent[city] = None
        distance[city] = -1

    startingCity = startingNode
    visited[startingCity] = True
    distance[startingCity] = 0
    queue.put(startingCity)

    while not queue.empty():
        u = queue.get()     
        bfs_traversal_output.append(u)

        for v in romaniaMap[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                queue.put(v)

    g = destinationNode
    path = []
    while g is not None:
        path.append(g)
        g = parent[g]

    path.reverse()
    print(path)


#bfs('City1', 'City2')