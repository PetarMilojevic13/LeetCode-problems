class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 0
        max_divider = n//2
        while n%max_divider!=0:
            max_divider-=1

        quotient = n//max_divider
        return quotient + self.minSteps(max_divider)