import heapq

def heap(array):
    heapq.heapify(array)
    return array

arr = [40, 10, 30, 50, 20]
new_array = heap(arr)
print(new_array)