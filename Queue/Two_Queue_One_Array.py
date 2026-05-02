import random as rd
from typing import List, Optional

class Queue:
    def __init__(self, limit: int) -> None:
        self.arr: List[Optional[int]] = [None] * limit
        self.front = -1
        self.rear = limit
        self.front_delete = 0
        self.rear_delete = limit - 1

    def insert1(self, num: int) -> None:
        if self.front + 1 == self.rear:
            print("Queue overflow")
            return
        self.front += 1
        self.arr[self.front] = num
        print(num, " is added into queue")

    def insert2(self, num: int) -> None:
        if self.front + 1 == self.rear:
            print("Queue overflow")
            return
        self.rear -= 1
        self.arr[self.rear] = num
        print(num, " is added into queue")

    def delete1(self):
        num = self.arr[self.front_delete]
        self.arr[self.front_delete] = None
        self.front_delete += 1
        return num
    
    def delete2(self):
        num = self.arr[self.rear_delete]
        self.arr[self.rear_delete] = None
        self.rear_delete -= 1
        return num

    def display(self):
        print("\nList: ")
        print(self.arr)

limit = int(input("Enter Array limit: "))
qu = Queue(limit)
while (True):
    list = ["1. Insert into Queue 1", "2. Insert into Queue 2", "3. Pop into Queue 1", "4. Pop into Queue 2", "5. Display", "6. Exit from Queue"]

    for i in list:
        print(i)
    ch = int(input("Enter your choice: "))
    if ch == 1:
        ele = rd.randint(11, 99)
        qu.insert1(ele)
    elif ch == 2:
        ele = rd.randint(11, 99)
        qu.insert2(ele)

    elif ch == 3:
        ele = qu.delete1()
        print("Poped element: ", ele)

    elif ch == 4:
        ele = qu.delete2()
        print("Poped element: ", ele)

    elif ch == 5:
        qu.display()
    elif ch == 6:
        print("Exit from Stack..!")
        break
    else:
        print("Enter a valid choice..!")
