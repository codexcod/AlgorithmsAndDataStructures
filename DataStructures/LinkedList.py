class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        current = self.head
        while not current.next is None:
            current = current.next

        current.next = Node(data)

    def prepend(self,data):
        newHead = Node(data)
        newHead.next = self.head
        self.head = newHead

    def deleteWithValue(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while not current.next is None:
            if current.next.data == data:
                current.next = current.next.next
                return

            current = current.next

    def remove(self):
        head = self.head.data
        self.head = self.head.next
        return head


    def print(self):
        print("Linked List")
        print("Head : ", self.head.data)
        current = self.head
        while not current.next is None:
            print("--------")
            print(current.next.data)
            current = current.next


#linkedList = LinkedList()
#linkedList.append(67)
#linkedList.append(7)
#linkedList.append(3)
#linkedList.append(90)
#linkedList.print()
#linkedList.deleteWithValue(7)
#linkedList.print()
#linkedList.prepend(80)
#linkedList.print()