class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        temp = self.root
        while True:
            if data < temp.data:
                if temp.left is None:
                    temp.left = new_node
                    break
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    break
                temp = temp.right

    def search(self, data):
        temp = self.root
        while temp:
            if data == temp.data:
                return True
            elif data < temp.data:
                temp = temp.left
            else:
                temp = temp.right
        return False

    def traverse_inorder(self):
        def _traverse_inorder(node):
            if node is None:
                return
            _traverse_inorder(node.left)
            print(node.data, end=" ")
            _traverse_inorder(node.right)

        _traverse_inorder(self.root)
        print()

    def traverse_preorder(self):
        def _traverse_preorder(node):
            if node is None:
                return
            print(node.data, end=" ")
            _traverse_preorder(node.left)
            _traverse_preorder(node.right)

        _traverse_preorder(self.root)
        print()

    def traverse_postorder(self):
        def _traverse_postorder(node):
            if node is None:
                return
            _traverse_postorder(node.left)
            _traverse_postorder(node.right)
            print(node.data, end=" ")

        _traverse_postorder(self.root)
        print()

    def __str__(self):
        def _str(node):
            if node is None:
                return ""
            return str(node.data) + " " + _str(node.left) + _str(node.right)

        return _str(self.root)
