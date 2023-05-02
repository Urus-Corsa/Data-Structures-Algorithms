#LC 28
def strStr(self, str1, str2):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if not str2 in str1:
            return -1
    else:
        for i in range(len(str1)):
            if str1[i] == str2[0]:
                if len(str2)+i > len(str1):
                    return -1
                if str1[i: len(str2)+i] == str2:
                    return i
