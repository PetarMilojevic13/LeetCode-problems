class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(" ")
        spaces = words.count("")
        for index in range(spaces):
            words.remove("")
        res = ""
        for index in range(len(words)-1,-1,-1):
            if index<len(s)-1:
                res+=" "
            res= res + s[index]
        return s