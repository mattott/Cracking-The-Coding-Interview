class Stack(Node):
    def __init__(self):
        self.top = Node(None, None)
        self.min = {0:None}
        self.elem = 0
    def getMin(self):
        if self.elem == 0:
            return "Empty stack requested."
        return self.min[self.elem]
    def push(self, data):
        if data < self.min[self.data]:
            self.elem += 1
            self.min[self.elem] = data
        else:
            temp = self.getMin()
            self.elem += 1
            self.min[self.elem] = temp
        self.top = Node(data, self.top)
    def pop(self):
        self.elem -= 1
        temp = self.top
        self.top = self.top.next
        temp.next = None
        return temp.data

pie_stack = Stack()
pie_stack.push(1)
pie_stack.getMin()
