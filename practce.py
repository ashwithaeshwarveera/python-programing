class Queue:
    def __init__(self):
        self.q = []
        self.front = -1
        
    def push(self,X):
        if self.front == -1 :
            self.front = 0
        self.q.append(X)
        
    def pop(self):
        if len(self.q) == 0:
            return -1
        x = self.q[self.front]
        self.front += 1
        if len(self.q) == self.front:
            self.front = -1
            self.q = []
        return 
        
    def getfront(self):
        if self.front == -1 :
            self.front = 0
        return self.front

        
    def size(self):
        if len(self.q) == 0:
            return -1
        return self.q[self.front]
        
    def display(self):
        print("elements in queue:",self.q[self.front:])
        
queue = Queue()
queue.push(2)
queue.push(5)
queue.push(6)
        
queue.display()
print(queue.getfront())
queue.pop()
queue.display()