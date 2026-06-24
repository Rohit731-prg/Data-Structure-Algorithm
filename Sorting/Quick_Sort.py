def partition(arr, start, end):
    pivot = arr[start]

    i = start + 1
    j = end

    while True:
        while i <= j and arr[i] <= pivot:
            i += 1

        while i <= j and arr[j] > pivot:
            j -= 1

        if i > j:
            break

        arr[i], arr[j] = arr[j], arr[i]

    arr[start], arr[j] = arr[j], arr[start]
    return j

def quick(arr, start, end):
    if start < end:
        p = partition(arr, start, end)

        quick(arr, start, p - 1)
        quick(arr, p + 1, end)

arr = [15, 45, 25, 35, 85, 75, 55]
quick(arr, 0, len(arr) - 1)
print(arr)