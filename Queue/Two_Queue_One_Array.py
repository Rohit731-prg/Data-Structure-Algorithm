import random as rd

class Queue:
    def __init__(self, limit) -> None:
        self.arr = [0] * limit
        self.front1 = -1
        self.front2 = limit
        self.rear1 = -1
        self.rear2 = limit
        self.size = limit

    
    def enqueue1(self, num: int):
        if self.rear1 + 1 == self.rear2:
            print("Queue overflow")
            return
        if self.front1 == -1:
            self.front1 += 1
        self.rear1 += 1
        self.arr[self.rear1] = num
        print(num, " added into queue 1")

    def enqueue2(self, num):
        if self.rear2 - 1 == self.rear1:
            print("Queue overflow")
            return
        if self.front2 == self.size:
            self.front2 -= 1
        self.rear2 -= 1
        self.arr[self.rear2] = num
        print(num, " added into queue 2")


    def dequeue1(self):
        if self.front1 == -1:
            print("Queue underflow")
            return
        val = self.arr[self.front1]
        self.arr[self.front1] = 0
        if self.front1 == self.rear1:
            self.front1 = -1
            self.rear1 = -1
        else:
            self.front1 += 1
        return val
    

    def dequeue2(self):
        if self.front2 == self.size:
            print("Queue underflow")
            return
        val = self.arr[self.front2]
        self.arr[self.front2] = 0
        if self.front2 == self.rear2:
            self.front2 = self.size
            self.rear2 = self.size
        else:
            self.front2 -= 1
        return val
    
    def display(self):
        print("\nQueue: ", self.arr)


limit = int(input("Enter Array limit: "))
qu = Queue(limit)
while (True):
    list = ["1. Insert into Queue 1", "2. Insert into Queue 2", "3. Pop into Queue 1", "4. Pop into Queue 2", "5. Display", "6. Exit from Queue"]

    for i in list:
        print(i)
    ch = int(input("Enter your choice: "))
    if ch == 1:
        ele = rd.randint(11, 99)
        qu.enqueue1(ele)
    elif ch == 2:
        ele = rd.randint(11, 99)
        qu.enqueue2(ele)

    elif ch == 3:
        ele = qu.dequeue1()
        print("Poped element: ", ele)

    elif ch == 4:
        ele = qu.dequeue2()
        print("Poped element: ", ele)

    elif ch == 5:
        qu.display()
    elif ch == 6:
        print("Exit from Stack..!")
        break
    else:
        print("Enter a valid choice..!")