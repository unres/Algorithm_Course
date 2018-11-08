
#homework
#closest_unvisted: {vertex, int} x [vertex] -> vertex
#Given the distances of all nodes through the source node,
#and the unvisited nodes, returns the one with the smallest distance
def closest_unvisited(distances, unvisited):
    smallest = unvisited[0]
    for elements in unvisited:
      if distances[elements] < distances[smallest]:
        smallest = elements
    return smallest

#find_neighbors: Graph x vertex -> Dict(vertex, int)
#Given a graph: G, and a vertex: current_node, return a dictionary (v, d) where
#v is a neighboring vertex to current_node, d is the distance to v from current_node
def find_neighbors(G, current_node):
    neighbors = {}
    for element in G.edges:
        if element.start == current_node:
            neighbors[element.end] = element.cost
        elif edge.end == current_node:
            neighbors[element.start] = element.cost
    return neighbors
#end homework


def make_edge(start, end, cost=1):
  return Edge(start, end, cost)

# we'll use infinity as a default distance to nodes.
inf = float('inf')

class Edge:
    def __init__(self, start, end, cost):
        self.start = start
        self.end = end
        self.cost = cost

    def print(self):
        print("Edge:",self.start,"-", self.end, ", ", self.cost)

class Graph:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = [make_edge(*edge) for edge in edges]
    def print(self):
        for v in self.vertices:
            print(v)
        for e in self.edges:
            e.print()

def dijkstra(G, source, dest):
    assert source in G.vertices

    unvisited_nodes = G.vertices.copy()

    #hint
    distances = {}
    for vertex in G.vertices:
        if(vertex == source):
            distances[vertex] = 0
        else:
            distances[vertex] = inf
    previous_vertices = {}
    for vertex in G.vertices:
        previous_vertices[vertex] = None


    # 1. Select the unvisited node with the smallest distance, 
    # it's current node now.
    while unvisited_nodes:
        current_node = closest_unvisited(distances, unvisited_nodes)

        # 4. Stop, if the smallest distance of unvisited nodes is infinity,
        #    or if we have reached the destination node
        if distances[current_node] == inf or current_node == dest:
            break
        # 2. Find unvisited neighbors for the current node 
        # and calculate their distances through the current node.
        neighbors = find_neighbors(G, current_node)
        for n in neighbors:
            possible_route = distances[current_node] + neighbors[n]

            # Compare the newly calculated distance to the assigned 
            # and save the smaller one.
            if possible_route < distances[n[0]]:
                distances[n[0]] = possible_route
                previous_vertices[n[0]] = current_node
        #3. Mark the current node as visited, and remove it from unvisited
        unvisited_nodes.remove(current_node)
                
    path = []
    current_step = dest
    while previous_vertices[current_step] is not None:
        path.append(current_step)
        current_step = previous_vertices[current_step]
    path.append(source)
    path.reverse()
    return path

#data
G = Graph(["a","b","c","d","e","f"],[
    ("a", "b", 7),  ("a", "c", 9),  ("a", "f", 14), ("b", "c", 10),
    ("b", "d", 15), ("c", "d", 11), ("c", "f", 2),  ("d", "e", 6),
    ("e", "f", 9)])


print(dijkstra(G, "a", "f"))
print(dijkstra(G, "a", "e"))
print(dijkstra(G, "b", "f"))
