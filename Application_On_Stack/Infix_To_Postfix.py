class Stack:
    def __init__(self, length: int):
        self.top_element = -1
        self.length = length
        self.stack = []
        self.output = []
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    # check if the stack is empty
    def is_empty(self):
        return self.top_element == -1
    
    def top(self):
        if self.is_empty():
            return None
        return self.stack[-1]
    
    def pop_from_stack(self):
        if self.is_empty():
            return None
        self.stack.pop()
        self.top_element -= 1

    def push_to_stack(self, item):
        self.top_element += 1
        self.stack.append(item)

    def is_alphabet(self, char):
        return char.isalpha()
    
    def check_precedence(self, operator):
        top_operator = self.top()

        if top_operator is None:
            return False
        if top_operator == "(":
            return False
        return self.precedence[top_operator] >= self.precedence[operator]
    
    def infix_to_postfix(self, infix):
        for i in infix:
            if self.is_alphabet(i):
                self.output.append(i)
            
            elif i == "(":
                self.push_to_stack(i)

            elif i == ")":
                while not self.is_empty() and self.top() != "(":
                    ele = self.top()
                    self.output.append(ele)
                    self.pop_from_stack()
                self.pop_from_stack()

            elif self.is_alphabet(i) == False:
                while not self.is_empty() and self.check_precedence(i):
                    ele = self.top()
                    self.output.append(ele)
                    self.pop_from_stack()
                self.push_to_stack(i)
        
        while self.top() is not None:
            ele = self.top()
            self.output.append(ele)
            self.pop_from_stack()

    def display(self):
        print("".join(self.output))


exp = "a+b*(c^d-e)^(f+g*h)-i"
StackObj = Stack(len(exp))
StackObj.infix_to_postfix(exp)
StackObj.display()