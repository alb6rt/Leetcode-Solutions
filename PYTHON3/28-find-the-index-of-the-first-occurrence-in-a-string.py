class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        flag = 2
        for i in range(0, len(haystack)):
            if haystack[i] == needle[0]:
                flag = 0
                for j in range(1, len(needle)):
                    try:
                        if needle[j] != haystack[i + j]:
                            flag = 1
                            break
                    except(IndexError):
                        return -1
            
            if flag == 0:
                return i
        
        return -1
