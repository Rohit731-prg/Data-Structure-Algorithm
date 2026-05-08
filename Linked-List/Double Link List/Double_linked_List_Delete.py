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
print("\n\t------------Double Linked List Delete At End----------------\n")
print(doubleLinkList.delete_At_end())

print("\n\t------------Double Linked List Delete At Front----------------\n")
print(doubleLinkList.delete_At_front())

print("\n\t------------Double Linked List After Deletion----------------\n")
doubleLinkList.display()