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
        
    def display_linked_list(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next

    def search_linked_list(self, num):
        temp = self.head
        while temp != None:
            if temp.data == num:
                print("Data is present in linked list..!")
                print("Element Address is: ", temp)
            temp = temp.next
        print("Data is not present in linked list")


linkList = LinkedList()
linkList.insert_At_begain(10)
linkList.insert_At_begain(20)
linkList.insert_At_begain(30)
linkList.insert_At_begain(40)
linkList.insert_At_begain(50)

linkList.display_linked_list()
print("-" * 40)
linkList.search_linked_list(40)