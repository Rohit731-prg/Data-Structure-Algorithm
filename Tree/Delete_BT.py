class Node:
    def __init__(self, num) -> None:
        self.data = num
        self.left = None
        self.right = None


class Tree:
    def __init__(self) -> None:
        self.head = None

    def insert(self, num):
        print("Inserting: ", num)
        new_node = Node(num)
        if self.head == None:
            self.head = new_node
            return
        
        temp: Node = self.head
        while True:
            if num < temp.data:
                if temp.left == None:
                    temp.left = new_node # type: ignore
                    return
                else:
                    temp = temp.left
            elif num > temp.data:
                if temp.right == None:
                    temp.right = new_node # type: ignore
                    return
                else:
                    temp = temp.right

    def display(self):
        if self.head == None:
            print("Tree is empty.")
            return
        stack = [self.head]
        while stack:
            node = stack.pop()
            print(node.data, end=" ")

            if node.right != None:
                stack.append(node.right)

            if node.left != None:
                stack.append(node.left)


    def min_val_Node(self, node):
        current = node
        while current.left != None:
            current = current.left
        return current
    

    def delete(self, root, num):
        if root == None:
            return None

        if num < root.data:
            root.left = self.delete(root.left, num)

        elif num > root.data:
            root.right = self.delete(root.right, num)

        else:
            if root.left == None:
                return root.right
            if root.right == None:
                return root.left
            
            temp = self.min_val_Node(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data) # type: ignore
        return root
    

node_string = input("Enter the numbers to be inserted in the tree: ")
node_list = node_string.split(" ")
node_list = list(set(node_list))
tree = Tree()
for i in node_list:
    try:
        num = int(i)
        tree.insert(num)
    except Exception as e:
        print("Invalid input, please enter only numbers.", e)
print("Tree created successfully.")
print("\n\t----------------Displaying the tree----------------\n")
tree.display()
print("\n\n\t----------------Deleting from the tree----------------\n")
print("\nBefore deletion:")
tree.display()

tree.head = tree.delete(tree.head, 75)

print("\nAfter deletion:")
tree.display()