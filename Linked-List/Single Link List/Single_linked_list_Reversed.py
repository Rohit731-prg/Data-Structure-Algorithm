class Node:
    def __init__(self, data, next = None) -> None:
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_At_begain(self, num):
        node = Node(num)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node


    def reverse_linked_list(self):
        if self.head == None:
            print("List is empty")
            return
        prev = save = None
        temp = self.head

        while temp != None:
            save = temp.next
            temp.next = prev
            prev = temp
            temp = save

        self.head = prev

    def display_linked_list(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next



ll = LinkedList()
ll.insert_At_begain(10)
ll.insert_At_begain(20)
ll.insert_At_begain(40)
ll.insert_At_begain(60)
ll.insert_At_begain(70)

print("\n\t----------------------Original Linked List----------------------\n")
ll.display_linked_list()

print("\n\t----------------------Reverse Linked List----------------------\n")
ll.reverse_linked_list()
ll.display_linked_list()