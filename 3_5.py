class MyQueue:
    def __init__(self):
        self.stacks = {1: None, 2: None}
    def enqueue(self, data):
        self.push(data, 2)
        self.moveStack(1,2)
        self.moveStack(2,1)
    def dequeue(self):
        self.moveStack(1,2)
        val = self.pop(2)
        self.moveStack(2,1)
        return val
    def moveStack(self, outS, inS):
        while self.stacks[outS] is not None:
            t_data = self.pop(outS)
            self.push(t_data, inS)
    def push(self, data, inS):
        from structures import Node
        if self.stacks[inS] is None:
            self.stacks[inS] = Node(data, None)
        else:
            top = Node(data, self.stacks[inS])
            self.stacks[inS] = top
    def pop(self, outS):
        if self.stacks[outS] is None:
            return None
        else:
            top = self.stacks[outS]
            self.stacks[outS] = top.next
            return top.data
        
q = MyQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print q.dequeue()
print q.dequeue()
print q.dequeue()
print q.dequeue()