
class BinaryTree(object):

    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):

        if self.leftChild == None:
            self.leftChild = newNode
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):

        if self.rightChild == None:
            self.rightChild = newNode
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRight(self):
        return  self.rightChild

    def getLeft(self):
        return self.leftChild

    def setRootValue(self, obj):
        self.key = obj

    def getRootValue(self):
        return self.key


r = BinaryTree('a')

print(r.getRootValue())

r.insertLeft('b')
print(r.getLeft())