def factorial(n):  #factorial of number n solved by recursion
    assert int(n) == n and n >= 0, "n should only be a postive integer" #edge cases where inifinte loop occur
    if n in [0,1]: #base conditions 0!,1! = 1 
        return 1   #terminates recursion
    return n * factorial(n-1)  #calculates factorial of n by calling factorial() recursively 
                               #to calcualte n.(n-1)! til base condition satisfied 