def reverse_str(str):
    for i in range(0, (int(len(str)/2))):
        temp = str[i]
        count = len(str) - i - 1
        last = str[count]
        str[i] = last
        str[count] = temp
    return str
