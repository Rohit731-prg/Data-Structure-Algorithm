class QueueMomoryException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class Queue:
    def __init__(self) -> None:
        self.ls = []

    def insert_at_rear(self, num: int) -> None:
        self.ls.append(num)

    def delete_at_front(self) -> int:
        if len(self.ls) == 0:
            raise QueueMomoryException("Queue Momory Empty")
        return self.ls.pop(0)
    
    def insert_at_front(self, num: int) -> None:
        self.ls.insert(0, num)

    def delete_at_rear(self) -> int:
        if len(self.ls) == 0:
            raise QueueMomoryException("Queue Momory Empty")
        return ls.pop();
    
    def Display_Queue(self) -> list:
        print(self.ls)
        return self.ls
    
queue = Queue()
try:
    ch = True
    while ch:
        print("\n1. Insert at front Element")
        print("\n2. Insert at rear Element")
        print("\n3. Delete at front Element")
        print("\n4. Delete at rear Element")
        print("\n5. Display Queue")
        print("\n6. Exit")

        ch = int(input("Enter Choise: "))

        if ch == 1:
            num = int(input("Enter Number: "))
            queue.insert_at_front(num)
        elif ch == 2:
            num = int(input("Enter Number: "))
            queue.insert_at_rear(num)
        elif ch == 3:
            num = queue.delete_at_front()
            print("Deleted Element: ", num)
        elif ch == 4:
            num = queue.delete_at_rear()
            print("Deleted Element: ", num)
        elif ch == 5:
            ls = queue.Display_Queue()
            print("Queue: ", ls)
        elif ch == 6:
            print("Exit from queue")
            ch = False
            break
        else:
            print("Invalid choise")
except QueueMomoryException as e:
    print("Error: ", str(e))
except Exception as e:
    print("Error: ", str(e))