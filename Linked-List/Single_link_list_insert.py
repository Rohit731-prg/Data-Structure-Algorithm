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

    def insert_At_start(self, num):
        node = Node(num)
        node.next = self.head
        self.head = node

    def insert_At_middle(self, num, poss):
        node = Node(num)
        temp = self.head

        while temp != None:
            if temp.data == poss:
                node.next = temp.next
                temp.next = node
                return
            temp = temp.next
        

    def display_Linked_list(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next


linkList = LinkList()
linkList.insert_At_end(10)
linkList.insert_At_end(20)
linkList.insert_At_end(30)

linkList.display_Linked_list()
print("\t\n-------------------------\n")
linkList.insert_At_start(40)
linkList.insert_At_start(50)

linkList.display_Linked_list()

linkList.insert_At_middle(80, 40)
print("\t\n-------------------------\n")
linkList.display_Linked_list()