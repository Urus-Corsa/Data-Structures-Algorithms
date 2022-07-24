from matplotlib.pyplot import axis
import numpy as np

# initialzing and inserting values at declaration of 2D array 
# O(1) time complexity, O(n) if declared then populated 
# O(n*m) space complexity(n=rows, m=columns)
dosD_array = np.array([[1,2,3], [4,5,6], [7,8,9]])


# insertion in 2D array indicating(initial array, index, array to insert, axis 0=row 1=column) 
# O(n*m) time complexity as rows and columns have to move accordingly
# O(1) space complexity
# [[11],[12],[13]] prints sequence of rows and columns of each element accordingly
# [11, 12, 13] adds this array as specified row or column at index specified
dosD_array_insert = np.insert(dosD_array, 2, [[11],[12],[13]], axis=1)

# append to end of 2D array indicating(initial array, array to insert, axis)
# only works with this format in this version of Python [[21],[22],[23]]=[21,22,23]
# time complexity O(1). Appends to end of 2D array w/o any row or column moving
# O(1) space complexity
dosD_array_append = np.append(dosD_array, [[21],[22],[23]], axis=1)


# fuction for accessing elements in 2D arrays
# len(arr)=lentgh of rows, len(arr[0])=lentgh of coloumns
# time and space complexity O(1)
def accessElement(arr, row, column):
    if row>=len(arr) or column>=len(arr[0]):    #O(1)
        return "Indices entered are not valid" #O(1)
    return arr[row][column]                 #O(1)
    

# function to traverse 2D arrays using nested loops
# for each row each column element is visited acordingly
# O(n*m) time complexity if rows = column => time complexity = O(n^2)
# O(1) space complexity
def traverse(arr):
    for i in range(len(arr)):         #O(n*m)
        for j in range(len(arr[0])):  #O(m)
            print(arr[i][j])          #O(1)


# function to search for given element in 2D arrays
# same operation as traversal given condition to return matched element indices
# O(n*m) time complexity if rows = column => time complexity = O(n^2)
# O(1) space complexity
def searchElement(arr, elem):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == elem:
                return "Element " + str(elem) + " found in row " + str(i) + " column " + str(j)
    return str(elem) + " not found in the array"


# deleting row or column of array indicating(initial array, index, axis)
# O(n*m) time complexity as rows and columns have to move accordingly 
# if deleted at end time complexity O(1). Deletes from end of array w/o any row or column moving  
# O(1) space complexity
dosD_array_delete = np.delete(dosD_array, 1, axis=1)

