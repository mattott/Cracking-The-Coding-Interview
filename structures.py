#Stacks and Queues
class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next
class Stack:
    def __init__(self):
        self.top = None
    def push(self, data):
        top = Node(data, self.top)
        self.top = top
    def pop(self):
        if self.top is None:
            return None
        else:
            top = self.top
            self.top = top.next
            return top.data
class Queue:
    def __init__(self):
        self.first = None
        self.last = None
    def enqueue(self, data):
        if self.first is None:
            first = Node(data, self.last)
            self.first = self.last = first
        else:
            last = Node(data, None)
            self.last.next = last
            self.last = last
        
    def dequeue(self):
        first = self.first
        if self.last == self.first:
            self.first = self.last = None
        else:
            self.first = first.next
        if first is not None:
            return first.data
        else:
            return None 
        
#Trees   
class TNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None
    def lookup(self, node, target):
        if node is None:
            return False
        elif node.data == target:
            return True
        elif target < node.data:
            return lookup(node.left, target)
        else:
            return lookup(node.right, target)
    def insert(self, node, data):
        if node is None:
            return TNode(data)
        elif data <= node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)
        return node
    def insertSortedArray(self, node, arr):
        from math import floor
        mdpt = int(floor(len(arr) / 2))
        node = TNode(arr[mdpt])
        if len(arr) > 1:
            node.left = self.insertSortedArray(node.left, arr[:mdpt])
            if len(arr) > 2:
                node.right = self.insertSortedArray(node.right, arr[mdpt+1:])
        return node
    def size(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.size(node.left) + self.size(node.right)
    def maxDepth(self, node):
        if node is None:
            return -1
        else:
            leftDepth = self.maxDepth(node.left)
            rightDepth = self.maxDepth(node.right)
            if leftDepth > rightDepth:
                return 1 + leftDepth
            else:
                return 1 + rightDepth
    def isBalanced(self, node):
        leftDepth = self.maxDepth(node.left)
        rightDepth = self.maxDepth(node.right)
        from math import fabs
        if fabs(leftDepth - rightDepth) > 1:
            return False
        else:
            return True
    def minValue(self, node):
        if node is None:
            return None
        while node.left is not None:
            node = node.left
        return node.data
    def maxValue(self, node):
        if node is None:
            return None
        while node.right is not None:
            node = node.right
        return node.data
    def printTree(self, node):
        if node is not None:
            self.printTree(node.left)
            print node.data
            self.printTree(node.right)
    def printPostorder(self, node):
        pass
    def build123(self):
        self.root = TNode(2)
        self.root.left = TNode(1)
        self.root.right = TNode(3)
    def build123alt(self):
        self.root = self.insert(self.root, 2)
        self.insert(self.root, 3)
        self.insert(self.root, 1)
bst = BST()
arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
bst.root = bst.insertSortedArray(bst.root, arr)
print bst.isBalanced(bst.root)
bst.printTree(bst.root)
print bst.maxDepth(bst.root)
        