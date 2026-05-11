class Queue:
    def __init__(self, limit: int) -> None:
        self.arr = [None] * limit
        self.limit = limit
        self.rear = -1
        self.front = -1
        self.size = 0

    def is_empty(self):
        return self.front == -1 and self.rear == -1
    
    def is_full(self):
        return self.size == self.limit
    
    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return
        return self.arr[self.front]

    def push(self, num):
        if self.is_full():
            print("Queue is full")
            return
        self.rear = (self.rear + 1) % self.limit
        self.arr[self.rear] = num
        self.size += 1

    def pop(self):
        if self.is_empty():
            print("Queue is Empty")
            return
        val = self.arr[self.front]
        self.front += 1
        self.arr[self.front] = None
        self.size -= 1

    def display(self):
        print("Queue: ", self.arr)


qu = Queue(3)
qu.push(10)
qu.push(30)
qu.push(50)

qu.display()
print("------------------\n\n")
qu.pop()
qu.display()
print("------------------\n\n")

qu.push(80)
qu.display()