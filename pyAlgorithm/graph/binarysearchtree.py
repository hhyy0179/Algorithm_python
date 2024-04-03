class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None 
        
class BST:
    def __init__(self,root):
        self.root = root

    def search(self,value):
        current_node = self.root

        while current_node:
            if current_node.value == value:
                return True
            if value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False
    
    def insert(self,value):
        current_node = self.root
        
        while True:
            if value < current_node.value:
                if current_node.left == None:
                    current_node.left = Node(value)
                    break
                else:
                    current_node = current_node.left
            else:
                if current_node.right == None:
                    current_node.right = Node(value)
                    break
                else:
                    current_node = current_node.right

    def delete(self,value):
        parent_node = self.root
        current_node = self.root
       
        if self.search(value):
            #current_node 위치와 parent_node 위치를 고정.
            while current_node:
                if current_node.value == value:
                    break

                parent_node = current_node

                if parent_node.value < value:
                    current_node = parent_node.right
                else:
                    current_node = parent_node.left
            
            #자식을 가지고 있지 않은 노드
            if not current_node.left and not current_node.right:
                
                if parent_node.value < value:
                    parent_node.right = None
                else:
                    parent_node.left = None
                return

            #자식을 한개 가지고 있는 노드
            if not current_node.left or not current_node.right:
                
                #current_node가 parent의 오른쪽일 때
                if parent_node.value < value:
                    #current_node의 child가 오른쪽일 때,
                    if current_node.left == None: 
                        parent_node.right = current_node.right
                    #current_node의 child가 왼쪽일 때,
                    else:
                        parent_node.right = current_node.left
                        current_node.left = None
                #current_node가 parent의 왼쪽일 때
                else:
                    #current의 child가 오른쪽일 때,
                    if current_node.left == None:
                        parent_node.left = current_node.right
                    #current의 child가 왼쪽일 때,
                    else:
                        parent_node.left = current_node.left
            
                return
            
            #자식을 두개 가지고 있는 노드
            if current_node.left and current_node.right:
                #최소값을 찾는 부모노드, 현재 노드 설정 (초기값은 현재의 우측노드)
                minimum_parent_node = current_node.right
                minimum_node = minimum_parent_node

                #우측 노드의 최소값 찾기
                while minimum_node.left:
                    minimum_parent_node = minimum_node
                    minimum_node = minimum_node.left
                
                #최소값의 우측 노드가 존재한다면,
                if minimum_node.right:
                    minimum_parent_node.left = minimum_node.right  
                else:
                    minimum_parent_node.left = None

                #current_node가 parent의 오른쪽일 때
                if parent_node.value < value:
                    #parent_node와 minmum을 연결
                    parent_node.right = minimum_node
                else:
                    parent_node.left = minimum_node
                
                minimum_node.left = current_node.left
                minimum_node.right = current_node.right
    
                del(current_node)

    def pre_order_traverse(self,node):
        if not node:
            return
        print(node.value, end = ' ')
        self.pre_order_traverse(node.left)
        self.pre_order_traverse(node.right)

                           

root = Node(8)
bst = BST(root)
bst.insert(2)
bst.insert(7)
bst.insert(1)
bst.insert(14)
bst.insert(3)
bst.insert(9)
bst.insert(18)
bst.insert(10)
bst.delete(2)
bst.pre_order_traverse(root) #dfs
 