
class BinHeap:
    capacity = 10
    items = []

    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def getLeftChildIndex(self, index):
        return 2 * index + 1

    def getRightChildIndex(self, index):
        return 2 * index + 2

    def getParentIndex(self, index):
        return (index - 1) / 2

    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < self.currentSize

    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < self.currentSize

    def hasParent(self, index):
        return self.getParentIndex(index) > 0

    def leftChild(self, index):
        return self.items[self.getLeftChildIndex(index)]

    def rightChild(self,index):
        return self.items[self.getRightChildIndex(index)]

    def parent(self, index):
        return self.items[self.getParentIndex(index)]

    def swap(self, indexOne, indexTwo):
        temp = self.items[indexOne]
        self.items[indexOne] = self.items[indexTwo]
        self.items[indexTwo] = temp

    def peek(self):
        if self.currentSize == 0:
            return
        return self.items[0]

    def poll(self):
        if self.currentSize == 0:
            return

        item = self.items[0]
        self.items[0] = self.items[self.currentSize - 1]
        self.currentSize = self.currentSize - 1
        self.heapifyDown()
        return item

    def add(self, item):
        self.items[self.currentSize] = item
        self.currentSize = self.currentSize + 1
        self.heapifyUp()

    def heapifyUp(self):
        index = self.currentSize - 1

        while self.hasParent(index) && self.parent(index) > self.items[index]:
                self.swap(self.getParentIndex(index), index)
                index = self.getParentIndex(index)

    def heapifyDown(self):

        index = 0

        while self.hasLeftChild(index):
            smallerChildIndex = self.getLeftChildIndex(index)
            if self.hasRightChild(index) && self.rightChild(index) < self.leftChild(index):
                smallerChildIndex = self.hasRightChild(index)

            if self.items[index] < self.items[smallerChildIndex]
                break
            else:
                self.swap(index, smallerChildIndex)

            index = smallerChildIndex
        