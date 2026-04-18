class QueueMomoryException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class Queue:
    def __init__(self) -> None:
        self.ls = []
        # self.front = -1
        # self.rear = -1

    def insert(self, num: int) -> None:
        # if self.front == -1:
        #     self.front += 1
        #     self.rear += 1
        #     print(self.front, self.rear)
        #     self.ls[self.front] = num
        self.ls.append(num)

    def delete_queue(self) -> int:
        # if self.rear == -1:
        #     raise QueueMomoryException("Queue Momory Empty")
        if len(self.ls) == 0:
            raise QueueMomoryException("Queue Momory Empty")
        return self.ls.pop(0)
    
    def Display_Queue(self) -> list:
        print(self.ls)
        return self.ls
    
queue = Queue()
try:
    ch = True
    while ch:
        print("\n1. Insert Element")
        print("\n2. Delete Element")
        print("\n3. Display Queue")
        print("\n4. Exit")

        ch = int(input("Enter Choise: "))

        if ch == 1:
            num = int(input("Enter Number: "))
            queue.insert(num)
        elif ch == 2:
            num = queue.delete_queue()
            print("Deleted Element: ", num)
        elif ch == 3:
            ls = queue.Display_Queue()
            print("Queue: ", ls)

        elif ch == 4:
            print("Exit from Queue..")
            ch = False
            break
        else:
            print("Invald choise")
except QueueMomoryException as e:
    print("Error: ", str(e))
except Exception as e:
    print("Error: ", str(e))