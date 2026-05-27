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


    def delete_At_end(self):
        if self.head == None:
            print("Linked list underflow")
            return

        if self.head.next == self.head:
            value = self.head.data
            temp = self.head
            self.head = None
            del temp
            return value
        
        temp = prev = self.head
        while temp.next != self.head: # type: ignore
            prev = temp
            temp = temp.next # type: ignore

        value = temp.data # type: ignore
        del temp
        prev.next = self.head # type: ignore
        return value
    

    def delete_At_begin(self):
        if self.head == None:
            print("Linked list is empty")
            return 
        
        if self.head.next == self.head:
            value = self.head.data
            temp = self.head
            self.head = None
            del temp
            return value
        
        temp = self.head
        while temp.next != self.head: # type: ignore
            temp = temp.next # type: ignore
        
        temp.next = self.head.next # type: ignore
        temp = self.head
        self.head = self.head.next
        value = temp.data
        del temp
        return value


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

print("Delete from end: ", ll.delete_At_end())
print("Delete from end: ", ll.delete_At_end())
print("\n\t-----------------Display-----------------\n")
ll.display()

print("Delete from Begin: ", ll.delete_At_begin())
print("Delete from Begin: ", ll.delete_At_begin())
print("\n\t-----------------Display-----------------\n")
ll.display()