#LC 58
def lola(s: str):
    """
    :type s: str
    :rtype: int
    """
    if s.strip() == "":
        return 0
    reversed = s[::-1].strip()
    for i in range(len(reversed)):
        if reversed[i] == " ":
            return i
    return len(reversed)    


