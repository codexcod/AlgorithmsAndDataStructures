class MinIntHeap:

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.items = []

        for i in range(self.capacity):
            self.items.append(None)

    def getLeftChildIndex(self, parentIndex): return 2 * parentIndex + 1
    def getRightChildIndex(self, parentIndex): return 2 * parentIndex + 2
    def getParentIndex(self, childIndex): return (childIndex - 1) // 2

    def hasLeftChild(self, index): return self.getLeftChildIndex(index) < self.size
    def hasRightChild(self, index): return self.getRightChildIndex(index) < self.size
    def hasParent(self, index): return self.getParentIndex(index) >= 0

    def leftChild(self, index): return self.items[self.getLeftChildIndex(index)]
    def rightChild(self, index): return self.items[self.getRightChildIndex(index)]
    def parent(self, index): return self.items[self.getParentIndex(index)]

    def swap(self,indexOne,indexTwo):
        temp = self.items[indexOne]
        self.items[indexOne] = self.items[indexTwo]
        self.items[indexTwo] = temp

    def ensureExtraCapacity(self):
        if self.size == self.capacity:
            for i in range(self.capacity):
                self.items.append(None)

            self.capacity += self.capacity

    def peek(self):
        if self.size == 0:
            raise Exception("size == 0")

        return self.items

    def poll(self):
        if self.size == 0:
            raise Exception("size == 0")

        item = self.items[0]
        self.items[0] = self.items[self.size - 1]
        self.size -= 1
        self.heapifyDown()
        return item

    def add(self,item):
        self.ensureExtraCapacity()
        self.items[self.size] = item
        self.size += 1
        self.heapifyUp()

    def heapifyUp(self):
        index = self.size - 1
        while self.hasParent(index) and self.parent(index) > self.items[index]:
            self.swap(self.getParentIndex(index),index)
            index = self.getParentIndex(index)

    def heapifyDown(self):
        index = 0
        while(self.hasLeftChild(index)):
            smallChildIndex = self.getLeftChildIndex(index)
            if self.hasLeftChild(index) and self.rightChild(index) < self.leftChild(index):
                smallChildIndex = self.getRightChildIndex(index)

            if self.items[index] < self.items[smallChildIndex]:
                break

            else:
                self.swap(index,smallChildIndex)

            index = smallChildIndex


heap = MinIntHeap(10)
heap.add(20)
heap.add(10)
heap.add(70)
heap.add(5)
heap.add(25)
heap.add(85)
heap.add(22)
heap.add(7)
heap.add(2)



print(heap.items)






