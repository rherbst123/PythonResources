class Tree:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
    
def preOrderTraversal(node):
        if node is None:
            return 
        
        print(node.data, end=", ")
        preOrderTraversal(node.right)
        preOrderTraversal(node.left)



def inOrderTraversal(node):
     if node is None:
          return
     inOrderTraversal(node.right)
     print(node.data, end=", ")
     inOrderTraversal(node.left)

def postOrderTraversal(node):
     if node is None:
          return
     postOrderTraversal(node.left)
     postOrderTraversal(node.right)
     print(node.data, end=", ")

root = Tree("R")
nodeA = Tree("A")
nodeB = Tree("B")
nodeC = Tree("C")
nodeD = Tree("D")
nodeE = Tree("E")
nodeF = Tree("F")
nodeG = Tree("G")
nodeH = Tree("H")

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

nodeD.left = nodeH


#print(root.left.left.data)
#preOrderTraversal(root)
print("\n " + 50*"=" )
inOrderTraversal(root)
print("\n " + 50*"=" )
#postOrderTraversal(root)