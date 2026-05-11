class Queue:
    def __init__(self) -> None:
        self.queue = []
        self.priority = []
        self.rear = -1

    def is_empty(self):
        return self.rear == -1
    
    def push(self, num, p):
        if self.is_empty():
            self.rear += 1
            self.queue.append(num)
            self.priority.append(p)
            return
        max = 0
        for i in range(len(self.priority)):
            if self.priority[i] > self.priority[max]:
                max = i
        self.rear += 1
        self.queue.insert(max, num)
        self.priority.insert(max, p)

    def pop(self):
        if self.is_empty():
            print("Queue is empty")
            return
        
        par = self.priority.pop(0)
        val = self.queue.pop(0)
        print("Poped element: ", val, " with priority: ", par)
    
    def display(self):
        print("Queue: ", self.queue)
        print("Priority", self.priority)


q = Queue()
q.push(10, 15)
q.push(30, 7)
q.push(80, 9)
q.push(50, 10)
q.push(90, 12)

q.display()
print("-------------------------\n\n")

q.pop()
q.pop()

q.display()
print("-------------------------\n\n")