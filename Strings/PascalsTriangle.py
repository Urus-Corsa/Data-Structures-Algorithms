#LC 118

def pascalsTrinangle(numRows: int) -> list:
    if numRows == 0:
        return [[]]
    elif numRows == 1:
        return [[1]]
    my_list = []
    for i in range(1, numRows+1):
        if i == 1:
            my_list = [[1]]
        elif i == 2:
            my_list.append([1,1])
        else:
            #if new list size is even => half + flah
            if i%2 == 0: 
                prev_list = my_list[i-2]
                half_prev_list = prev_list[:len(prev_list)//2+1]
                new_list = [1, i-1]
                for j in range(1,len(half_prev_list)):
                    if j+1>=len(half_prev_list):
                        break
                    new_list.append(half_prev_list[j]+half_prev_list[j+1])
                reversed_list = new_list[::-1]
                new_list.extend(reversed_list)
                my_list.append(new_list)
            # new list size is not even => half + Lah
            else:
                prev_list = my_list[i-2]
                half_prev_list = prev_list[:len(prev_list)//2+1]
                new_list = [1, i-1]
                for j in range(1, len(my_list)):
                    if j+1>=len(half_prev_list):
                        break
                    new_list.append(half_prev_list[j]+half_prev_list[j+1])
                reversed_list = new_list[::-1]
                reversed_list.pop(0)
                new_list.extend(reversed_list)
                my_list.append(new_list)
    return my_list