# Define a node of the Binary Search Tree (BST)
class TreeNode:
    def __init__(self, key):
        self.key = key        # Value of the node
        self.left = None      # Left child
        self.right = None     # Right child

    def __str__(self):
        return str(self.key)

# Define the Binary Search Tree
class BinarySearchTree:
    def __init__(self):
        self.root = None  # Initially the tree is empty

    # Internal method to recursively insert a new key
    def _insert(self, node, key):
        if node is None:
            return TreeNode(key)  # Create new node if reached a leaf
        if key < node.key:
            node.left = self._insert(node.left, key)   # Insert to the left subtree
        elif key > node.key:
            node.right = self._insert(node.right, key) # Insert to the right subtree
        return node

    # Public method to insert a key into the BST
    def insert(self, key):
        self.root = self._insert(self.root, key)

    # Internal method to recursively search for a key
    def _search(self, node, key):
        if node is None or node.key == key:
            return node  # Found the key or reached a leaf
        if key < node.key:
            return self._search(node.left, key)
        elif key > node.key:
            return self._search(node.right, key)

    # Public method to search a key
    def search(self, key):
        return self._search(self.root, key)

    # Internal method to recursively delete a node with the given key
    def _delete(self, node, key):
        if node is None:
            return node  # Key not found

        # Navigate to the correct subtree
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Node with one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # Node with two children: get the inorder successor (smallest in right subtree)
            node.key = self._min_value(node.right)
            # Delete the inorder successor
            node.right = self._delete(node.right, node.key)
        return node

    # Public method to delete a key from the BST
    def delete(self, key):
        self.root = self._delete(self.root, key)

    # Helper method to find the minimum key in a subtree
    def _min_value(self, node):
        while node.left is not None:
            node = node.left
        return node.key

    # Internal method for inorder traversal (left-root-right)
    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)

    # Public method to get the inorder traversal result as a list
    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result


# Test the BinarySearchTree class
bst = BinarySearchTree()
nodes = [50, 30, 20, 40, 70, 60, 80]

# Insert nodes into BST
for node in nodes:
    bst.insert(node)

# Search for a key
print('Search for 80:', bst.search(80))  # Should return a TreeNode object

# Display inorder traversal (should print sorted values)
print("Inorder traversal:", bst.inorder_traversal())

# Delete a node and verify it's gone
bst.delete(40)
print("Search for 40:", bst.search(40))  # Should return None

