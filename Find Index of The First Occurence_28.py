class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        index = 0
        while index<len(haystack):
            if haystack[index]!=needle[0]:
                index+=1
            else:
                index_needle = 1
                helper = index+1
                while index_needle<len(needle) and helper<len(haystack):
                    if needle[index_needle]!=haystack[helper]:
                        break
                    else:
                        index_needle+=1
                        helper+=1
                if index_needle<len(needle):
                    index+=1
                else:
                    return index
        return -1
