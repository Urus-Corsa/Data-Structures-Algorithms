def gcdOfArray(nums): #finds GCD of smallest and largest elements in given array of int
    i = 0
    for i in range(nums[i]): 
        largest = max(nums) #finds largest element
        smallest = min(nums) #finds smallest element
        break
    remainder = largest%smallest  
    if remainder == 0: #base condition if smallest element itself is GCD between two elements
        return smallest 
    elif  remainder == 1: #base condition if remainder of division is 1, one is GCD 
        return 1
    else:    
        return gcdOfArray([remainder,smallest]) #recursively call gcdOfArray on remainder and smallest until base condition met

