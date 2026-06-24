class Stack:
    def __init__(self) -> None:
        self.stack_exp = []

    def push(self, exp):
        self.stack_exp.append(exp)

    def top(self):
        return self.stack_exp.pop()
    
    def application(self, exp):
        if exp in "[{(":
            self.push(exp)
        elif exp in ")}]":
            if not self.stack_exp:
                return False
            
            last_ele = self.top()
            
            if ((exp == ")" and last_ele != "(") or (exp == "}" and last_ele != "{") or (exp == "]" and last_ele != "[")):
                return False
            
            return True
            


            
stack = Stack()
exp = '{[(a+b)*c]}'
re = True
for i in exp:
    re = stack.application(i)

if re and not stack.stack_exp:
    print("Balenced")
else:
    print("Not Balence")