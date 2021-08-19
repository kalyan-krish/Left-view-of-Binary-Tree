# Left view of Binary Tree


        
'''    
    
            4
            /\
        2       12
       /          \
     6             11
        \ 
         7

#leftview = 4 2 6 7   

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
        
    def leftviewuntil(self,root,level,max_level):
        if root is None:
            return
        
        if max_level[0] < level:
            print(root.data)
            max_level[0] = level
        
        self.leftviewuntil(root.left,level+1,max_level)
        self.leftviewuntil(root.right,level+1,max_level)    
    
            
            
    def leftview(self,root):
        max_level = [0]
        self.leftviewuntil(root,1,max_level)
        
        
root = Node(4)
root.left = Node(2)
root.right = Node(12)
root.right.right = Node(11)
root.left.left = Node(6)
root.left.left.right = Node(7)
root.leftview(root)
