from queue import PriorityQueue

class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = list()
        self.visited = False

    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)

class Graph:
    vertices = {}

    def New_Vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def New_Edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            for key, value in self.vertices.items():
                if key == vertex1:
                    value.add_neighbor(vertex2)
                if key == vertex2:
                    value.add_neighbor(vertex1)
            return True
        else:
            return False

    def UCS(self, h, start, goal):
        Counter = 0
        Frontier = PriorityQueue()
        Frontier.put((0, [start]))
       
        while Frontier:
            Counter += 1
            cost, node = Frontier.get()
            current = self.vertices[node[len(node) - 1]]
            if current.visited == False:
                current.visited = True
                if current.name == goal:
                    print("Path found by UCS: " + str(node) + ", Count= " + str(Counter))
                    break
                for vertexName in current.neighbors:
                    if self.vertices[vertexName].visited == False:
                        temp = node[:]
                        temp.append(vertexName)
                        heuristicValue = h[vertexName]
                        Frontier.put((heuristicValue, temp))
                print("Path till now", node)

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors))

g = Graph()

vertices = ['Arad', 'Zerind', 'Timisoara', 'Sibiu', 'Oradea', 'Lugoj', 'RimnicuVilcea',
            'Mehadia', 'Craiova', 'Pitesti', 'Fagaras', 'Dobreta', 'Bucharest', 'Giurgiu']

for i in vertices:
    g.New_Vertex(Vertex(i))

edges = {
    'Arad': {'Zerind', 'Sibiu'},
    'Timisoara': {'Arad', 'Lugoj'},
    'Sibiu': {'Oradea', 'Fagaras', 'RimnicuVilcea'},
    'Oradea': {'Zerind', 'Sibiu'},
    'Mehadia': {'Lugoj', 'Dobreta'},
    'Craiova': {'Dobreta', 'RimnicuVilcea', 'Pitesti'},
    'Pitesti': {'RimnicuVilcea', 'Craiova'},
    'Fagaras': {'Bucharest'},
    'Dobreta': {'Craiova'},
    'Bucharest': {'Pitesti', 'Giurgiu'}
}

print(type(vertices))

for vertex1, value in edges.items():
    for vertex2 in edges[vertex1]:
        g.New_Edge(vertex1, vertex2)

heuristicValue =  {'Arad': 366, 'Zerind': 374,
         'Timisoara':329,
         'Sibiu': 400,
         'Oradea': 380,
         'Lugoj': 244, 'RimnicuVilcea': 193,
         'Mehadia': 241, 'Cra   iova': 160,
         'Pitesti': 10, 'Fagaras': 176,
         'Dobreta': 242, 'Bucharest': 0,
         'Giurgiu': 77}

g.UCS(heuristicValue, 'Arad', "Bucharest")
