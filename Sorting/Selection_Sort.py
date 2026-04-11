class Sort:
    def selection_sort(self, lst) -> None:
        for i in range(len(lst)): # pass each ittaration
            min_val = lst[i]
            min_index = i
            for j in range(i + 1, len(lst)): # find the minimum element
                if lst[j] < min_val:
                    min_val = lst[j]
                    min_index = j

            lst[i], lst[min_index] = lst[min_index], lst[i] # swap with minimum element with last index

        print("\nSorted array: ", lst)                


limit = int(input("Enter Limit: "))
lst = []
for i in range(limit):
    element = int(input("Enter Data: "))
    lst.append(element)
print("\nOriginal array: ", lst)
sort = Sort()
sort.selection_sort(lst)