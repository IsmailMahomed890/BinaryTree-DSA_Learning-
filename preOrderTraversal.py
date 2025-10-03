# Pre-Order Traversal Implementation
# Pattern: Root → Left → Right (🔵 Root comes FIRST)

import BinaryTree as BT  # Import our binary tree structure

def preOrderTraversal(node):
    """
    Pre-order traversal visits nodes in this order:
    1. Process the current node (Root)
    2. Recursively traverse the left subtree  
    3. Recursively traverse the right subtree
    
    This is useful for:
    - Creating a copy of the tree
    - Prefix expression evaluation
    - Tree serialization
    """
    # Base case: if node is None, stop recursion
    if node is None:
        return
    
    # Step 1: Visit/Process the ROOT first
    print(node.data, end=' ')  
    
    # Step 2: Traverse LEFT subtree
    preOrderTraversal(node.left)  
    
    # Step 3: Traverse RIGHT subtree
    preOrderTraversal(node.right)

# Use the tree from BinaryTree.py
#       1
#      / \
#     2   3
#    / \
#   4   5

root = BT.root
print("Pre-order Traversal of the Binary Tree:")
preOrderTraversal(root)  
print()  # New line for clean output

# Expected Output: 1 2 4 5 3
# Explanation:
# 1 (root) → 2 (left child) → 4 (leftmost) → 5 (right of 2) → 3 (right child of root)