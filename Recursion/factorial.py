def factorial(n):  #factorial of number n solved by recursion
    if n == 0: #base condition 
        return 1 #terminates recursion
    x = n * factorial(n-1)  #calculates factorial of n by calling factorial() recursively 
                            #to calcualte n.(n-1)! til base condition satisfied 
    return x 
