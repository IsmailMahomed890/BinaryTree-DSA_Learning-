# Basic Binary Tree Structure

# Node class - represents each element in the tree
class Node:
    def __init__(self, data , left = None ,right = None):
        self.data = data    # Store the value
        self.left = left    # Left child node
        self.right = right  # Right child node

# Create the tree structure
#       1
#      / \
#     2   3
#    / \
#   4   5

root = Node(1)              # Root node
root.left = Node(2)         # Left child of root
root.right = Node(3)        # Right child of root
root.left.left = Node(4)    # Left child of node 2
root.left.right = Node(5)   # Right child of node 2

# Access and print node values
print(root.left.right.data)  # Prints 5
print(root.left.left.data)   # Prints 4
print(root.right.data)       # Prints 3

