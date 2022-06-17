def sum_of_digits(n):
    assert int(n) == n and n >= 0, "n should be a positive integer" #edge cases including the restriction of input
    if n < 10: #base condition to avoid infinite recursive calls, if n is less than 10 it cant be divided further down
        return n
    else:
        division_tuple = divmod(n,10) #divmod(number, dividend) returns a tuple(quotient,remainder) to split the digits
        #return sum_of_digits(division_tuple[0]) + sum_of_digits(division_tuple[1]) 
        return sum_of_digits(division_tuple[0]) + int(division_tuple[1]) #recursivley call division until the digits are separated
                                                                                    # then sum up all digits
