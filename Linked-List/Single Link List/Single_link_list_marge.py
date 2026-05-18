class Node:
    def __init__(self, data, next = None) -> None:
        self.data = data
        self.next = next


class LinkList:
    def __init__(self) -> None:
        self.head = None

    def insert_At_end(self, num):
        node = Node(num)    # the address of Node class will be return
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = node

    def marge(self, link_list):
        if self.head is None:
            self.head = link_list.head
            return
        
        temp = self.head
        while temp.next != None:
            temp = temp.next

        temp.next = link_list.head

    def display_Linked_list(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next


linkList = LinkList()
linkList.insert_At_end(10)
linkList.insert_At_end(20)
linkList.insert_At_end(30)

print("\n\t----------------List 1----------------\n")
linkList.display_Linked_list()

linkList2 = LinkList()
linkList2.insert_At_end(50)
linkList2.insert_At_end(70)
linkList2.insert_At_end(90)

print("\n\t----------------List 2----------------\n")
linkList2.display_Linked_list()

linkList.marge(linkList2)
print("\n\t----------------Marge List----------------\n")
linkList.display_Linked_list()