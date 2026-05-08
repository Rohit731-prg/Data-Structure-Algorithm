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
        if self.head is None:
            print("Linked List is empty")
            raise Exception("Linked List is empty")
        temp = ptr = self.head
        while temp!= None:
            if temp.data == num:
                ptr.next = temp.next
                del temp
                return
            ptr = temp
            temp = temp.next

        


    def delete_front(self) -> int:
        if self.head is None:
            print("Linked List is empty")
            raise Exception("Linked List is empty")
        temp = self.head
        Value = temp.data
        self.head = temp.next
        del temp
        return Value

    def delete_end(self) -> int:
        if self.head is None:
            print("Linked List is empty")
            raise Exception("Linked List is empty")
        temp = ptr = self.head
        while temp.next != None:
            ptr = temp
            temp = temp.next
        Value = temp.data
        ptr.next = None
        del temp
        return Value

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
print("Deleted value from front: ", linkList.delete_front())
print("Deleted Linked List...")
linkList.display_Linked_list()
print("Deleted value from end: ", linkList.delete_end())
print("Deleted Linked List...")
linkList.display_Linked_list()