class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        left = 0
        right = len(s)-1
        res = []
        for letter in s:
            res.append(letter)

        while left<right:
            if s[left].isalpha()==False:
                left+=1
            elif s[right].isalpha()==False:
                right-=1
            else:
                tmp = res[left]
                res[left]=res[right]
                res[right]=tmp
                left+=1
                right-=1
        return "".join(res)
