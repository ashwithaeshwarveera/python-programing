class Queue:
    def __init__(self):
        self.q = []
        self.front = -1
        
    def push(self,X):
        if self.front == -1 :
            self.front = 0
        self.q.append(X)
        
    def pop(self,X):
        if len(self.q) == 0:
            return -1
        x = self.q[self.front]
        self.front += 1
        if len(self.q) == self.front:
            self.front = -1
            self.q = []
        return X
        
    def getfront(self):
        if len(self.q) == 0:
            return -1
        return self.q[self.front]
        
    def size(self):
        if self.front == -1:
            return 0
        return len(self.q) - self.front
        
    def display(self):
        print("elements in queue:",self.q[self.front:])
        
queue = Queue()
queue.push(2)
queue.push(5)
queue.push(6)
        
queue.display()


#queue using linked list
class Node :
    def __init__(self,data):
        self.data = data
        self.next = None
        
class queue :
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0
        
    def push(self,x):
        newnode = Node(x)
        self.length += 1
        if self.front is None :
            self.front = newnode
            self.rear = newnode
        else:
            self.rear.next = newnode
            self.rear = newnode
        return x
    
    def pop(self):
        if self.front == None :
            return -1
        self.length -= 1   
        x = self.front.data
        self.front = self.front.next
        if self.front is None :
            self.rear = None
        return x
        
           
    def getfront(self):
           if self.front is None:
               return -1
           return self.front.data
           
    def getsize(self):
           return self.length
           
           
    def display(self):
           curr = self.front
           print("elements in queue:",end = " ")
           while curr != None:
               print(curr.data,end = " ")
               curr = curr.next
           print()
     
q = queue( )

q.push(5)
q.push(4)
q.push(3)
q.push(1)               
                                      
q.display()

            
q.pop()
q.display()