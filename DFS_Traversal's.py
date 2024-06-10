class nodeclass:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

node1 = nodeclass(10)
node1.left = nodeclass(20)   
node1.right = nodeclass(30)
node1.left.left = nodeclass(40)
node1.left.right = nodeclass(50)
node1.left.right.left = nodeclass(60)
node1.left.right.right = nodeclass(70)
node1.right.right = nodeclass(80) 


def inorder(root):

    if not root:
        return None
    
    inorder(root.left)
    print(root.value)
    inorder(root.right)


# inorder(node1) 

def preorder(root):

    if not root:
        return None
    
    print(root.value)
    preorder(root.left)
    preorder(root.right)

# preorder(node1) 


def postorder(root):

    if not root:
        return None
    
    postorder(root.left)
    postorder(root.right)
    print(root.value)

postorder(node1)         