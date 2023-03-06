class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        new_node = Node(data)

        # when the list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        # when the list is not empty
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def traverse_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def reverse(self):
        temp = None
        current = self.head
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        if temp is not None:
            self.head = temp.prev

    def reverse_recursive(self):
        def _reverse_recursive(current, prev):
            if not current:
                return prev
            next = current.next
            current.next = prev
            current.prev = next
            return _reverse_recursive(next, current)

        self.head = _reverse_recursive(self.head, None)

    def __str__(self):
        temp = self.head
        result = ""
        while temp:
            result += str(temp.data) + " "
            temp = temp.next
        return result

    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":

    dlist = DoublyLinkedList()
    dlist.insert(1)
    dlist.insert(2)
    dlist.insert(3)
    dlist.insert(4)
    dlist.insert(5)

    print(dlist)
