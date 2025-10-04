# Level-Order Traversal Implementation (BFS)
# Pattern: Level by level, left to right (🌊 Breadth-First Search)

import BinaryTree as BT  # Import our binary tree structure
from collections import deque

def levelOrderTraversal(root):
    """
    Level-order traversal visits nodes level by level:
    1. Visit all nodes at depth 0 (root)
    2. Visit all nodes at depth 1 (children of root)
    3. Visit all nodes at depth 2, and so on...
    
    This is useful for:
    - Finding shortest path in unweighted trees
    - Level-by-level processing
    - Tree serialization by levels
    """
    # Base case: if root is None, return
    if root is None:
        return 
    
    # Use a queue (FIFO) to store nodes to visit
    queue = deque([root])  # Initialize queue with root node
    
    while queue:
        current = queue.popleft()  # Dequeue the front node
        print(current.data, end=' ')  # Process the current node
        
        # Enqueue left child if it exists
        if current.left:
            queue.append(current.left)
        
        # Enqueue right child if it exists
        if current.right:
            queue.append(current.right)

# Use the tree from BinaryTree.py
#       1
#      / \
#     2   3           
#    / \
#   4   5   

root = BT.root
print("Level-order Traversal of the Binary Tree:")
levelOrderTraversal(root)
print()  # New line for clean output

# Expected Output: 1 2 3 4 5
# Explanation:
# Level 0: 1 (root)
# Level 1: 2, 3 (children of root)
# Level 2: 4, 5 (children of node 2)
# 
# 🌟 Key Insight: Uses queue (FIFO) unlike DFS traversals that use recursion stack (LIFO)