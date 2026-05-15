from typing import Optional

from httpx import head

class Node:
    def __init__(self, num: int) -> None:
        self.data = num
        self.next: Optional[Node] = None
        self.prev: Optional[Node] = None

class DoubleLinkList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def insert_At_end(self, num):
        new_node = Node(num)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node # pyright: ignore
            new_node.prev = self.tail
            self.tail = new_node

    def delete_At_end(self):
        if self.head is None or self.tail is None:
            print("List is empty")
            raise Exception("List is empty")
        value = self.tail.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
            del self.tail

        else:
            temp = self.tail
            value = temp.data
            prev_node = self.tail.prev
            if prev_node is not None:
                prev_node.next = None
                self.tail = prev_node
                del temp
        return value
        

    def delete_At_front(self):
        if self.head is None or self.tail is None:
            print("List is empty")
            raise Exception("List is empty")
        value = self.head.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
            del self.tail
        else:
            temp = self.head
            value = temp.data
            next_node = self.head.next
            if next_node is not None:
                next_node.prev = None
                self.head = next_node
                del temp
        return value


    def delete_At_middle(self, num):
        if self.head == None:
            print("List is empty")
            return
        temp = self.head
        while temp.data != num and temp != None: # type: ignore
            temp = temp.next
        
        if temp is None:
            print("Value not found")
            return
        value = temp.data
        pre = temp.prev
        pre.next = temp.next # type: ignore
        nex = temp.next
        nex.prev = temp.prev # type: ignore
        del temp
        return value
    

    def delete_At_middle_node(self):
        if self.head is None:
            print("List is empty")
            return
        p1 = p2 = self.head
        while p2 is not None and p2.next is not None and p2.next.next is not None:
            p1 = p1.next # type: ignore
            p2 = p2.next.next
        if p1 is None:
            return
        Value = p1.data
        p1.prev.next = p1.next # type: ignore
        p1.next.prev = p1.prev # type: ignore
        del p1
        return Value

    def display(self):
        if self.head is None or self.tail is None:
            print("List is empty")
            raise Exception("List is empty")
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next


doubleLinkList = DoubleLinkList()
print("\n\t------------Double Linked List Insert At End----------------\n")
doubleLinkList.insert_At_end(10)
doubleLinkList.insert_At_end(20)
doubleLinkList.insert_At_end(30)
doubleLinkList.insert_At_end(40)
doubleLinkList.insert_At_end(50)

doubleLinkList.display()

print("\n\t------------Double Linked List Delete At middle----------------\n")
print(doubleLinkList.delete_At_middle_node())

print("\n\t------------Double Linked List Delete At given value----------------\n")
print(doubleLinkList.delete_At_middle(40))

print("\n\t------------Double Linked List Delete At End----------------\n")
print(doubleLinkList.delete_At_end())

print("\n\t------------Double Linked List Delete At Front----------------\n")
print(doubleLinkList.delete_At_front())

print("\n\t------------Double Linked List After Deletion----------------\n")
doubleLinkList.display()