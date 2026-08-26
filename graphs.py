# total degree of graph = 2 x no. of edges
# in degree n out degree = inward n outward edges to a node
# if there is no weight given we assume it as 1 unit

# Adjacency Matrix
# Space Complexity: O(N²)

# Number of nodes (n) and edges (m)
from ast import Return
from asyncio import graph
from collections import deque
from curses import start_color
import heapq
from itertools import count
from multiprocessing import heap
from typing import List

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
    adj[v].append(u)     # remove this for directed

# Adjacency List (Weighted)
# Stores tuples in the format (neighbor_node, weight)
n, m = map(int, input().split())

adj = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, weight = map(int, input().split())
    adj[u].append((v, weight))
    adj[v].append((u, weight))  # Omit for directed

# adj = [[] for _ in range(V)]
# adj[0] = [1, 2]
# adj[1] = [0, 3]
# adj[2] = [0, 4]
# adj[3] = [1]
# adj[4] = [2]

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

            # Traver se all adjacent vertices of the dequeued node
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

def dfs_matrix(grid: list[list[int]], start_r: int, start_c: int):
    rows, cols = len(grid), len(grid[0])
    visited = set()

    def dfs(r: int, c: int):
        # 1. Base Case: Out of bounds or already visited
        if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited:
            return
        
        # Add grid conditions here if needed (e.g., if grid[r][c] == 0: return)

        # 2. Mark visited
        visited.add((r, c))

        # 3. Explore 4 directions
        dfs(r + 1, c) # Down
        dfs(r - 1, c) # Up
        dfs(r, c + 1) # Right
        dfs(r, c - 1) # Left

    dfs(start_r, start_c)
    
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

def bfs_matrix(grid: list[list[int]], start_r: int, start_c: int):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start_r, start_c)])
    visited = set([(start_r, start_c)])
    
    # 4-directional moves: Down, Up, Right, Left
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        r, c = queue.popleft()
        
        # Process current cell here if needed
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            # Boundary & Visited Check
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                # Add grid conditions here if needed (e.g., grid[nr][nc] == 1)
                visited.add((nr, nc))
                queue.append((nr, nc))


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

    def dfs(r,c) -> None:
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

def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    if not grid:
        return 0
    
    row,col=len(grid),len(grid[0])
    self.maxsize=0
    self.size=0

    def dfs(r,c):
        if r>=row or r<0 or c>=col or c<0 or grid[r][c]==0:
            return
        
        grid[r][c]=0
        self.size+=1
        self.maxsize=max(self.size,self.maxsize)

        dfs(r,c-1)
        dfs(r,c+1)
        dfs(r-1,c)
        dfs(r+1,c)

    for r in range(row):
        for c in range(col):
            if grid[r][c]==1:
                self.size=0
                dfs(r,c)
    
    return self.maxsize

def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    if not image:
        return image
    
    row,col=len(image),len(image[0])
    x=image[sr][sc]

    if x==color:
        return image

    def dfs(r,c) -> None:
        if r>=row or r<0 or c>=col or c<0 or image[r][c]!=x:
            return
        
        image[r][c]=color

        dfs(r,c-1)
        dfs(r,c+1)
        dfs(r-1,c)
        dfs(r+1,c)

    dfs(sr,sc)

    return image

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

def maxDistance(self, grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    dist=[[-1] *cols for _ in range (rows)]
    queue = deque()

    for r in range(rows):
        for c in range(cols):
            if grid[r][c]==1:
                dist[r][c]=0
                queue.append((r,c))

    if len(queue) == 0 or len(queue) == rows * cols:
        return -1

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
    maxdist=0

    while queue:
        r, c = queue.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if (0<=nr<rows and 0 <= nc < cols and dist[nr][nc] == -1):
                dist[nr][nc]=dist[r][c]+1
                maxdist=max(maxdist,dist[nr][nc])
                queue.append((nr, nc))  

    return maxdist

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

def isBipartite(self, graph: List[List[int]]) -> bool:
    color = [-1] * len(graph)
    q = deque()

    for i in range(len(graph)):
        q.append(i)
        color[i] = 0

        while q:
            node = q.popleft() 
            if color[i]!=-1:
                continue 

            for it in graph[node]:
                if color[it]==-1:
                    color[it] = 0 if color[node]==1 else 1
                    q.append(it)
                elif color[it]== color[node]:
                    return False

    return True

def isBipartite(self, graph: List[List[int]]) -> bool:
    color = [-1] * len(graph)

    def dfs(node):
        color[i]=0
        for it in graph[node]:
            if color[it]==-1:
                color[it] = 0 if color[node]==1 else 1
                if dfs(it) is False:
                    return False
            elif color[it]== color[node]:
                return False
        return True

    for i in range(len(graph)):
        if color[i]==-1:
            color[i]=0
            if dfs(i) is False:
                return False

    return True

class DirectedGraph:
    def isCyclic(self, V: int, edges: list[list[int]]) -> bool:
        adj = [[] for _ in range(V)]
        vis = [False] * V
        pathvis = [False] * V

        for u, v in edges:
            adj[u].append(v)

        for i in range(V):
            if not vis[i]:
                if self.dfs(i, adj, vis, pathvis):
                    return True

        return False
            
    def dfs(self,node:int,adj:list[list[int]],vis:list[int],pathvis:list[int]) -> bool:
        vis[node]=True
        pathvis[node]=True

        for i in adj[node]:
            if not vis[i]:
                if self.dfs(i,adj,vis,pathvis):
                    return True
            elif pathvis[i]:
                return True
                
        pathvis[node]=False
        return False
        
def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
    n=len(graph)
    vis=[False]*n
    pathvis=[False]*n
    check=[False]*n
    safenode=[]

    def dfs(node):
        vis[node]=True
        pathvis[node]=True

        for i in graph[node]:
            # If neighbor is unvisited, recurse
            if not vis[i]:
                if dfs(i):
                    check[node]=False
                    return True
        # If neighbor is already in the current path, cycle found
            elif pathvis[i]:
                check[node]=False
                return True
        # Node is safe if no cycle is reachable from it
        check[node]=True
        pathvis[node]=False
        return False

    for i in range(n):
        if not vis[i]:
            dfs(i)

    for i in range(n):
        if check[i]:
            safenode.append(i)

    return safenode

def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        vis = [False] * numCourses
        pathvis = [False] * numCourses

        # Build graph: [a, b] means b -> a (to take 'a', take 'b' first)
        for dest, src in prerequisites:
            adj[src].append(dest)

        # Detect cycle using DFS
        def dfs(node):
            vis[node] = True
            pathvis[node] = True

            for neighbor in adj[node]:
                if not vis[neighbor]:
                    if dfs(neighbor):
                        return True
                elif pathvis[neighbor]:
                    return True

            pathvis[node] = False
            return False

        # If a cycle exists anywhere, you CANNOT finish
        for i in range(numCourses):
            if not vis[i]:
                if dfs(i):
                    return False

        return True

# Topological Sort Algo iS on DAG(Directed Acyclic Graph)
# why DAG bc we have to do linear ordering of nodes but if its a cycle we cant do that
# such that u-> v  u apppears before v

def topoSort(self, V: int, edges: list[list[int]]) -> list[int]:
    # using dfs such that u-> v  u apppears before v
    adj = [[] for _ in range(V)]
    for u, v in edges:
        adj[u].append(v)

    vis=[False]*V
    stack=[]

    def dfs (node):
        vis[node]=True

        for it in adj[node]:
            if not vis[it]:
                dfs(it)
        
        stack.append(node)

    for i in range(V):
        if not vis[i]:
            dfs(i)

    return stack[::-1]

def KhansAlgoTopologicalSort(self, V, ad) -> list:
        # Create a list to store in-degree of each vertex
        indegree = [0] * V

        # Loop over all vertices to calculate in-degree
        for i in range(V):
            # Loop through adjacent vertices
            for it in adj[i]:
                # Increase in-degree of connected vertex
                indegree[it] += 1

        q = deque()

        # Loop through all vertices
        for i in range(V):
            # If in-degree is zero, add to queue
            if indegree[i] == 0:
                q.append(i)

        topo = []

        while q:
            node = q.popleft()
            # Add it to the topological order
            topo.append(node)

            for it in adj[node]:
                # Reduce in-degree of connected vertex
                indegree[it] -= 1
                # If in-degree becomes zero, push into queue
                if indegree[it] == 0:
                    q.append(it)

        return topo

def isCyclic(self, V: int, edges: list[list[int]]) -> bool:
    # logic is we cannot do full topo sort on cyclic graph
    indeg=[0]*V
    topo=[]
    q=deque()
    adj=[[] for _ in range (V)]

    for u,v in edges:
        adj[u].append(v)

    for i in range(V):
        for it in adj[i]:
            indeg[it]+=1

    for i in range(V):
        if indeg[i]==0:
            q.append(i)

    while q:
        node=q.popleft()
        topo.append(node)

        for it in adj[node]:
            indeg[it]-=1

            if indeg[it]==0:
                q.append(it)

    if len(topo)==V:
        return False
    else:
        return True

class CourseSchedule:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # logic if we can assign in a linear order then we can do all tasks i.e topo sort but if not i.e cycel present we cant perform all task
        adj = [[] for _ in range(numCourses)]
        indeg=[0]*numCourses
        topo=[]
        q=deque()

        for dest, src in prerequisites:
            adj[src].append(dest)    

        for i in range(numCourses):
            for it in adj[i]:
                indeg[it]+=1

        for i in range(numCourses):
            if indeg[i]==0:
                q.append(i)

        while q:
            node=q.popleft()
            topo.append(node)

            for it in adj[node]:
                indeg[it]-=1

                if indeg[it]==0:
                    q.append(it)

        if len(topo)==numCourses:
            return True
        else:
            return False

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indeg=[0]*numCourses
        topo=[]
        q=deque()

        for dest, src in prerequisites:
            adj[src].append(dest)    

        for i in range(numCourses):
            for it in adj[i]:
                indeg[it]+=1

        for i in range(numCourses):
            if indeg[i]==0:
                q.append(i)

        while q:
            node=q.popleft()
            topo.append(node)

            for it in adj[node]:
                indeg[it]-=1

                if indeg[it]==0:
                    q.append(it)

        if len(topo)==numCourses:
            return topo
        else:
            return []

def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
    V=len(graph)
    indeg=[0]*V
    topo=[]
    adj=[[] for _ in range(V)]
    for i in range(V):
        for it in graph[i]:
            adj[it].append(i)
            indeg[i]+=1

    q=deque()

    for i in range(V):
        if indeg[i]==0:
            q.append(i)

    while q:
        node=q.popleft()
        topo.append(node)

        for it in adj[node]:
            indeg[it]-=1

            if indeg[it]==0:
                q.append(it)

    return sorted(topo)

def alienDict(self, words: list[str]) -> str:
    n = len(words)
    adj=[[] for _ in range(26)]
    present = [False] * 26

    for w in words:
      for ch in w:
        present[ord(ch) - ord("a")] = True

    for i in range(n-1):
        s1=words[i]
        s2=words[i+1]
        leng=min(len(s1),len(s2))

        # if len(s1) > len(s2) and s1[:leng] == s2[:leng]:
        #     return ""

        for j in range(leng):
            if s1[j]!=s2[j]:
                adj[ord(s1[j]) - ord('a')].append(ord(s2[j]) - ord('a'))
                break

    def KhansAlgoTopologicalSort(V, adj):
        indegree = [0] * V

        for i in range(V):
            for it in adj[i]:
                indegree[it] += 1

        q = deque()

        for i in range(V):
            if present[i] and indegree[i] == 0:
                q.append(i)

        topo = []

        while q:
            node = q.popleft()
            topo.append(node)

            for it in adj[node]:
                indegree[it] -= 1
                if indegree[it] == 0:
                    q.append(it)

        return topo  

    topo=KhansAlgoTopologicalSort(26,adj)

    if len(topo)==sum(present):
        # ans = "".join(chr(it + ord('a')) for it in topo) 
        ans=''
        for it in topo:
            ans+=chr(it+ord('a'))

        return ans
    else:
        return ''

def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        res = []

        def dfs(node: int, path: List[int]):
            if node == target:
                res.append(list(path))
                return

            for neighbor in graph[node]:
                path.append(neighbor)
                dfs(neighbor, path)
                path.pop()  

        dfs(0, [0])
        return res

def shortestPathDirected(self, V: int, edges: list[list[int]]) -> list[int]:
    dist=[float('inf')]*V
    topo=[]
    vis=[False]*V
    adj=[[] for _ in range(V)]

    for u,v,wt in edges:
        adj[u].append((v,wt))

    def toposortdfs(node):
        vis[node]=True
        for it,wt in adj[node]:
            if not vis[it]:
                toposortdfs(it)
        topo.append(node)

    for i in range(V):
        if not vis[i]:
            toposortdfs(i)

    dist[0]=0

    while topo:
        node=topo.pop()
        if dist[node] != float('inf'):
            for it,wt in adj[node]:
                if dist[node]+wt<dist[it]:
                    dist[it]=dist[node]+wt

    return [d if d != float('inf') else -1 for d in dist]

def shortestCostUndirected(self, V, edges, src, dest):
    adj = [[] for _ in range(V)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    dist = [-1] * V
    dist[src] = 0
    q = deque([src])

    while q:
        node = q.popleft()

        if node == dest:
            return dist[node]

        for neighbor in adj[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                q.append(neighbor)

    return -1

def shortestPathUnDirected(self, V: int, edges: list[list[int]] ) -> list[int]:
    adj=[[] for _ in range(V)]
    for u,v in edges:
        adj[u].append(v)
        adj[v].append(u)

    dist=[-1]*V
    dist[0]=0
    q=deque([0])

    while q:
        node=q.popleft()

        for i in adj[node]:
            if dist[i] == -1:
                dist[i] = dist[node] + 1
                q.append(i)

    return dist

def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        
        # If endWord is not in the dictionary, no valid sequence exists
        if endWord not in word_set:
            return 0

        # Queue stores tuples of (current_word, current_transformation_length)
        queue = deque([(beginWord, 1)])
        
        while queue:
            word, length = queue.popleft()
            
            # Target word reached
            if word == endWord:
                return length
            
            # Try changing each character from 'a' through 'z'
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    
                    if next_word in word_set:
                        word_set.remove(next_word)  # Mark as visited to avoid cycles
                        queue.append((next_word, length + 1))
                        
        return 0

def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    word_set=set(wordList)
    res=[]

    if endWord not in word_set:
        return []
    
    q=deque([[beginWord]])
    visited_this_level = set()

    while q:
        level_size=len(q)

        for _ in range(level_size):

            path = q.popleft()
            word=path[-1]

            if word == endWord:
                res.append(path)
                continue
                
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                        
                    if next_word in word_set:
                        visited_this_level.add(next_word) 
                        q.append(path+[next_word])
        if res:
            break

        word_set-=visited_this_level
        visited_this_level.clear()

    return res

# Dijkstra's Algorithm  TC: O(E logV)
def dijkstra(self, V: int, edges: list[list[int]], src: int) -> list[int]:
    adj = [[] for _ in range(V)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))

    # 2. Priority Queue storing (distance, node)
    pq = [(0, src)]
    dist = [float('inf')] * V
    dist[src] = 0

    while pq:
        # gives min distance
        cdis, cnode = heapq.heappop(pq)

        # Ignore outdated distances
        if cdis > dist[cnode]:
                continue

        # Relax neighbors
        for inode, weight in adj[cnode]:
            dis = cdis + weight

            if dis < dist[inode]:
                dist[inode] = dis
                heapq.heappush(pq, (dis, inode))

    return dist

def dijkstraPath(self, V: int, edges: list[list[int]], src: int, dest:int) -> list[int]:
    # shortest path
    adj = [[] for _ in range(V+1)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))

    pq = [(0,src)] # src=1
    dist = [float('inf')] * (V+1)
    dist[src] = 0
    parent=list(range(V+1))

    while pq:
        currdist,currnode=heapq.heappop(pq)

        if currdist>dist[currnode]:
            continue  #bc older larger dist should be removed

        for node,weight in adj[currnode]:
            dis=currdist+weight

            if dis<dist[node]:
                dist[node]=dis
                parent[node]=currnode
                heapq.heappush(pq,(dis,node))

    if dist[dest]==float('inf'):
        return [-1] 
    
    node=dist
    path=[]
    while parent[node]!=node:
        path.append(node)
        node=parent[node]

    path.append(src)
    return path[::-1] # reverse the list n return bc we started from destination

def shortestPath(self, mat: list[list[int]], src: list[int], dest: list[int]) -> int:
    if mat[src[0]][src[1]] == 0 or mat[dest[0]][dest[1]] == 0:
        return -1
    
    if src==dest:
        return 0
    
    q=deque([(0,src[0],src[1])])
    dr=[-1,0,1,0]
    dc=[0,1,0,-1]
    n=len(mat)
    m=len(mat[0])

    # Initialize the distance matrix, marking all cells as unvisited initially
    dist = [[float('inf')] * m for _ in range(n)]
    dist[src[0]][src[1]] = 0

    while q:
        dis,r,c = q.popleft()

        for i in range(4):
            nr,nc=r+dr[i],c+dc[i]

            # Check if the new cell is within bounds and is a valid cell (i.e., 1)
            if 0 <= nr < n and 0 <= nc < m and mat[nr][nc] == 1 and dis + 1 < dist[nr][nc]:
                dist[nr][nc]=dis+1
                if [nr,nc]==dest:
                    return dis+1
                
                q.append((dis+1,nr,nc))

    return -1

def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    if grid[0][0] == 1 or grid[n - 1][m - 1] == 1:
        return -1
    
    if n == 1 and m == 1:
        return 1
    
    q=deque([(1,0,0)])
    grid[0][0]=1
    directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]
    n=len(grid)
    m=len(grid[0])

    while q:
        dis,r,c = q.popleft()

        for dr,dc in directions:
            nr,nc=r+dr,c+dc

            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 0:
                if nr == n - 1 and nc == m - 1:
                    return dis + 1
                
                grid[nr][nc]=1  #so i wont go back
                q.append((dis+1,nr,nc))

    return -1

def minimumEffortPath(self, heights: List[List[int]]) -> int:






