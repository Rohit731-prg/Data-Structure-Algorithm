class Node:
    def __init__(self, num) -> None:
        self.data = num
        self.next = None

class Linked_list:
    def __init__(self) -> None:
        self.head = None
    
    def Insert_At_end(self, num):
        new_node = Node(num)
        if self.head == None:
            self.head = new_node
            new_node.next = self.head # type: ignore
            return
        
        temp = self.head
        while temp.next != self.head: # type: ignore
            temp = temp.next # type: ignore

        temp.next = new_node # type: ignore
        new_node.next = self.head # type: ignore


    def Insert_At_begin(self, num):
        new_node = Node(num)
        if self.head == None:
            self.head = new_node
            new_node.next = self.head # type: ignore
            return

        temp = self.head
        while temp.next != self.head: # type: ignore
            temp = temp.next # type: ignore
        temp.next = new_node # type: ignore
        new_node.next = self.head # type: ignore
        self.head = new_node


    def display(self):
        if self.head == None:
            print("Empty Linked List..!")
            return
        temp = self.head
        while True: # type: ignore
            print("Node: ", temp.data) # type: ignore
            temp = temp.next # type: ignore
            if temp == self.head: # type: ignore
                break

ll = Linked_list()
ll.Insert_At_end(10)
ll.Insert_At_end(30)
ll.Insert_At_end(20)
ll.Insert_At_end(60)
print("\n\t-----------------Display-----------------\n")
ll.display()

ll.Insert_At_begin(80)
ll.Insert_At_begin(25)
print("\n\t-----------------Display-----------------\n")
ll.display()

