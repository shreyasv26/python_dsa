# | Tree Type  | Node Child Count      | Leaf Node Placement                  | Balanced?       | Height (h) given N nodes             |
# |------------|-----------------------|--------------------------------------|-----------------|--------------------------------------|
# | Full       | 0 or 2                | Can be at any level                  | Not necessarily | O(N) (worst case) to O(log N)        |
# | Perfect    | All internal have 2   | Must be at the exact same level      | Always          | Exactly O(log N)                     |
# | Complete   | 0, 1, or 2            | Last level packed from left to right | Always          | Exactly O(log N)                     |
# | Balanced   | 0, 1, or 2            | Can vary slightly                    | Always          | O(log N)                             |
# | Skewed     | Exactly 1 (except leaf)| Only one leaf at the very bottom    | Never           | Exactly O(N)                         |

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
        

