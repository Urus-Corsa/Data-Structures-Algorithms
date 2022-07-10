def largestElement (arr):
    largestElementInArr = arr[0]  #O(1)
    for i in range(1,len(arr)):   #O(n)                              O(n) time complexity of this function
        if arr[i] > largestElementInArr:  #O(1)
            largestElementInArr = arr[i]  #O(1)
    print(largestElementInArr)            #O(1)

array = [0,15,555,856852,2,1,333,5685,16461,123882,3841032,324864321,33,12558,12]
largestElement(array)

