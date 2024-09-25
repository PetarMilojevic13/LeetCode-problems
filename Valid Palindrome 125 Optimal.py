class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s)-1
        while left<right:

            if s[left].isalnum()==False:
                left+=1
            elif s[right].isalnum()==False:
                right-=1
            else:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1


        return True
