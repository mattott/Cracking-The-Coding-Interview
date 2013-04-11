class SortStack:
    def __init__(self, args):
        from structures import Stack
        self.unsorted = Stack()
        for i in range(len(args)):
            self.unsorted.push(args[i])
        self.sorted = Stack()
    def sort(self):
        while self.unsorted.top is not None:
            cur = self.unsorted.pop()
            self.move(cur)
    def move(self, cur):
        max = self.sorted.top
        if max is None or cur >= max.data:
            self.sorted.push(cur)
        else:
            self.unsorted.push(self.sorted.pop())
            self.move(cur)
            self.sorted.push(self.unsorted.pop())

ss = SortStack([3,6,7,4,2,1,5,122,3,213,23,5,77])
ss.sort()
while ss.sorted.top is not None:
    print ss.sorted.pop()
            