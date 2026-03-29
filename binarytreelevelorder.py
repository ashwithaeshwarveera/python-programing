#levelorder
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

root = Node(5)
root.left =Node(2)        
root.right = Node(4) 
root.left.right = Node(7) 

class queue:
    def __init__(self):
        self.q =[]
        self.front = -1
    
    def  push(self,x):
        if self.front == -1 :
            self.front = 0
        self.q.append(x)
        
    def pop(self):
        if  len(self.q) == 0:
            return -1
        x = self.q[self.front] 
        self.front += 1
        if len(self.q) == self.front:
            self.front = -1
            self.q = []
        return x
        
    def getfront(self):
        if len(self.q) == 0:
            return -1
        return self.q[self.front]
        
    def size(self):
        if self.front == -1:
            return 0
        return len(self.q) - self.front   
 
class solution:
    def levelorder(self,root):
        self.ans = []
        if root is None:
            return -1
        q = queue()
        q.push(root)
        self.ans.append([root.data])
        
        
        while q.size() > 0:
            l = q.size()
            level = []
            for i in range (l):
                front = q.pop()
                if front.left != None :
                    q.push(front.left)
                    level.append(front.left.data)
                if front.right != None :
                    q.push(front.right)
                    level.append(front.right.data) 
                
            if len(level) > 0:
                self.ans.append(level)
    
        return self.ans                                     
                    
sol = solution() 
print(sol.levelorder(root))               
               