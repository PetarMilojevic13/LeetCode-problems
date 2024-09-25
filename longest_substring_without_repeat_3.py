class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = ""
        best = 0
        for index in range(len(s)):
            char = s[index]
            if char in res:
                if len(res)>best:
                    best=len(res)
                removal_index = res.find(char)
                res = res[removal_index+1::]
                res+=char
            else:
                res+=char
        if len(res)>best:
            best=len(res)
        return best

