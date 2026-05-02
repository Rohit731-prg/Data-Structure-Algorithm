def partition(arr, left, right):
    pivot = arr[left]   # choose first element as pivot
    i = left + 1
    j = right

    while True:
        # move i to the right
        while i <= j and arr[i] <= pivot:
            i += 1

        # move j to the left
        while i <= j and arr[j] > pivot:
            j -= 1

        # if pointers cross, break
        if i > j:
            break

        # swap elements
        arr[i], arr[j] = arr[j], arr[i]

    # place pivot in correct position
    arr[left], arr[j] = arr[j], arr[left]

    return j   # return pivot index


def quick_sort(arr, left, right):
    if left < right:
        p = partition(arr, left, right)

        # sort left part
        quick_sort(arr, left, p - 1)

        # sort right part
        quick_sort(arr, p + 1, right)


# Driver code
arr = [15, 45, 25, 35, 85, 75, 55]
quick_sort(arr, 0, len(arr) - 1)

print(arr)