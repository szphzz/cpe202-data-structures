from queue_array import Queue


class TreeNode:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree:

    def __init__(self):
        # Returns empty BST
        self.root = None

    def is_empty(self):
        # returns True if tree is empty, else False
        return self.root == None

    def searchHelper(self, key, curr):
        if key == curr.key:
            return True
        elif curr.left != None and key < curr.key:
            return self.searchHelper(key, curr.left)
        elif curr.right != None and key > curr.key:
            return self.searchHelper(key, curr.right)
        else:
            return False

    def search(self, key):
        # returns True if key is in a node of the tree, else False
        if self.is_empty():
            return False
        return self.searchHelper(key, self.root)

    def insertHelper(self, key, data, curr):
        if key == curr.key:
            curr.data = data
        elif curr.left == None and key < curr.key:
            curr.left = TreeNode(key, data)
        elif curr.right == None and key > curr.key:
            curr.right = TreeNode(key, data)
        elif curr.left != None and key < curr.key:
            return self.insertHelper(key, data, curr.left)
        elif curr.right != None and key > curr.key:
            return self.insertHelper(key, data, curr.right)

    def insert(self, key, data=None):
        # inserts new node w/ key and data
        # If an item with the given key is already in the BST,
        # the data in the tree will be replaced with the new data
        if self.is_empty():
            self.root = TreeNode(key, data)
        else:
            self.insertHelper(key, data, self.root)

    def find_minHelper(self, curr):
        if curr.left is None:
            return (curr.key, curr.data)
        else:
            return self.find_minHelper(curr.left)

    def find_min(self):
        # returns a tuple with min key and data in the BST
        # returns None if the tree is empty
        if self.is_empty():
            return None
        return self.find_minHelper(self.root)

    def find_maxHelper(self, curr):
        if curr.right is None:
            return (curr.key, curr.data)
        else:
            return self.find_maxHelper(curr.right)

    def find_max(self):
        # returns a tuple with max key and data in the BST
        # returns None if the tree is empty
        if self.is_empty():
            return None
        return self.find_maxHelper(self.root)

    def tree_heightHelper(self, curr):
        if curr == None:
            return 0
        l = 1 + self.tree_heightHelper(curr.left)
        r = 1 + self.tree_heightHelper(curr.right)
        return max(l, r)

    def tree_height(self):  # return the height of the tree
        # returns None if tree is empty
        if self.is_empty():
            return None
        return self.tree_heightHelper(self.root) - 1

    def inorder_list(self):
        # return Python list of BST keys representing in-order traversal of BST
        # DON'T use a default list parameter
        if self.is_empty():
            return []

        def inorder_listHelper(curr, li):
            if curr:
                inorder_listHelper(curr.left, li)
                li.append(curr.key)
                inorder_listHelper(curr.right, li)

        a = []
        inorder_listHelper(self.root, a)
        return a

    def preorder_list(self):
        # return Python list of BST keys representing pre-order traversal of BST
        # DON'T use a default list parameter
        if self.is_empty():
            return []

        def preorder_listHelper(curr, li):
            if curr:
                li.append(curr.key)
                preorder_listHelper(curr.left, li)
                preorder_listHelper(curr.right, li)

        a = []
        preorder_listHelper(self.root, a)
        return a

    def level_order_list(self):  # return Python list of BST keys representing level-order traversal of BST
        # You MUST use your queue_array data structure from lab 3 to implement this method
        # DON'T attempt to use recursion
        q = Queue(25000)  # Don't change this!
        li = []
        if self.is_empty():
            return []
        q.enqueue(self.root)
        while not q.is_empty():
            parent = q.dequeue()
            li.append(parent.key)
            if parent.left is not None:
                q.enqueue(parent.left)
            if parent.right is not None:
                q.enqueue(parent.right)
        return li