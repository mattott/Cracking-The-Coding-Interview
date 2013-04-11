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