from DataStructures.Stack import Stack,Node
from DataStructures.Graph import GraphNode

def postOrder(root):
    stack = Stack()
    result = []

    if root is None:
        return result

    stack.push(root)
    while not stack.isEmpty():
        node = stack.po
