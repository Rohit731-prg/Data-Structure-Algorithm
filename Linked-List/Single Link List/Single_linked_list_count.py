class Node:
    def __init__(self, num: int) -> None:
        self.data = num
        self.next = None

    
class Linked_list:
    def __init__(self) -> None:
        self.head = None

    def insert_At_end(self, num: int):
        new_node = Node(num)
        if self.head == None:
            self.head = new_node

        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    def count_linked_list(self):
        count = 0
        if self.head == None:
            print("No node present in Linked List")
            return
        temp = self.head
        while temp != None:
            count += 1
            temp = temp.next

        print("Total Nodes: ", count)

    def display(self):
        if self.head == None:
            print("No records found")
            return
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next

Lt = Linked_list()
Lt.insert_At_end(10)
Lt.insert_At_end(50)
Lt.insert_At_end(30)
Lt.insert_At_end(40)
Lt.insert_At_end(50)

Lt.display()
print("\n\t------------------\n")
Lt.count_linked_list()