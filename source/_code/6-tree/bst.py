class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):

        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True

        tmp_root = self.root

        while True:

            if new_node.value == tmp_root.value:
                return False

            elif new_node.value < tmp_root.value:

                if tmp_root.left is None:
                    tmp_root.left = new_node
                    return True
                tmp_root = tmp_root.left
            else:
                if tmp_root.right is None:
                    tmp_root.right = new_node
                    return True
                else:
                    tmp_root = tmp_root.right

    def search(self, value):

        tmp = self.root

        while tmp is not None:

            if value < tmp.value:
                tmp = tmp.left
            elif value > tmp.value:
                tmp = tmp.right

            else:
                return True
        return False

    def _r_search(self, current_root, value):

        if current_root == None:
            return False
        if value == current_root.value:
            return True

        if value < current_root.value:
            return self._r_search(current_root=current_root.left, value=value)
        if value > current_root.value:
            return self._r_search(current_root=current_root.right, value=value)

    def r_search(self, value):

        return self._r_search(self.root, value)

    def _r_insert(self, current_root, value):
        if current_root == None:
            return Node(value)

        if value < current_root.value:
            current_root.left = self._r_insert(
                current_root=current_root.left, value=value
            )
        if value > current_root.value:
            current_root.right = self._r_insert(
                current_root=current_root.right, value=value
            )
        if value == current_root.value:
            return current_root

    def r_insert(self, value):

        if self.root is None:
            self.root = Node(value)

        self._r_insert(self.root, value)


if __name__ == "__main__":

    bst = BinarySearchTree()

    for i in [8, 3, 10, 1]:
        bst.r_insert(i)

    print(bst.root)
    print(bst.root.left)
    print(bst.root.right)
