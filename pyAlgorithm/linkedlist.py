import sys
import random

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    
    # 연결리스트의 길이를 반환한다.
    def __len__(self):
        return self.length
    
    # head에 list 삽입
    def appendleft(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            node = Node(data)
            node.next = self.head
            self.head = node
        self.length += 1
    
    #마지막에 list 삽입
    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)
        self.length += 1

    #print
    def __str__(self):
        if self.head is None:
            return "Linked list is empty"
        res = "Head"
        node = self.head
        while node:
            res += " -> " + str(node.data)
            node = node.next
        return res

    #찾기
    def __contains__(self, target):
        if self.head is None:
            return False
        node = self.head
        while node:
            if node.data == target:
                return True
            node = node.next
        return False
    
    # head에 list 제거
    def popleft(self):
        node = self.head
        self.head = node.next
        #node.next = None
        self.length -= 1
        return node.data
    
    #마지막에 list 제거 
    def pop(self):
        node = self.head

        while node.next:
            prev = node
            node = prev.next
  
        if prev == self.head:
            self.head = None
        else:
            prev.next = None
        
        self.length -= 1
        return node.data
    
    #특정 원소 제거
    def remove(self,target):

        node = self.head

        while node and node.data != target:
            prev = node
            node = node.next
        if node is None:
            return False
        if node == self.head:
            self.head = self.head.next
        else:
            prev.next = node.next
        self.length -= 1
        return True

    #특정 위치에 데이터 삽입
    def insert(self,idx,data):
        if idx <= 0:
            self.appendleft(data)
        elif idx >= self.length:
            self.append(data)
        else:
            node = self.head
            for _ in range(idx-1):
                node = node.next
            new_node = Node(data)
            new_node.next = node.next
            node.next = new_node
            self.length += 1

    def reverse(self):
        prev = None
        node = self.head.next
        while node:
            self.head.next = prev
            prev = self.head
            self.head = node
            node = node.next
        self.head.next = prev


if __name__ == "__main__":
    my_list = LinkedList()
    data = list(range(10,20))
    random.shuffle(data)
   
    for i in data:
        my_list.append(i)
    print(my_list)

    my_list.reverse()
    print(my_list)  
    

          
