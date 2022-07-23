from array import *

array = array('i', [1,2,25,30,58,120,2585])

def traverse(arr):
    for i in range(len(arr)):
        print(arr[i])
    return "Array could not be traversed"

#traverse(array)    

array.insert(1,0)
def traverse_improved(arra):
    for i in arra:
        print(i)
    return "Array could not be traversed"

traverse_improved(array)        
 
# array.append(1) #only appends one integer at the end of array

# print(array)



# print(array)



