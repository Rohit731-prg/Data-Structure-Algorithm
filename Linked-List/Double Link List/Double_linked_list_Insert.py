from typing import Optional

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
            

    def insert_At_front(self, num):
        new_node = Node(num)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node


    def display(self):
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

print("\n\t------------Double Linked List Insert At Front----------------\n")
doubleLinkList.insert_At_front(5)
doubleLinkList.insert_At_front(0)
doubleLinkList.insert_At_front(-5)
doubleLinkList.insert_At_front(-10)
doubleLinkList.insert_At_front(-15)

doubleLinkList.display()