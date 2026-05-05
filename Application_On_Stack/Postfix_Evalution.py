import math

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
        if operator == "+":
            self.stack.append(self.oper2 + self.oper1)
        elif operator == "-":
            self.stack.append(self.oper2 - self.oper1)
        elif operator == "*":
            self.stack.append(self.oper2 * self.oper1)
        elif operator == "/":
            self.stack.append(self.oper2 // self.oper1)
        elif operator == "^":
            self.stack.append(self.oper2 ** self.oper1)

    def display(self):
        print(self.stack[0])


if __name__ == "__main__":
    expression = input("Enter the expression: ")
    expression = expression.split(" ")
    stack = Stack()
    for i in expression:
        try:
            stack.push_operand(int(i))
        except ValueError:
            stack.pop_operand()
            stack.operation(i)
    stack.display()