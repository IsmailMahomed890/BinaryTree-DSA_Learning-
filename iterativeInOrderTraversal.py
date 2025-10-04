# Iterative In-Order Traversal (Using Stack)
# Pattern: Left → Root → Right (🟢 No Recursion)

import BinaryTree as BT  # Import our binary tree structure

def iterativeInOrderTraversal(root):
    """
    In-order traversal using a stack instead of recursion.
    Returns a list containing the traversal result.
    """
    if root is None:
        return []
    
    res = []  # Result list to store the traversal
    stack = []  # Stack to keep track of nodes
    current = root  # Start with the root node
    
    while stack or current:
        # Go to the leftmost node of the current node
        while current:
            stack.append(current)  # Push current node to stack
            current = current.left  # Move to left child
        
        # Current must be None here, so we backtrack
        current = stack.pop()  # Pop from stack
        res.append(current.data)  # Store the node data in result
        
        # We have visited the node and its left subtree, now visit right subtree
        current = current.right
    
    return res

# Use the tree from BinaryTree.py
#       1
#      / \
#     2   3
#    / \
#   4   5

root = BT.root
print("Iterative In-order Traversal:")
result = iterativeInOrderTraversal(root)
print(result)

# Expected Output: [4, 2, 5, 1, 3]
# Key Insight: Stack helps us remember nodes while going left, then process them in order