class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

root = Node(5)
root.left =Node(2)        
root.right = Node(4) 
root.left.right = Node(7) 

#preorder
class solution:
    def __init__(self):
        self.ans = []

    def preorder(self,root):
        #base case
        if root is None:
            return
        #recurssive case
        self.ans.append(root.data)
        self.preorder(root.left)  
        self.preorder(root.right) 
        
    def preordertraverse(self,root):
        self.ans = []
        self.preorder(root)
        return self.ans

#postorder
        
    def postorder(self,root):
        if root is None :
            return
        
        self.postorder(root.left)
        self.postorder(root.right) 
        self.ans.append(root.data)  
        
    def postordertraverse(self,root):
        self.ans = []
        self.postorder(root)
        return self.ans
    
    
#inorder 
    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        self.ans.append(root.data)  
        self.inorder(root.right) 
        
        
    def inordertraverse(self,root):
        self.ans = []
        self.inorder(root)
        return self.ans    
           
    
sol = solution() 
print(sol.preordertraverse(root))    
print(sol.postordertraverse(root))
print(sol.inordertraverse(root))

#inverse binary tree

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

root = Node(5)
root.left =Node(2)        
root.right = Node(4) 
root.left.right = Node(7) 
class solution:
    def __init__(self):
        self.ans = []
    
    def invertTree(self,root):
        if root is None:
            return None
        
        root.left ,root.right = root.right ,root.left
        
        self.invertTree(root.left)  
        self.invertTree(root.right) 
        
        return root
        
    def preorder(self,root):
        if root is None:
            return 
        
        self.ans.append(root.data)
        self.preorder(root.left)  
        self.preorder(root.right) 
    
    def preordertraverse(self,root):
        self.ans = []
        self.preorder(root)
        return self.ans
    
sol = solution()
print(sol.preordertraverse(root)) 

sol.invertTree(root)
print(sol.preordertraverse(root)) 
   
    
     


        
    
               
