class Sort:
    def __init__(self, lst) -> None:
        self.lst = lst

    def bubble_sort(self) -> None:
        for i in range(len(self.lst) - 1):
            for j in range(len(self.lst) - i - 1):
                if (self.lst[j] > self.lst[j + 1]):
                    self.lst[j], self.lst[j + 1] = self.lst[j + 1], self.lst[j]

        print("Sorted array: ", lst)


limit = int(input("Enter Limit: "))
lst = []
for i in range(limit):
    element = int(input("Enter Data: "))
    lst.append(element)
print("\nOriginal array: ", lst)
sort = Sort(lst);
sort.bubble_sort()