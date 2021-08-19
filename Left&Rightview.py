# Left view of Binary Tree
# Right view of Binary Tree


        
'''    
    
            4
            /\
        2       12
       /          \
     6             11
        \ 
         7
           \ 
             9

#leftview = 4 2 6 7 9
#Rightview = 4 12 11 7 9

'''  
#class Leftview of Binary Tree
# Recursive function to print left view of a binary tree.
# It takes a root, the current level, and 
# the max level so far of the binary tree

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Binarytree(Node):
    def __init__(self,*args):
        super(Binarytree).__init__()
    
    def leftviewuntil(self,root,level,max_level):
        if root is None:
            return
        
        if max_level[0] < level:
            print(root.data)
            max_level[0] = level
        
        self.leftviewuntil(root.left,level+1,max_level)
        self.leftviewuntil(root.right,level+1,max_level)
    
        
         
    
    def rightviewuntil(self,root,level,max_level):
        if root is None:
            return
        
        if max_level[0] < level:
            print(root.data)
            max_level[0] = level
        
        
        self.rightviewuntil(root.right,level+1,max_level) 
        self.rightviewuntil(root.left,level+1,max_level)
    
            
            
    def leftview(self,root):
        max_level = [0]
        print('Left View of Binary Tree')
        self.leftviewuntil(root,1,max_level)
    
    def rightview(self,root):
        max_level = [0]
        print('Left View of Binary Tree')
        self.rightviewuntil(root,1,max_level)
        
        
        
root = Node(4)
Bt = Binarytree()
root.left = Node(2)
root.right = Node(12)
root.right.right = Node(11)
root.left.left = Node(6)
root.left.left.right = Node(7)
root.left.left.right.right = Node(9)
Bt.leftview(root)
Bt.rightview(root)
