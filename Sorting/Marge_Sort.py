def partition(arr, start, mid, end):
    # get the size of 2 arrays
    s1 = mid - start + 1
    s2 = end - mid

    left_array = [0] * s1
    right_array = [0] * s2

    for i in range(s1):
        left_array[i] = arr[start + i]
    for j in range(s2):
        right_array[j] = arr[mid + 1 + j]

    i = j = 0
    k = start
    while i < s1 and j < s2:
        if left_array[i] > right_array[j]:
            arr[k] = right_array[j]
            j += 1
            k += 1
        else:
            arr[k] = left_array[i]
            i += 1
            k += 1
    while i < s1:
        arr[k] = left_array[i]
        i += 1
        k += 1
    while j < s2:
        arr[k] = right_array[j]
        j += 1
        k += 1
    



def Marge_Sort(arr, start, end):
    if start < end:
        mid = (start + end) // 2

        Marge_Sort(arr, start, mid)
        Marge_Sort(arr, mid + 1, end)
        partition(arr, start, mid, end)

arr = [15, 45, 25, 35, 85, 75, 55]
print("Original Array: ", arr)
print("\n\t\t---------------------------\n")
Marge_Sort(arr, 0, (len(arr) - 1))
print("Sorted Array: ", arr)