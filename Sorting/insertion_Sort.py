class Sort:
    def insertion_sort(self, lst):
        n = len(lst)

        for i in range(1, n):
            key = lst[i]
            j = i - 1

            while j >= 0 and lst[j] > key:
                lst[j + 1] = lst[j]
                j -= 1

            lst[j + 1] = key
    

lst = [15, 45, 35, 55, 25, 85, 65]
sort = Sort()
print("Original Array: ", lst)
sort.insertion_sort(lst)
print("\nSorted array: ", lst)