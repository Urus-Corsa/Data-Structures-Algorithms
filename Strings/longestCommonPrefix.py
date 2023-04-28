#LC 14
def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]
        shortest = min(strs)
        for elem in strs:
            if elem.startswith(shortest):
                  continue
            else:
                  for j in range(len(shortest)):
                        if elem.startswith(shortest[0 :-1-j]):
                              shortest = shortest[0 :-1-j]
                              break
                        
            continue
        return shortest