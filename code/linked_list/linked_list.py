class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
            if temp:
                print('->', end=' ')
        print()

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value) -> None:
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


if __name__ == '__main__':

    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(3)
    linked_list.append(5)
    linked_list.append(7)
    linked_list.append(9)
    linked_list.prepend(0)
    linked_list.print_list()
