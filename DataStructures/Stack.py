class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def peek(self):
        return self.top

    def push(self,data):
        node = Node(data)
        node.next = self.top
        self.top = node

    def pop(self):
        data = self.top.data
        self.top = self.top.next
        return data

    def print(self):
        current = self.top
        while not current is None:
            print(current.data)
            print("----------")
            current = current.next

        print("            ")








