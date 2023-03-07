# stack implementation using a linked list.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        if self.top:
            data = self.top.data
            self.top = self.top.next
            self.size -= 1
            return data
        else:
            return None

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def print_stack(self):
        if self.top:
            node = self.top
            while node:
                print(node.data)
                node = node.next
        else:
            print("Stack is empty.")
