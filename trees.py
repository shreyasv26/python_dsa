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
    





