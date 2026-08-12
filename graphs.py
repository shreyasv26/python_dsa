# total degree of graph = 2 x no. of edges
# in degree n out degree = inward n outward edges to a node
# if there is no weight given we assume it as 1 unit

# Adjacency Matrix
# Space Complexity: O(N²)

# Number of nodes (n) and edges (m)
from collections import deque
from itertools import count
from typing import List

from strings import rotateString


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

# bfs in two ways

def bfs(start_node, adj):
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)

    while queue:
        node = queue.popleft()
        
        # Process node here (e.g., print(node))
        for neighbor in adj[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

def bfs_grid(grid, start_r, start_c):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start_r, start_c)])
    visited = set([(start_r, start_c)])
    
    # 4 directional movements (down, up, right, left)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        r, c = queue.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            # Boundary and condition checks
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc))


def orangesRotting(self, grid: List[List[int]]) -> int:
    if not grid:
        return 0
    
    row,col=len(grid),len(grid[0])
    count=0
    queue = deque()
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for r in range(row):
        for c in range(col):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh+= 1

    while queue:
        count+=1

        for _ in range(len(queue)):
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc]==1:
                    grid[nr][nc]=2
                    fresh-=1
                    queue.append((nr, nc))

    return count if fresh==0 else -1

def containsCycle(self, grid: List[List[str]]) -> bool:
    rows, cols = len(grid), len(grid[0])
    visited = set()

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    def dfs(r: int, c: int,pr:int,pc:int,char:str):
        visited.add((r, c))

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == char):
                if (nr,nc)==(pr,pc):
                    continue

# If neighbor is already visited and not parent -> Cycle detected!
                if (nr,nc) in visited:
                    return True
                
                if dfs(nr, nc,r,c,char):
                    return True
        return False

# Check every unvisited cell as a potential starting point
    for r in range(rows):
        for c in range(cols):
            if(r,c) not in visited:
                if dfs(r,c,-1,-1,grid[r][c]):
                    return True
                
    return False

# Muli-Source BFS

def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
#     Instead of starting at each 1 and searching outward to find the nearest 0 (which is slow and repeats work), we invert the problem:

# Start from all 0s at the exact same time.

# Expand outward level-by-level to neighboring 1s.

# The first time an expansion reaches a 1, that path is guaranteed to be the shortest distance to a 0.
    rows, cols = len(mat), len(mat[0])
    dist=[[-1] *cols for _ in range (rows)]
    queue = deque()

    for r in range(rows):
        for c in range(cols):
            if mat[r][c]==0:
                dist[r][c]=0
                queue.append((r,c))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

    while queue:
        r, c = queue.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if (0<=nr<rows and 0 <= nc < cols and dist[nr][nc] == -1):
                dist[nr][nc]=dist[r][c]+1 # Distance is current cell + 1
                queue.append((nr, nc))  # Add neighbor to queue for next level

    return dist

def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
    rows, cols = len(isWater), len(isWater[0])
    dist=[[-1] *cols for _ in range (rows)]
    queue = deque()

    for r in range(rows):
        for c in range(cols):
            if isWater[r][c]==1:
                dist[r][c]=0
                queue.append((r,c))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

    while queue:
        r, c = queue.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if (0<=nr<rows and 0 <= nc < cols and dist[nr][nc] == -1):
                dist[nr][nc]=dist[r][c]+1
                queue.append((nr, nc))

    return dist

def solve(self, board: list[list[str]]) -> None:
    rows, cols = len(board), len(board[0])

    def dfs(r: int, c: int):
        if r>=rows or r<0 or c>=cols or c<0 or board[r][c]!="O":
            return
        
        board[r][c] = "T"

        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
 
    for r in range(rows):
        if board[r][0]=="O":
            dfs(r,0)
        if board[r][cols-1]=='O':
            dfs(r,cols-1)

    for c in range(cols):
        if board[0][c]=='O':
            dfs(0,c)
        if board[rows-1][c]=='O':
            dfs(rows-1,c)

    for r in range(rows):
        for c in range(cols):
            if board[r][c]=='O':
                board[r][c]="X"
            elif board[r][c]=='T':
                board[r][c]='O'

def numEnclaves(self, grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])

    def dfs(r: int, c: int):
        if r>=rows or r<0 or c>=cols or c<0 or grid[r][c]!=1:
            return
        
        grid[r][c] = 0

        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
 
    for r in range(rows):
        if grid[r][0]==1:
            dfs(r,0)
        if grid[r][cols-1]==1:
            dfs(r,cols-1)

    for c in range(cols):
        if grid[0][c]==1:
            dfs(0,c)
        if grid[rows-1][c]==1:
            dfs(rows-1,c)

    count=0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c]==1:
                count+=1

    return count

