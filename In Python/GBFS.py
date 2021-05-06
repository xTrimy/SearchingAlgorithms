from queue import PriorityQueue

# Node of the graph
class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = list()
        self.visited = False

    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            #self.neighbors.sort()


class Graph:
    # Dictionary "Python" or Hashmap "Java" of Vertices in the graph =>key = vertex name, value = object of vertex
    vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    # Create edge between two vertices that already exists in the graph
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            # key = vertex name, value = object of vertex
            for key, value in self.vertices.items():
                # Adding each vertex name neighbour to the other vertex with cost
                if key == vertex1:
                    value.add_neighbor(vertex2)
                if key == vertex2:
                    value.add_neighbor(vertex1)
            return True
        else:
            return False

    # UCS Algorithm
    def uniform_cost_search(self, h, start, goal):
        count = 0
        frontier = PriorityQueue()
        frontier.put((0, [start]))
       
        while frontier:
            count += 1
            cost, node = frontier.get()
            current = self.vertices[node[len(node) - 1]]
            if current.visited == False:
                current.visited = True
                if current.name == goal:
                    print("Path found by UCS: " + str(node) + ", Count= " + str(count))
                    break
                for vertexName in current.neighbors:
                    if self.vertices[vertexName].visited == False:
                        temp = node[:]
                        temp.append(vertexName)
                        heuristicValue = h[vertexName]
                        frontier.put((heuristicValue, temp))
                print("Path till now", node)

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors))


# Create Graph
g = Graph()

vertices = ['Arad', 'Zerind', 'Timisoara', 'Sibiu', 'Oradea', 'Lugoj', 'RimnicuVilcea',
            'Mehadia', 'Craiova', 'Pitesti', 'Fagaras', 'Dobreta', 'Bucharest', 'Giurgiu']

for i in vertices:
    g.add_vertex(Vertex(i))

# g.print_graph()
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
        g.add_edge(vertex1, vertex2)

heuristicValue =  {'Arad': 366, 'Zerind': 374,
         'Timisoara':329,
         'Sibiu': 400,
         'Oradea': 380,
         'Lugoj': 244, 'RimnicuVilcea': 193,
         'Mehadia': 241, 'Craiova': 160,
         'Pitesti': 10, 'Fagaras': 176,
         'Dobreta': 242, 'Bucharest': 0,
         'Giurgiu': 77}

# g.print_graph()
g.uniform_cost_search(heuristicValue, 'Arad', "Bucharest")