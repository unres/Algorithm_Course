# Takes in a G and returns a graph where i is all of the vertex
# and G[i] is the number of times that vertex is pointed to

def inDegrees(G):
  indegree = {}
  #invarient = 
  #varient = 
  # sets all the values of each vertex to 0
  for vertex in G:
      indegree[vertex] = 0    
  #invarient = 
  #varient = 
  #increments the value by 1 for each occurance 
  for vertex in G:
      #invarient = 
      #varient = 
      for edge in G[vertex]:
        indegree[edge] += 1
  return indegree
