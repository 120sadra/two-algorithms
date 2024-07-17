import time
start_time=time.time()
def heapify(arr, n, i):
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    # If left child exists and is greater than root
    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    # If right child exists and is greater than largest so far
    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    # If largest is not the root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap root with last element
        heapify(arr, i, 0)

# Example usage
if __name__ == "__main__":
    my_array = [50,48,49,47,45,46,44,42,41,43,40,38,39,37,35,36,34,32,31,30,29,27,28,25,26,24,21,23,22,20,91,17,18,15,14,16,18,17,11,12,10,9,7,8,5,4,6,3,1,2] 
    heap_sort(my_array)
    print("Sorted array:", my_array)
    print('time',time.time() - start_time)
