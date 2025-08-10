class FrontMiddleBack:
    def __init__(self):
        self.q = []

    def pushFront(self, val):
        self.q.insert(0, val)

    def pushMiddle(self, val):
        mid = len(self.q) // 2
        self.q.insert(mid, val)

    def pushBack(self, val):
        self.q.append(val)

    def popFront(self):
        if not self.q:
            return -1
        return self.q.pop(0)

    def popMiddle(self):
        if not self.q:
            return -1
        mid = (len(self.q) - 1) // 2  
        return self.q.pop(mid)

    def popBack(self):
        if not self.q:
            return -1
        return self.q.pop()

queue = FrontMiddleBack()

queue.pushFront(9)    
queue.pushBack(8)     
queue.pushMiddle(7)   
queue.pushMiddle(5)   

print(queue.popFront())   
print(queue.popMiddle()) 
print(queue.popMiddle())  
print(queue.popBack())    
print(queue.popBack())  