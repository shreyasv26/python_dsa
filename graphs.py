# total degree of graph = 2 x no. of edges
# in degree n out degree = inward n outward edges to a node
# if there is no weight given we assume it as 1 unit

# Adjacency Matrix
# Space Complexity: O(N²)

# Number of nodes (n) and edges (m)
from collections import deque


n, m = map(int, input().split())

# map(int, ...)

# Applies the int() function to every element in that list, converting the string values into actual integers.

# 1-based indexing matrix initialized with zeros
adj = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u][v] = 1
    adj[v][u] = 1  # Omit this line for a directed graph

# Adjacency List
# Undirected Graph
# Space Complexity: O(2 × E)

n, m = map(int, input().split())

# List of lists for 1-based indexing
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)     # Directed edge from u to v
    adj[v].append(u)      #remove this for directed

# Adjacency List (Weighted)
# Stores tuples in the format (neighbor_node, weight)
n, m = map(int, input().split())

adj = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, weight = map(int, input().split())
    adj[u].append((v, weight))
    adj[v].append((u, weight))  # Omit for directed


# Traversal Techniques
 
def bfsOfGraph(self, V: int, adj: list[list[int]]) -> list[int]:
    # time complexity -> O( N + 2E ) 
        bfs = []
        vis = [False] * V
        q = deque()

        # Start BFS from node 0
        q.append(0)
        vis[0] = True

        while q:
            node = q.popleft()  
            bfs.append(node)

            # Traverse all adjacent vertices of the dequeued node
            for it in adj[node]:
                if not vis[it]:
                    vis[it] = True
                    q.append(it)

        return bfs

def dfsOfGraph(self, V: int, adj: list[list[int]],vis:list[bool],result:list[int]) -> list[int]:
    vis[V]=True
    result.append(V)

    for i in adj[V]:
         if not vis[i]:
              self.dfsOfGraph(i,adj,vis,result)

# adj = [[] for _ in range(V)]
# adj[0] = [1, 2]
# adj[1] = [0, 3]
# adj[2] = [0, 4]
# adj[3] = [1]
# adj[4] = [2]

def findCircleNum(self, isConnected: List[List[int]]) -> int:
    n=len(isConnected)
    adj=[[] for _ in range(n)]

    for i in range(n):
        for j in range(i+1,n):
            if isConnected[i][j]==1:
                adj[i].append(j)
                adj[j].append(i)

    count=0
    vis=[0]*n

    def dfs(node):
        vis[node]=1
        for i in adj[node]:
            if vis[i]==0:
                dfs(i)

    for i in range(len(vis)):
        if vis[i]==0:
            count+=1
            dfs(i)

    return count

def numIslands(self, grid: List[List[str]]) -> int:
    if not grid:
        return 0
    
    row,col=len(grid),len(grid[0])
    count=0

    def dfs(r,c):
        if r>=row or r<0 or c>=col or c<0 or grid[r][c]=='0':
            return
        
        grid[r][c]='0'

        dfs(r,c-1)
        dfs(r,c+1)
        dfs(r-1,c)
        dfs(r+1,c)

    for r in range(row):
        for c in range(col):
            if grid[r][c]=='1':
                count+=1
                dfs(r,c)

    return count

def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    if not image:
        return image
    
    row,col=len(image),len(image[0])
    x=image[sr][sc]

    if x==color:
        return image

    def dfs(r,c):
        if r>=row or r<0 or c>=col or c<0 or image[r][c]!=x:
            return
        
        image[r][c]=color

        dfs(r,c-1)
        dfs(r,c+1)
        dfs(r-1,c)
        dfs(r+1,c)

    dfs(sr,sc)

    return image
