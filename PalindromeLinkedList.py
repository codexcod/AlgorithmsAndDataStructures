from ReverseLinkedList import reverseLinkedList, LinkedList


# Palindrome significant capicua
def isPalindrome(head):
    fast = head
    slow = head

    while not fast is None and not fast.next is None:
        fast = fast.next.next
        slow = slow.next

    slow = reverseLinkedList(slow)
    fast = head

    while not slow is None:
        if slow.data != fast.data:
            return False

        slow = slow.next
        fast = fast.next

    return True


linkedList = LinkedList()
linkedList.append(1)
linkedList.append(2)
linkedList.append(4)
linkedList.append(4)
linkedList.append(2)
linkedList.append(1)
linkedList.print()
print(isPalindrome(linkedList.head))
