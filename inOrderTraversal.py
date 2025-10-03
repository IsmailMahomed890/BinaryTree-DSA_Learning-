# In-Order Traversal Implementation  
# Pattern: Left → Root → Right (🟢 Root in the MIDDLE)

import BinaryTree as BT  # Import our binary tree structure

def inOrderTraversal(node):
    """
    In-order traversal visits nodes in this order:
    1. Recursively traverse the left subtree  
    2. Process the current node (Root)
    3. Recursively traverse the right subtree
    
    This is useful for:
    - Retrieving data in sorted order (for BSTs)
    - Expression tree evaluations
    - Getting elements in ascending order
    """
    # Base case: if node is None, stop recursion
    if node is None:
        return
    
    # Step 1: Traverse LEFT subtree first
    inOrderTraversal(node.left)  
    
    # Step 2: Visit/Process the ROOT (middle)
    print(node.data, end=' ')  
    
    # Step 3: Traverse RIGHT subtree last
    inOrderTraversal(node.right)

# Use the tree from BinaryTree.py
#       1
#      / \
#     2   3
#    / \
#   4   5

root = BT.root
print("In-order Traversal of the Binary Tree:")
inOrderTraversal(root)
print()  # New line for clean output

# Expected Output: 4 2 5 1 3
# Explanation:
# 4 (leftmost) → 2 (parent of 4) → 5 (right of 2) → 1 (root) → 3 (right child of root)
# 
# 🌟 Key Insight: For Binary Search Trees (BSTs), in-order traversal 
# gives you all values in ascending sorted order!
