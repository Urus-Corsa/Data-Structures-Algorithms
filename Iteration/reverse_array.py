def reverse(arr):
    for i in range(0, int(len(arr)/2)):
        count = len(arr)-1-i
        temp = arr[i]
        last = arr[count]
        arr[i] = last
        arr[count] = temp
    return arr
    
def reverse_improved(arr):
    for i in range(0, int(len(arr)/2)):
        count = len(arr)-1-i
        temp = arr[i]
        arr[i]= arr[count]
        arr[count] = temp
    return arr    

