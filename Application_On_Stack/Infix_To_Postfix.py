from Postfix_Evalution import Stack as PostfixStack

class Stack:
    def __init__(self) -> None:
        self.arr = []
        self.postfix = []

        self.precedence = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
            "^": 3
        }

    def push_operator(self, ele):
        self.arr.append(ele)
    
    def push_expression(self, ele):
        self.postfix.append(ele)

    def pop(self):
        return self.arr.pop()

    def display(self):
        print("Postfix:", " ".join(self.postfix))
        re = input("Do you want to evaluate the postfix expression? (y/n): ")
        if re.lower() == "y":
            result_stack = PostfixStack()
            for i in self.postfix:
                try:
                    result_stack.push_operand(int(i))
                except ValueError:
                    result_stack.pop_operand()
                    result_stack.operation(i)
            result_stack.display()


# 🔹 MAIN
infix_expression = input("Enter the infix expression: ")
infix_expression = infix_expression.split(" ")

stack = Stack()

for i in infix_expression:

    # If number → directly add
    if i.isnumeric():
        stack.push_expression(i)

    # If '(' → push
    elif i == "(":
        stack.push_operator(i)

    # If operator
    elif i in ["+", "-", "*", "/", "^"]:

        while True:
            if len(stack.arr) == 0:
                break

            top = stack.arr[-1]

            if top == "(":
                break

            if stack.precedence[top] >= stack.precedence[i]:
                stack.push_expression(stack.pop())
            else:
                break

        stack.push_operator(i)

    # If ')'
    elif i == ")":

        while True:
            top = stack.arr[-1]

            if top == "(":
                stack.pop()   # remove '('
                break

            stack.push_expression(stack.pop())


while len(stack.arr) != 0:
    stack.push_expression(stack.pop())


stack.display()