def power(n,e):
    assert int(e) == e, "exponent must be an integer" #edge case where the function fails
    assert (n,e) != (0,0), "zero to the power of zero is undefined"
    # if n == 0 and e == 0: #edge case where only in one combinitiation result is undefined
    #     return "zero to the power of zero is undefined"
    if e == 1: #base case of exponent = 1 to avoid indifinte recursive calls
        return n
    elif e == 0: #base case of exponent = 0 to avoid indifinte recursive calls
        return 1
    elif e > 0: #in case of positive exponent n * n^(e-1)
        return n * power(n, e-1)
    else:
        return 1/n * power(n, e+1) #in case of negative exponent 1/n * (1/n)^(e-1)
