# Iterative Pre-Order Traversal (Using Stack)
# Pattern: Root → Left → Right (🔵 No Recursion)

import BinaryTree as BT  # Import our binary tree structure

def iterativePreOrderTraversal(root):
    """
    Pre-order traversal using a stack instead of recursion.
    Same result as recursive version, but avoids function calls.
    """
    if root is None:
        return
    
    # Use a stack (LIFO) to store nodes to visit
    stack = [root]  # Initialize stack with root node
    
    while stack:
        current = stack.pop()  # Pop the top node
        print(current.data, end=' ')  # Process the current node
        
        # Push right child first (LIFO means left will be processed first)
        if current.right:
            stack.append(current.right)
        
        # Push left child second
        if current.left:
            stack.append(current.left)

# Use the tree from BinaryTree.py
#       1
#      / \
#     2   3
#    / \
#   4   5

root = BT.root
print("Iterative Pre-order Traversal:")
iterativePreOrderTraversal(root)
print()  # New line for clean output

# Expected Output: 1 2 4 5 3
# Key Insight: Stack (LIFO) replaces recursion calls