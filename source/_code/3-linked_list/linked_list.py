class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def print_list(self):
        tmp = self.head
        while tmp:
            print(tmp.data, end=" ")
            tmp = tmp.next
            if tmp:
                print("-> ", end=" ")
        print()

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node


if __name__ == "__main__":

    linkedlist = LinkedList()
    linkedlist.append(1)
    linkedlist.append(2)
    linkedlist.append(3)

    linkedlist.print_list()
    linkedlist.prepend(0)
    linkedlist.print_list()
