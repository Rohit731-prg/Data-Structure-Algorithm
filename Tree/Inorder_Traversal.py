# search in binary tree with inorder traversal method

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
        
        temp: Node = self.head
        stack = [temp]

        while stack:
            node = stack.pop()
            print(node.data, end=" ")

            if node.next is not None:
                stack.append(node.next)
            
            if node.prev is not None:
                stack.append(node.prev)


    def search(self, num: int):
        if self.head is None:
            print("Tree is empty.")
            return 
        
        temp: Node = self.head
        stack = [temp]

        while True:
            if not stack:
                print(f"{num} not found in the tree.")
                return
            node = stack.pop()
            if node.data == num:
                print(f"Found: {num}")
                return
            
            if node.next is not None:
                stack.append(node.next)
            if node.prev is not None:
                stack.append(node.prev)


    def inorder_traversal(self, root: Optional[Node]):
        if root is None:
            return
        self.inorder_traversal(root.prev)
        print(root.data, end=" ")
        self.inorder_traversal(root.next)


tree = Tree()
for i in range(5):
    num = random.randint(11, 99)
    tree.insert(num)

print("\n\t------------------Display Tree------------------")
tree.display()

print("\n\t------------------Inorder Traversal------------------")
tree.inorder_traversal(tree.head)

print("\n\t------------------Search Tree------------------")
search_num = int(input("Enter the number to be searched: "))
tree.search(search_num)