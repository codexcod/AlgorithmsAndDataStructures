class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:

    def __init__(self):
        self.head = None
        self.tail = None


    def isEmpty(self):
        return self.head == None

    def peek(self):
        return self.head

    def add(self,data):
        node = Node(data)
        if not self.tail is None:
            self.tail.next = node

        self.tail = node
        if self.head is None:
            self.head = node

    def remove(self):
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None

        return data

    def print(self):
        print("Tail : ",self.tail.data)
        print("Head : ",self.head.data)
        if not self.head.next is None:
            print("Head Next : ", self.head.next.data)


queue = Queue()
queue.add(40)
queue.add(50)
queue.add(60)
queue.add(70)
queue.print()
queue.remove()
queue.print()
