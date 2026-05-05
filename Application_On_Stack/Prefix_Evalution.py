class Stack:
    def __init__(self) -> None:
        self.stack = []
        self.oper1 = 0
        self.oper2 = 0

    def push_operand(self, num):
        self.stack.append(num)

    def pop_operand(self):
        ele1 = self.stack.pop()
        self.oper1 = ele1
        ele2 = self.stack.pop()
        self.oper2 = ele2

    def operation(self, operator):
        if operator == '+':
            return self.oper1 + self.oper2
        elif operator == '-':
            return self.oper1 - self.oper2
        elif operator == '*':
            return self.oper1 * self.oper2
        elif operator == '/':
            return self.oper1 // self.oper2
        elif operator == '^':
            return self.oper1 ** self.oper2

    def display(self):
        print(self.stack[0])

expression = input("Enter the expression: ")
expression = expression.split(" ")
expression.reverse()
stack = Stack()

for i in expression:
    try:
        stack.push_operand(int(i))   # works for -70, 10, 0, etc.
    except ValueError:
        stack.pop_operand()
        result = stack.operation(i)
        stack.push_operand(result)

stack.display()