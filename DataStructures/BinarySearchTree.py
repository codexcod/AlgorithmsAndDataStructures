class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def append(self, value):
        if value <= self.data:
            if self.left is None:
                self.left = Node(value)

            else:
                self.left.append(value)

        else:
            if self.right is None:
                self.right = Node(value)

            else:
                self.right.append(value)

    def contains(self, value):
        if value == self.data:
            return True

        elif value < self.data:
            if self.left is None:
                return False

            else:
                return self.left.contains(value)

        else:
            if self.right is None:
                return False

            else:
                return self.right.contains(value)

    def printInOrder(self):
        if not self.left is None:
            self.left.printInOrder()

        print(self.data)
        if not self.right is None:
            self.right.printInOrder()

    def printPreOrder(self):
        print(self.data)
        if not self.left is None:
            self.left.printInOrder()

        if not self.right is None:
            self.right.printInOrder()

    def printPostOrder(self):
        if not self.left is None:
            self.left.printInOrder()

        if not self.right is None:
            self.right.printInOrder()

        print(self.data)






binaryTree = Node(46)
binaryTree.append(60)
binaryTree.append(23)
binaryTree.append(42)
binaryTree.append(55)
binaryTree.append(15)
binaryTree.printInOrder()
print("--------")
binaryTree.printPreOrder()
print("--------")
binaryTree.printPostOrder()


