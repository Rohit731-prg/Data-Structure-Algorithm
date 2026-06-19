# search in binary tree with preorder traversal method

from typing import Optional
import random

class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.prev: Optional['Node'] = None
        self.next: Optional['Node'] = None


class Tree:
    def __init__(self) -> None:
        self.head: Optional[Node] = None


    def insert(self, num: int):
        print("Inserting: ", num)
        newNode = Node(num)
        if self.head is None:
            self.head = newNode
            return
        
        temp: Node = self.head
        while True:
            if num < temp.data:
                if temp.prev is None:
                    temp.prev = newNode
                    return    
                temp = temp.prev
            
            else:
                if temp.next is None:
                    temp.next = newNode
                    return
                temp = temp.next

    def display(self):
        if self.head is None:
            print("Tree is empty.")
            return
        
        stack1 = [self.head]
        stack2 = []

        while stack1:
            node = stack1.pop()
            stack2.append(node)

            if node.prev is not None:
                stack1.append(node.prev)
            if node.next is not None:
                stack1.append(node.next)

        while stack2:
            node = stack2.pop()
            print(node.data, end=" ")
        

    def postorder_traversal(self, root: Optional[Node]):
        if root is None:
            return
        self.postorder_traversal(root.prev)
        self.postorder_traversal(root.next)
        print(root.data, end=" ")


    def search(self, num: int):
        if self.head is None:
            print("Tree is empty.")
            return 
        
        stack = [self.head]
        while stack:
            node = stack.pop()
            if node.data == num:
                print("Number found: ", num)
                return
            
            if node.prev is not None:
                stack.append(node.prev)
            if node.next is not None:
                stack.append(node.next)
        
        print(f"{num} not found in the tree.")
        return


tree = Tree()
for i in range(5):
    num = random.randint(11, 99)
    tree.insert(num)

print("\n\t------------------Display Tree------------------")
tree.display()


print("\n\t------------------Postorder Traversal------------------")
tree.postorder_traversal(tree.head)

print("\n\t------------------Search Tree------------------")
search_num = int(input("Enter the number to be searched: "))
tree.search(search_num)