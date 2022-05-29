from DataStructures.LinkedList import LinkedList


def reverseLinkedList(head):
    prev = None

    while (not head is None):
        next = head.next
        head.next = prev
        prev = head
        head = next

    return prev


"""linkedList = LinkedList()
linkedList.append(1)
linkedList.append(2)
linkedList.append(3)
linkedList.append(4)
linkedList.append(5)
linkedList.print()
print("`+`+`+`+`+`+")
current = reverseLinkedList(linkedList.head)
print("Head : ", current.data)
while not current.next is None:
    print("--------")
    print(current.next.data)
    current = current.next"""

