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
            
    
    def display_Linked_list(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next

    
    def delete_value(self, num):    # num contain the value that we need to delete from linked list
        temp = self.head
        prev = temp
        while temp != None:
            if temp.data == num:
                if prev is None:
                    self.head = temp.next
                else:
                    prev.next = temp.next
                return
            else:
                prev = temp
                temp = temp.next


linkList = LinkList()
linkList.insert_At_end(10)
linkList.insert_At_end(20)
linkList.insert_At_end(30)
linkList.insert_At_end(40)
linkList.insert_At_end(50)
print("Original Linked List...")
linkList.display_Linked_list()
linkList.delete_value(30)
print("Deleted Linked List...")
linkList.display_Linked_list()
