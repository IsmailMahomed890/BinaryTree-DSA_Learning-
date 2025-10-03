# Post-Order Traversal Implementation
# Pattern: Left → Right → Root (🟡 Root comes LAST)

import BinaryTree as BT  # Import our binary tree structure

def postOrderTraversal(node):
    """
    Post-order traversal visits nodes in this order:
    1. Recursively traverse the left subtree  
    2. Recursively traverse the right subtree
    3. Process the current node (Root)
    
    This is useful for:
    - Deleting the tree (children before parent)
    - Evaluating postfix expressions
    - Calculating directory sizes
    """
    # Base case: if node is None, stop recursion
    if node is None:
        return
    
    # Step 1: Traverse LEFT subtree first
    postOrderTraversal(node.left)  
    
    # Step 2: Traverse RIGHT subtree next
    postOrderTraversal(node.right)
    
    # Step 3: Visit/Process the ROOT last
    print(node.data, end=' ')

# Use the tree from BinaryTree.py
#       1
#      / \
#     2   3
#    / \
#   4   5

root = BT.root
print("Post-order Traversal of the Binary Tree:")
postOrderTraversal(root)
print()  # New line for clean output

# Expected Output: 4 5 2 3 1
# Explanation:
# 4 (leftmost) → 5 (right of 2) → 2 (parent processed after children) → 3 (right child) → 1 (root last)
# 
# 🌟 Key Insight: Perfect for tree deletion - children are processed before their parent!