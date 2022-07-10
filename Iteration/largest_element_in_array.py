def largestElement (arr):
    largestElementInArr = arr[0]  #O(1)
    for i in range(1,len(arr)):   #O(n)                    O(n) time complexity of function
        if arr[i] > largestElementInArr:  #O(1)
            largestElementInArr = arr[i]  #O(1)
    print(largestElementInArr)            #O(1)



