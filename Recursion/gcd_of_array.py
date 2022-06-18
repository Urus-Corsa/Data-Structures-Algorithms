def gcdOfArray(nums):
    i = 0
    for i in range(nums[i]):
        largest = max(nums)
        smallest = min(nums)
        break
    remainder = largest%smallest 
    if remainder == 0:
        return smallest
    elif  remainder == 1:
        return 1
    else:    
        return gcdOfArray([remainder,smallest])

