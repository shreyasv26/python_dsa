# | Tree Type  | Node Child Count      | Leaf Node Placement                  | Balanced?       | Height (h) given N nodes             |
# |------------|-----------------------|--------------------------------------|-----------------|--------------------------------------|
# | Full       | 0 or 2                | Can be at any level                  | Not necessarily | O(N) (worst case) to O(log N)        |
# | Perfect    | All internal have 2   | Must be at the exact same level      | Always          | Exactly O(log N)                     |
# | Complete   | 0, 1, or 2            | Last level packed from left to right | Always          | Exactly O(log N)                     |
# | Balanced   | 0, 1, or 2            | Can vary slightly                    | Always          | O(log N)                             |
# | Skewed     | Exactly 1 (except leaf)| Only one leaf at the very bottom    | Never           | Exactly O(N)                         |

from collections import deque
import re


class Node:
    def __init__(self, key):
        self.data = key       # Stores the value of the node
        self.left = None      # Reference to the left child node
        self.right = None     # Reference to the right child node

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
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

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
    # Logic: We move down the tree as far left as possible, pushing every node onto the stack along the way. When we hit a None (the end of the left path), we pop from the stack (the Root/Current node), process it, and then move to its right child.
    # left root right
    if not root:
        return []
    
    stack,res=[root],[]

    while stack or curr:
        curr=stack.pop()

        while curr:
            stack.append(curr.val)
            curr=curr.next
        
        res.append(curr.val)

        curr=curr.right

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
        sum = [float('-inf')]
        sum(root,sum)
        return sum[0]
        
    def sum(self, root: Optional[TreeNode],sum:List[int]):
        if not root:
            return 0
        
        lsum=max(0,self.sum(root.left,sum))
        rsum=max(0,self.sum(root.right,sum))

        sum[0]=max(sum[0],lsum+rsum+root.val)
        return root.val+max(lsum,rsum)
    
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




