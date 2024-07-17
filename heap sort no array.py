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

if __name__ == "__main__":
    input_string = input("use space when inter number ")
    my_array = [int(num) for num in input_string.split()]
    heap_sort(my_array)
    print("your sort arrey: ", my_array)
