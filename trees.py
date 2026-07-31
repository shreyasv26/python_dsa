# | Tree Type  | Node Child Count      | Leaf Node Placement                  | Balanced?       | Height (h) given N nodes             |
# |------------|-----------------------|--------------------------------------|-----------------|--------------------------------------|
# | Full       | 0 or 2                | Can be at any level                  | Not necessarily | O(N) (worst case) to O(log N)        |
# | Perfect    | All internal have 2   | Must be at the exact same level      | Always          | Exactly O(log N)                     |
# | Complete   | 0, 1, or 2            | Last level packed from left to right | Always          | Exactly O(log N)                     |
# | Balanced   | 0, 1, or 2            | Can vary slightly                    | Always          | O(log N)                             |
# | Skewed     | Exactly 1 (except leaf)| Only one leaf at the very bottom    | Never           | Exactly O(N)                         |

# Height vs. Depth:

# Height: Distance from a node down to its furthest leaf.

# Depth: Distance from the root down to that node.

# list1.append([4, 5])   ->    [1, 2, 3, [4, 5]]
# list2.extend([4, 5])   ->    [1, 2, 3, 4, 5]

# 1. Preorder + Inorder → Unique tree

# Preorder: Root → Left → Right
# Inorder: Left → Root → Right

# Example:

# Preorder = [3, 9, 20, 15, 7]
# Inorder  = [9, 3, 15, 20, 7]

# Take the first preorder element as root:

# Root = 3

# Inorder:
# [9] 3 [15,20,7]
#  ↑       ↑
# left    right

#     3
#    / \
#   9   20
#      /  \
#     15   7

# 2. Postorder + Inorder → Unique tree

# Postorder: Left → Right → Root

# Now the last element of postorder is the root.

# Postorder = [9, 15, 7, 20, 3]
# Inorder   = [9, 3, 15, 20, 7]

# Root = 3.

# The important trick: because we're consuming postorder backwards, construct:


from collections import deque
from collections import defaultdict
from typing import Optional

# nodes_map = defaultdict(list)

# Key '3' doesn't exist yet, but this works perfectly:
# nodes_map[3].append(10)

# nodes_map = {}
# nodes_map[3].append(10)   this not posible bc it shows error

class Solution:
    def create_binary_tree(self):
        # Creates the root node with key value 1
        root = Node(1)       

        # Creates a left child node for the root with key value 2
        root.left = Node(2)       

        # Creates a right child node for the root with key value 3
        root.right = Node(3)      

        # Creates a left child node for the right child of root with key value 5
        root.right.left = Node(5) 

        return root
    
# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    res = []
        
    def dfs(node):
        if not node:
            return
        res.append(node.val)
        dfs(node.left)
        dfs(node.right)
            
    dfs(root)
    return res

def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    res=[]

    def dfs(node):
        if not node:
           return 
        dfs(node.left)
        res.append(node.val)
        dfs(node.right)

    dfs(root)
    return res

def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    res=[]

    def dfs(node):
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        res.append(node.val)

    dfs(root)
    return res

def allThreeTraversals(self, root: Optional[TreeNode]):
        preorder, inorder, postorder = [], [], []
        if not root:
            return preorder, inorder, postorder
        
        # Stack stores tuples: [node, state]
        # State 1 = Preorder, State 2 = Inorder, State 3 = Postorder
        stack = [[root, 1]]
        
        while stack:
            curr = stack[-1] # Look at the top of the stack
            node, state = curr[0], curr[1]
            
            # STATE 1: Preorder
            if state == 1:
                preorder.append(node.val)
                curr[1] += 1 # Move to state 2
                
                if node.left:
                    stack.append([node.left, 1]) # Push left child
                    
            # STATE 2: Inorder
            elif state == 2:
                inorder.append(node.val)
                curr[1] += 1 # Move to state 3
                
                if node.right:
                    stack.append([node.right, 1]) # Push right child
                    
            # STATE 3: Postorder
            elif state == 3:
                postorder.append(node.val)
                stack.pop() # Fully processed, remove from stack
                
        return preorder, inorder, postorder

def preorder2(self, root: Optional[TreeNode]) -> List[int]:
    # Logic: We use a stack to mimic recursion. Since a stack is Last-In, First-Out (LIFO), we push the right child first and then the left child. This ensures the left child is popped and processed before the right child.
    # root left right
    if not root:
        return []
    stack=[root]
    res=[]

    while stack:
        node=stack.pop()
        res.append(node.val)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        
    return res

def inorder2(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    
    stack = []
    res = []
    curr = root  # Initialize curr properly

    while stack or curr:
        # 1. Go down to the leftmost node of the current subtree
        while curr:
            stack.append(curr)  # Store the node object, not the val
            curr = curr.left    # Move left (not .next)
            
        # 2. Backtrack: curr is now None, so pop the parent node from stack
        curr = stack.pop()
        res.append(curr.val)    # Process the Root/Current node
        
        # 3. Move to the right subtree
        curr = curr.right
        
    return res

def postorder2(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    stack=[root]
    res=[]

    while stack:
        node=stack.pop()
        res.append(node.val)

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
        # Reversing Root -> Right -> Left gives Left -> Right -> Root (Postorder)
    return res[::-1]
    
def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    # breadth first search bfs
    q=deque([root])
    ans=[]

    if not root:
        return ans

    while q:
        level=[]
        for _ in range(len(q)):
            node=q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        ans.append(level)
    return ans

def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    
    lh=self.maxDepth(root.left)
    rh=self.maxDepth(root.right)

    return 1+max(lh,rh)

class Balance:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfsHeight(root) != -1

    def dfsHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        leftHeight = self.dfsHeight(root.left)
        if leftHeight == -1: 
            return -1
            
        rightHeight = self.dfsHeight(root.right)
        if rightHeight == -1: 
            return -1
        
        if abs(leftHeight - rightHeight) > 1: 
            return -1
            
        return max(leftHeight, rightHeight) + 1

class Diameter:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter=[0]
        self.dfs(root,diameter)
        return diameter[0]
    

    def dfs(self, root: Optional[TreeNode],diameter):
        if not root:
            return 0
        
        lh=self.dfs(root.left,diameter)
        rh=self.dfs(root.right,diameter)
        diameter[0]=max(diameter[0],lh+rh)

        return 1+max(lh,rh)

class MaxSumPath:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        msum = [float('-inf')]
        sum(root,msum)

        return msum[0]
        
    def sum(self, root: Optional[TreeNode],sum:List[int]):
        if not root:
            return 0
        
        lsum=max(0,self.sum(root.left,sum))
        rsum=max(0,self.sum(root.right,sum))

        sum[0]=max(sum[0],lsum+rsum+root.val)     
        return root.val+max(lsum,rsum) #for each node
    
def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool: 
    if not p and not q:    #if both r null
        return True
    if not p or not q:     #if anyone of em is null
        return False
    
    return (p.val==q.val) and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    #level order traversal
    q=deque([root])
    ans=[]

    if not root:
        return ans

    while q:
        level=[]
        for _ in range(len(q)):
            node=q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        ans.append(level)

    for i in range(1,len(ans),2):
        ans[i]=ans[i][::-1]

    return ans

    # q=deque([root])
    # ans=[]

    # if not root:
    #     return ans

    # left-right=True

    # while q:
    #     level=[]
    #     for _ in range(len(q)):
    #         node=q.popleft()
    #         level.append(node.val)
    #         if node.left:
    #             q.append(node.left)
    #         if node.right:
    #             q.append(node.right)

    #     if not left-right:
    #         ans.append(level[::-1])

    #     left-right=not left-right

    # return ans

class TraverseBoundary:
    def boundaryTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        res = []
        
        # If the root is not a leaf node, add it to the result
        if not self.isLeaf(root):
            res.append(root.val)
            
        # Step 1: Add Left Boundary (excluding leaves)
        self.addLeftBoundary(root.left, res)
        
        # Step 2: Add all Leaf Nodes
        self.addLeaves(root, res)
        
        # Step 3: Add Right Boundary (excluding leaves, in reverse order)
        self.addRightBoundary(root.right, res)
        
        return res

    def isLeaf(self, node: Optional[TreeNode]) -> bool:
        return node is not None and node.left is None and node.right is None

    def addLeftBoundary(self, node: Optional[TreeNode], res: List[int]):
        curr = node
        while curr:
            if not self.isLeaf(curr):
                res.append(curr.val)
            # Prioritize moving left. If left doesn't exist, move right.
            curr = curr.left if curr.left else curr.right

    def addLeaves(self, node: Optional[TreeNode], res: List[int]):
        if not node:
            return
        if self.isLeaf(node):
            res.append(node.val)
            return
        # Standard DFS to collect leaves from left to right
        self.addLeaves(node.left, res)
        self.addLeaves(node.right, res)

    def addRightBoundary(self, node: Optional[TreeNode], res: List[int]):
        curr = node
        temp = []
        while curr:
            if not self.isLeaf(curr):
                temp.append(curr.val)
            # Prioritize moving right. If right doesn't exist, move left.
            curr = curr.right if curr.right else curr.left
            
        # Reverse the right boundary to ensure counter-clockwise order
        res.extend(temp[::-1])

class verticalTrversal1:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        # Map to store: { col: [(row, node_val), (row, node_val), ...] }
        nodes_map = defaultdict(list)
        
        # Queue stores tuples of: (current_node, row, col)
        q = deque([(root, 0, 0)])
        
        while q:
            node, row, col = q.popleft()
            
            # Store the row and value at this column key
            nodes_map[col].append((row, node.val))
            
            # Process left and right children
            if node.left:
                q.append((node.left, row + 1, col - 1))
            if node.right:
                q.append((node.right, row + 1, col + 1))
                
        res = []
        
        # Sort by column keys from leftmost to rightmost
        for col in sorted(nodes_map.keys()):
            # Sort the pairs within the same column by row index first, 
            # and then by node value if row indices are identical
            column_nodes = sorted(nodes_map[col], key=lambda x: (x[0], x[1]))
            
            # Extract only the node values for the final result
            res.append([val for row, val in column_nodes])
            
        return res

class AnothersolnBetter:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Edge Case: If the tree is empty, return an empty list immediately
        if not root:
            return []
            
        nodes = []

        def dfs(node, row, col):
            if not node:
                return
            # Storing col first ensures Python's native sort handles column order first
            nodes.append((col, row, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)
        
        # Sorts by col, then by row, then by val automatically!
        nodes.sort()

        res = []
        prev_col = float('-inf')

        for col, row, val in nodes:
            # Whenever the column changes, start a brand-new sublist
            if col != prev_col:
                res.append([])
                prev_col = col
            # res[-1] targets the active/current column list we are filling
            res[-1].append(val)

        return res
     
def topView(self, root):
    if not root:
        return []
    
    # Map to store: { col: node_val }
    top_map = {}
    
    # Queue stores tuples of: (node, column)
    q = deque([(root, 0)])
    
    while q:
        node, col = q.popleft()
        
        # Only record the FIRST node that appears at this column
        if col not in top_map:
            top_map[col] = node.val
            
        if node.left:
            q.append((node.left, col - 1))
        if node.right:
            q.append((node.right, col + 1))
            
    # Sort by column index from leftmost to rightmost
    return [top_map[col] for col in sorted(top_map.keys())]

def bottomView(self, root):
    if not root:
        return []
    
    # Map to store: { col: node_val }
    bottom_map = {}
    
    # Queue stores tuples of: (node, column)
    q = deque([(root, 0)])
    
    while q:
        node, col = q.popleft()
        
        # ALWAYS update/overwrite the value at this column
        bottom_map[col] = node.val
            
        if node.left:
            q.append((node.left, col - 1))
        if node.right:
            q.append((node.right, col + 1))
            
    # Sort by column index from leftmost to rightmost
    return [bottom_map[col] for col in sorted(bottom_map.keys())]

class Symmertic:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return self.isMirror(root.left, root.right)

    def isMirror(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left and not right:
            return True
            
        if not left or not right or left.val != right.val:
            return False
            
        return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)

class SideView:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        self.dfs(root,0,res)
        return res

    def dfs(self, node: Optional[TreeNode],level:int, res:List[int]):
        if not node:
            return
        
        if level==len(res):    #firsttime reaching that level so add it
            res.append(node.val)
        
        self.dfs(node.right,level+1,res)   #priority right
        self.dfs(node.left,level+1,res)

class getPAth:
    # Function to find the path from root to a given node
    def getPath(self, root, arr, x):
        if root is None:
            return False

        arr.append(root.val)

        if root.val == x:
            return True

        # Recurse on left and right
        if self.getPath(root.left, arr, x) or self.getPath(root.right, arr, x):
            return True

        # Backtrack if not found
        arr.pop()
        return False

    # Function to return the final path list
    def solve(self, root, x):
        # Initialize result path
        arr = []

        # If tree is empty
        if root is None:
            return arr

        # Get path using helper
        self.getPath(root, arr, x)
        return arr

def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    # Base case
        if root is None or root == p or root == q:
            return root
        
        # Search in left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # Result
        if left is None:
            return right
        elif right is None:
            return left
        else: # Both left and right are not null, we found our result
            return root        
    
def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        ans = 0
        q = deque([(root, 0)])  # pair: (node, index)
        
        while q:
            size = len(q)
            mmin = q[0][1]      # minimum id at the current level
            first, last = 0, 0
            
            for i in range(size):
                node, curr_idx = q.popleft()
                cur_id = curr_idx - mmin  # make id start from 0 to prevent overflow
                
                if i == 0:
                    first = cur_id
                if i == size - 1:
                    last = cur_id
                
                if node.left:
                    q.append((node.left, cur_id * 2 + 1))
                if node.right:
                    q.append((node.right, cur_id * 2 + 2))
            
            ans = max(ans, last - first + 1)
            
        return ans

def checkTree(self, root: Optional[TreeNode]) -> bool:
    if not root:
        return False

    return root.val==root.left.val+root.right.val

class distanceK:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return []
        parent={}
        self.map_parent(root,parent)

        return self.bfsTarget(target,parent,k)


    def map_parent(self,root:TreeNode,parent:dict):
        # BSF
        q=deque()
        q.append(root)

        while q:
            node=q.popleft()

            if node.left:
                parent[node.left]=node
                q.append(node.left)

            if node.right:
                parent[node.right]=node
                q.append(node.right)

    def bfsTarget(self,target: TreeNode,parent:dict, k:int ):
        q=deque()
        visited=set()

        q.append(target)
        visited.add(target)

        curr_level=0

        while q:
            if curr_level==k:
                break

            for _ in range(len(q)):
                node=q.popleft()
                if node.left and node.left not in visited:     #left
                    visited.add(node.left)
                    q.append(node.left)

                if node.right and node.right not in visited:    #right
                    visited.add(node.right)
                    q.append(node.right)

                if node in parent and parent[node] not in visited:  #up
                    visited.add(parent[node])
                    q.append(parent[node])

            curr_level+=1

        return [node.val for node in q]

class timeToBurn:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        if root.left== None and root.right==None:
            return 0
        
        parent={}
        start_node = self.map_parent2(root,parent,start)

        return self.bfsStart(start_node ,parent)

    def map_parent2(self,root:TreeNode,parent:dict, start:int):
        # BSF
        q=deque()
        q.append(root)

        while q:
            node=q.popleft()

            if node.val==start:
                start_node=node

            if node.left:
                parent[node.left]=node
                q.append(node.left)

            if node.right:
                parent[node.right]=node
                q.append(node.right)

        return start_node

    def bfsStart(self,target: TreeNode,parent:dict ):
        q=deque()
        visited=set()

        q.append(target)
        visited.add(target)

        time=0

        while q:
            for _ in range(len(q)):
                node=q.popleft()
                if node.left and node.left not in visited:     #left
                    visited.add(node.left)
                    q.append(node.left)

                if node.right and node.right not in visited:    #right
                    visited.add(node.right)
                    q.append(node.right)

                if node in parent and parent[node] not in visited:  #up
                    visited.add(parent[node])
                    q.append(parent[node])

            if q:
                time+=1

        return time

class CountNodes:
    def countNodes(self, root):
        if not root:
            return 0
        
        lh = self.leftH(root)
        rh = self.rightH(root)
        
        # Replace (1 << lh) - 1 with exponentiation    
        if lh == rh:
            return (2 ** lh) - 1     #2^h-1 is height of complete BT
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def leftH(self,node) -> int:
        height=0

        while node:
            height+=1
            node=node.left

        return height

    def rightH(self,node) -> int:
        height=0

        while node:
            height+=1
            node=node.right

        return height

def buildTree(self, preorder, inorder):
        # Create a hashmap to store inorder indices
        in_map = {val: idx for idx, val in enumerate(inorder)}

        # Helper function to build tree recursively
        def build(preStart, preEnd, inStart, inEnd):
            if preStart > preEnd or inStart > inEnd:
                return None

            # Root from preorder
            root_val = preorder[preStart]
            root = TreeNode(root_val)

            # Find index in inorder
            inRoot = in_map[root_val]
            numsLeft = inRoot - inStart    #num of nodes on the left

            # Recurse on left and right
            root.left = build(preStart + 1, preStart + numsLeft, inStart, inRoot - 1)
            root.right = build(preStart + numsLeft + 1, preEnd, inRoot + 1, inEnd)

            return root

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)

def buildTree(self, inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        in_map = {inorder[i]: i for i in range(len(inorder))}

        def build(postStart, postEnd, inStart, inEnd):
            if postStart > postEnd or inStart > inEnd:
                return None

            root_val = postorder[postEnd]
            root = TreeNode(root_val)

            inRoot = in_map[root_val]
            numsLeft = inRoot - inStart

            root.left = build(postStart, postStart + numsLeft - 1, inStart, inRoot - 1)
            root.right = build(postStart + numsLeft, postEnd - 1, inRoot + 1, inEnd)

            return root

        return build(0, len(postorder) - 1, 0, len(inorder) - 1)


#Binary Search Tree (BST)  O(logN)   
#rightmost node is max n leftmost node is min

def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    curr= root

    while curr:
        if curr.val==val:
            return curr
        elif curr.val>val:
            curr=curr.left
        else:
            curr=curr.right

    return None

def ceilingBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    curr=root
    ceil=None

    while curr:
        if curr.val>val:
            ceil=curr
            curr=curr.left
        elif curr.val==val:
            return ceil
        else:
            curr=curr.right

    return ceil

def floorBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    curr=root
    floor=None

    while curr:
        if curr.val>val:
            curr=curr.left
        elif curr.val==val:
            return floor
        else:
            floor=curr
            curr=curr.right

    return floor

def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
        return TreeNode(val)

    curr=root
    prev=None
    while curr:
        if curr.val>val:
            prev=curr
            curr=curr.left
        else:
            prev=curr
            curr=curr.right

    if prev.val>val:
        prev.left=TreeNode(val)
    else:
        prev.right=TreeNode(val)

    return root

class DeleteNode:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val == key:
            return self.helper(root)
        
        curr = root
        while curr:
            if curr.val > key:
                if curr.left and curr.left.val == key:
                    curr.left = self.helper(curr.left)
                    break
                curr = curr.left
            else:
                if curr.right and curr.right.val == key:
                    curr.right = self.helper(curr.right)
                    break
                curr = curr.right
        
        return root

    def helper(self, node: TreeNode) -> Optional[TreeNode]:
        if not node.left:
            return node.right
        if not node.right:
            return node.left

        right_child = node.right
        last_right = self.find_last_right(node.left)
        last_right.right = right_child
        return node.left

    def find_last_right(self, node: TreeNode) -> TreeNode:
        while node.right:
            node = node.right
        return node

#  in-order traveral of BST gives sorted values which can be stored in array   O(NlogN)

def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    self.k=k
    self.ans=None


    def inorder(node):
        #  nonlocal k,ans  Tells Python to modify 'k' and 'ans' from the parent function scope
        if not node and self.ans is not None:
            return 
        
        inorder(root.left)

        self.k-=1
        if self.k==0:
            self.ans=node.val
            return
        
        inorder(node.right)

    inorder(root)
    return self.ans

def kthLargest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.ans = None

        def reverse_inorder(node):
            if not node or self.ans is not None:
                return

            reverse_inorder(node.right)

            self.k -= 1
            if self.k == 0:
                self.ans = node.val
                return

            reverse_inorder(node.left)

        reverse_inorder(root)
        return self.ans

class ValidBst:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return valid(root,min=float("-inf"),max=float("inf"))
        
    def valid(self,root: Optional[TreeNode], min,max):
        if not root:
            return True

        if not (min<root.val<max):
            return False
        
        return self.valid (root.left,min,root.val) and self.valid(root.right,root.val,max)

def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if root==None or p==root or q==root:
        return root

    curr=root
    while curr:
        if curr.val>p.val and curr.val>q.val:
            curr=curr.left
        elif curr.val<p.val and curr.val<q.val:
            curr=curr.right
        else:
            return curr

def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        self.i = 0

        def build(upper_bound=float("inf")):
            # Stop if all elements are processed or the current element exceeds upper bound
            if self.i == len(preorder) or preorder[self.i] > upper_bound:
                return None

            root = TreeNode(preorder[self.i])
            self.i += 1  # Advance the index pointer globally

            # Construct left subtree with upper bound = current node's value
            root.left = build(root.val)
            root.right = build(upper_bound)

            return root

        return build()

def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode | None':
    successor=None

    while root:
        if root.val<=p.val:
            root=root.right
        else:
            successor=root
            root=root.left

    return successor

def twosum(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()

        def dfs(node):
            if not node:
                return False

            # Check if complement exists
            if k - node.val in seen:
                return True

            seen.add(node.val)

            # Search left and right subtrees
            return dfs(node.left) or dfs(node.right)

        return dfs(root)

class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack=[]
        self.pushAll(root)
        
    def next(self) -> int:
        node=self.stack.pop()

        if node.right:
            self.pushAll(node.right)
        
        return node.val
        
    def hasNext(self) -> bool:
        return len(self.stack)>0

    def pushAll(self,node:Optional[TreeNode]):
        while node:
            self.stack.append(node)
            node=node.left

