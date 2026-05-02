import random as rd
from typing import List, Optional

class Stack:
    def __init__(self, limit: int) -> None:
        self.arr: List[Optional[int]] = [None] * limit
        self.top1 = -1
        self.top2 = limit


    def insertStack1(self, num: int) -> None:
        if self.top1 + 1 == self.top2:
            print("Stack Overflow!")
            return
        self.top1 += 1
        self.arr[self.top1] = num
        print(num, " is added in Stack 1")

    def insertStack2(self, num: int) -> None:
        if self.top1 + 1 == self.top2:
            print("Stack Overflow!")
            return
        self.top2 -= 1
        print("top 2: ", self.top2)
        self.arr[self.top2] = num
        print(num, " is added in Stack 2")


    def popStack1(self):
        ele = self.arr[self.top1]
        self.arr[self.top1] = None
        return ele


    def popStack2(self):
        ele = self.arr[self.top2]
        self.arr[self.top2] = None
        return ele
    
    def display(self) -> None:
        print("\nDisplay of array:")
        print(self.arr)


limit = int(input("Enter Array limit: "))
st = Stack(limit)
while (True):
    list = ["1. Insert into Stack1", "2. Insert into Stack2", "3. Pop into Stack1", "4. Pop into Stack1", "5. Display", "6. Exit from Stack"]

    for i in list:
        print(i)
    ch = int(input("Enter your choice: "))
    if ch == 1:
        ele = rd.randint(11, 99)
        st.insertStack1(ele)
    elif ch == 2:
        ele = rd.randint(11, 99)
        st.insertStack2(ele)

    elif ch == 3:
        ele = st.popStack1()
        print("Poped element: ", ele)

    elif ch == 4:
        ele = st.popStack2()
        print("Poped element: ", ele)

    elif ch == 5:
        st.display()
    elif ch == 6:
        print("Exit from Stack..!")
        break
    else:
        print("Enter a valid choice..!")
