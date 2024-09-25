class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        index = 0
        while index<len(s):
            letter = s[index]
            if letter.isalnum()==False:
                s = s[:index]+s[index+1:]
            else:
                s = s[:index] + s[index].lower() +s [index+1:]
                index+=1
        left = 0
        right = len(s)-1
        while left<right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True
