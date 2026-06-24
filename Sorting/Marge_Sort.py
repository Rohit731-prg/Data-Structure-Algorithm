def marge(start_array, end_array):
    list = []

    i = j = 0
    print(start_array, end_array)
    while i < len(start_array) and j < len(end_array):
        if start_array[i] < end_array[j]:
            list.append(start_array[i])
            i += 1
        else:
            list.append(end_array[j])
            j += 1
            

    list.extend(start_array[i:])
    list.extend(end_array[j:])

    return list

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2

    left_array = arr[:mid]
    right_array = arr[mid:]

    left = merge_sort(left_array)
    right = merge_sort(right_array)

    return marge(left, right)


numbers = [38, 27, 43, 3, 9, 82, 10, 55]
print("Original:", numbers)
print("Sorted:  ", merge_sort(numbers))