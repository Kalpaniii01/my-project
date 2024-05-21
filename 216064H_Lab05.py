#Activity 01
class graph:
    def __init__(self,size):
        self.matrix = []
        for i in range (size):
            self.matrix.append([0]*size)
        self.size=size
def addEdge(self,u,v):
    self.matrix[u][v]=self.matrix[v][u]=1
def isEdge(self,u,v):
    if self.matrix[v][u]==1:
        return True
    else:
        return False
    
#bfs (Activity 02)  
graph = {
  'P' : ['Q','R'],
  'Q' : ['S', 'T'],
  'R' : ['U'],
  'S' : [],
  'T' : ['U'],
  'U' : []
}

visited = [] 
queue = []  

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for adjacent in graph[s]:
      if adjacent not in visited:
        visited.append(adjacent)
        queue.append(adjacent)

bfs(visited, graph, 'P')

#dfs (Activity 03)
graph = {
  'P' : ['Q','R'],
  'Q' : ['S', 'T'],
  'R' : ['U'],
  'S' : [],
  'T' : ['U'],
  'U' : []
}

visited = set()

def dfs(visited, graph, node):
        if node not in visited:
            print (node)
            visited.add(node)
            for adjacent in graph[node]:
                dfs(visited, graph, adjacent)

dfs(visited, graph, 'P')

print("Hi Kalpani")

a = 20
b = 30
x = a + b
print("X value is: " ,x)
