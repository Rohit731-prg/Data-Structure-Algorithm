class Sort:
    def shell_sort(self, lst):
        n = len(lst)
        gap = n // 2

        while gap > 0:
            for i in range(gap, n):
                temp = lst[i]
                j = i

                while j >= gap and lst[j - gap] > temp:     # elements of the sub groups compair [0, 1], [2, 3] compair = 0, 2 and 1, 3
                    lst[j] = lst[j - gap]   # insert the left side element to right side
                    j -= gap    # decress by gap value not by 1

                lst[j] = temp   # because of gap value subtraction index j holds correct left side element

            gap //= 2
        return lst

lst = [22, 34, 25, 12, 64, 11, 90, 88, 45]
print("Original Array: ", lst)
sort = Sort()
result = sort.shell_sort(lst)
print("\nSorted Array: ", result)