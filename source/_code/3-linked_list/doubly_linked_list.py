class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def print_list(self):
        tmp = self.head
        while tmp:
            print(tmp.data, end=" ")
            tmp = tmp.next
            if tmp:
                print(" <-> ", end=" ")
        print()

    def append(self, value):
        # O(1) if know tail
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, value):
        # O(1)
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def pop_first(self):
        # O(1)
        if self.head == None:
            return
        if self.head.next == None:
            self.head = None
            self.tail = None
            return

        temp = self.head
        self.head = self.head.next
        self.head.prev = None
        temp.next = None
        return temp

    def pop(self):
        # O(1)
        if self.head == None:
            return
        if self.head.next == None:
            self.head = None
            self.tail = None

        temp = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        temp.prev = None
        return temp


if __name__ == "__main__":

    dl = DoublyLinkedList()
    dl.append(1)
    dl.append(2)
    dl.append(3)
    dl.prepend(0)
    dl.prepend(-1)
    dl.print_list()

    dl.pop()
    dl.print_list()

    dl.pop_first()
    dl.print_list()
