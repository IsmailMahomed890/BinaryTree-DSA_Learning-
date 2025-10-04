# Level-Order Traversal with Grouped Levels
# Output: [[level0], [level1], [level2], ...]

import BinaryTree as BT
from collections import deque

def levelOrderTraversalGrouped(root):
    """
    Level-order traversal that groups nodes by their levels.
    Returns a 2D list where each inner list contains nodes at the same level.
    
    Example output: [[1], [2, 3], [4, 5]]
    """
    if root is None:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)  # Number of nodes at current level
        current_level = []
        
        # Process all nodes at the current level
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.data)
            
            # Add children for next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result

# Use the tree from BinaryTree.py
#       1
#      / \
#     2   3           
#    / \
#   4   5   

root = BT.root
print("Level-order Traversal (Grouped by levels):")
levels = levelOrderTraversalGrouped(root)
print(levels)

# Expected Output: [[1], [2, 3], [4, 5]]
# Explanation:
# Level 0: [1] - just the root
# Level 1: [2, 3] - children of root
# Level 2: [4, 5] - children of node 2