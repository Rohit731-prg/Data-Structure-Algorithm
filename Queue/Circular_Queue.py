class Queue:

    def __init__(self, limit):
        self.arr = [0] * limit
        self.limit = limit
        self.front = -1
        self.rear = -1
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.limit

    def enqueue(self, num):

        if self.is_full():
            print("Queue is full")
            return

        if self.front == -1:
            self.front = 0

        self.rear = (self.rear + 1) % self.limit
        self.arr[self.rear] = num
        self.size += 1

    def dequeue(self):

        if self.is_empty():
            print("Queue is empty")
            return

        value = self.arr[self.front]
        self.arr[self.front] = 0

        # last element
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.limit

        self.size -= 1

        return value

    def display(self):
        print("Queue:", self.arr)


qu = Queue(3)

qu.enqueue(10)
qu.enqueue(30)
qu.enqueue(50)

qu.display()

print("----------------")

print("Delete element", qu.dequeue())
print("Delete element", qu.dequeue())

qu.display()

print("----------------")

qu.enqueue(80)
qu.display()
print("Delete element", qu.dequeue())