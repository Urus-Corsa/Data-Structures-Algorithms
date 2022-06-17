def fibonacci(n):
    assert n >= 0 and int(n) == n,"n should only be a positive integer" #edge cases where infinite loop occur
    if n ==0 : #first base condition, when n is 0 returns 0
        return 0
    elif n == 1 :#second base condition, when n is 1 returns 1
        return 1
    return fibonacci(n-1) + fibonacci(n-2) #recursive calls to calculate fibonacci of n by summing up fibonacci elements of n-1 and n-2    