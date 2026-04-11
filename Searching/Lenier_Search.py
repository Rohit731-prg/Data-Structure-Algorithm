class Search:
    def __init__(self, lst) -> None:
        self.lst = lst

    def linear_search(self, target) -> bool:
        for i in range(len(self.lst)):
            if self.lst[i] == target:
                return True
            
        return False


list = []
limit = int(input("Enter the number of elements in the list: "))
for i in range(limit):
    element = int(input("Enter element: "))
    list.append(element)

target = int(input("Enter the target element: "))
search = Search(list)
result = search.linear_search(target)
if result:
    print(f"Element found in the list.")
else:
    print("Element not found in the list.")