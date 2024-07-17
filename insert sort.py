import time
start=time.time()
def insertionSort(arr): 
   
    for i in range(1, len(arr)): 
   
        key = arr[i] 
   
        j = i - 1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key

#main

if __name__ == '__main__':
    arr = [50,48,49,47,45,46,44,42,41,43,40,38,39,37,35,36,34,32,31,30,29,27,28,25,26,24,21,23,22,20,91,17,18,15,14,16,18,17,11,12,10,9,7,8,5,4,6,3,1,2] 
    insertionSort(arr) 
    print ("Sorted array is:") 
    print (arr)
    print('time',(time.time() - start))

    

    
