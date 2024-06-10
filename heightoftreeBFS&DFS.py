
from collections import deque
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

 


def DFS_Height(root):

    if not root:
        return 0
    
    else:
        lh = DFS_Height(root.left)
        rh = DFS_Height(root.right)

        return max(lh,rh) + 1
    
print(DFS_Height(node1))


def BFS_Height(root):

    queue = deque([root])
    height = 0 
    while queue:

        for i in range(len(queue)):
        
            node = queue.popleft()

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)    

        height += 1

    return height    

print(BFS_Height(node1))