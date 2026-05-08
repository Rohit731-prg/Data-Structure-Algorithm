class Stack:
    def __init__(self, limit) -> None:
        self.top_element = -1
        self.stack = []
        self.output = []
        self.limit = limit
        self.presidence = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '^': 3
        }

    def is_empty(self):
        return self.top_element == -1
    
    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]
    
    def push(self, item):
        self.top_element += 1
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        self.top_element -= 1
        self.stack.pop()

    def is_alphabet(self, char):
        return char.isalpha()

    def check_presidence(self, oper):
        top_oper = self.peek()
        if top_oper is None:
            return False
        if top_oper == "(":
            return False
        return self.presidence[top_oper] > self.presidence[oper]
    
    def infix_to_postfix(self, infix):
        for i in infix:
            if self.is_alphabet(i):
                self.output.append(i)

            elif i == "(":
                self.push(i)
            
            elif i == ")":
                while not self.is_empty() and self.peek() != "(":
                    ele = self.peek()
                    self.output.append(ele)
                    self.pop()
                self.pop()

            elif self.is_alphabet(i) == False:
                while not self.is_empty() and self.check_presidence(i):
                    ele = self.peek()
                    self.output.append(ele)
                    self.pop()
                self.push(i)

        while not self.is_empty():
            ele = self.peek()
            self.output.append(ele)
            self.pop()

    def postfix_to_prefix(self):
        prefix = self.output[::-1]
        return prefix

exp = "(A+(B*C)-D)"
reversed_exp = exp[::-1]
reversed_exp = (
    reversed_exp
    .replace("(", "#")
    .replace(")", "(")
    .replace("#", ")")
)

stack = Stack(len(reversed_exp))
stack.infix_to_postfix(reversed_exp)
prefix = stack.postfix_to_prefix()
print("".join(prefix))