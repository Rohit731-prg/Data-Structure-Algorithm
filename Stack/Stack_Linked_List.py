class Node:
    def __init__(self, num) -> None:
        self.data = num
        self.next = None


class Stack_linked_list:
    def __init__(self) -> None:
        self.top = None
        self.head = None

    def push(self, num):
        new_node = Node(num)
        if self.head == None:
            self.head = new_node
        new_node.next = self.top # type: ignore
        self.top = new_node
        
    def pop(self):
        if self.top == None:
            print("Stack is empty")
            return
        temp = self.top
        self.top = self.top.next
        value = temp.data
        del temp
        return value

    def display(self):
        temp = self.head
        while temp != None:
            print("Data: ", temp.data)
            temp = temp.next


stack = Stack_linked_list()
stack.push(15)
stack.push(55)
stack.push(95)

stack.display()

print("Delete : ", stack.pop())
print("Delete : ", stack.pop())
print("Delete : ", stack.pop())