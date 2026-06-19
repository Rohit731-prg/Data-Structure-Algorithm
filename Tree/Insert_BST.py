# insertion and traversal of binary tree with preorder traversal method

from typing import Optional

class Node:
    def __init__(self, num) -> None:
        self.data = num
        self.prev: Optional['Node'] = None
        self.next: Optional['Node'] = None

    
class Tree:
    def __init__(self) -> None:
        self.head: Optional['Node'] = None


    def tree_insert(self, num):
        print("Inserting: ", num)
        new_node = Node(num)
        if self.head == None:
            self.head = new_node
            return
        
        temp: Node = self.head
        while True:
            if num < temp.data:
                if temp.prev == None:
                    temp.prev = new_node
                    return
                else:
                    temp = temp.prev
            elif num > temp.data:
                if temp.next == None:
                    temp.next = new_node
                    return
                else:
                    temp = temp.next

    
    def display(self):
        if self.head == None:
            print("Tree is empty.")
            return
        stack = [self.head]
        while stack:
            node = stack.pop()
            print(node.data, end=" ")

            if node.next != None:
                stack.append(node.next)

            if node.prev != None:
                stack.append(node.prev)
            
            


node_string = input("Enter the numbers to be inserted in the tree: ")
node_list = node_string.split(" ")
node_list = list(set(node_list))
tree = Tree()
for i in node_list:
    try:
        num = int(i)
        tree.tree_insert(num)
    except Exception as e:
        print("Invalid input, please enter only numbers.", e)
print("Tree created successfully.")
print("\n\t----------------Displaying the tree----------------\n")
tree.display()