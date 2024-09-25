class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x<0:
            return False

        right = x

        if x==0:
            return True

        left = 10


        while True:
            if x//left==0:
                break
            left*=10
        left = left//10


        while right>0:
            last = right%10
            first = (x//left)%10
            if last!=first:
                return False
            right = right//10
            left = left//10

        return True