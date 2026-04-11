class Search:
    def __init__(self, lst) -> None:
        self.lst = lst

    def binary_search(self, target) -> bool:
        left = 0
        right = len(self.lst) - 1

        while left <= right:
            mid = (left + right) // 2

            if self.lst[mid] == target:
                return True
            
            elif self.lst[mid] < target:
                left = mid + 1
            
            else:
                right = mid - 1
        
        
        return False

    

limit = int(input("Enter the number of elements in the list: "))
list = []
for i in range(limit):
    element = int(input("Enter element: "))
    list.append(element)

target = int(input("Enter the target element: "))
list = sorted(list)
search = Search(list)
result = search.binary_search(target)
if result:
    print("Element found in the list.")
else:
    print("Element does not found in the list.")