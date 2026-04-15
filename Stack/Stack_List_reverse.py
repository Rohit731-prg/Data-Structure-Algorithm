class EmptyException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class Stack:
    def __init__(self) -> None:
        self.lst = []

    def length(self) -> int:
        return len(self.lst)
    
    def push(self, num) -> None:
        self.lst.insert(0, num)

    def peek(self) -> int:
        if (len(self.lst) == 0):
            raise EmptyException("Stack is Empty")
        return self.lst[0]
    
    def pop_stack(self) -> int:
        if (len(self.lst) == 0):
            raise EmptyException("Stack is Empty")
        return self.lst.pop(0)
    

stack = Stack()
ch = True
while ch:
    try:
        print("1. Insert into Stack.")
        print("2. Delete into Stack.")
        print("3. See Top Element.")
        print("4. See length of the stack.")
        print("5. Exit")

        ch = int(input("Enter Choice: "))
        if ch == 1:
            element =  int(input("Enter data: "))
            stack.push(element)
        elif ch == 2:
            ele = stack.pop_stack()
            print(ele, " has beed removed")
        elif ch == 3:
            ele = stack.peek()
            print("Top element is: ", ele)
        elif ch == 4:
            length = stack.length()
            print("Length of the stack: ", length)
        elif ch == 5:
            print("Exit from stack")
            ch = False
        else:
            print("Invalid choice...!")
    except EmptyException as e:
        print(e)
    except Exception as e:
        print(str(e))