class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n<=0:
            return False

        number = n


        while number>1:
            if number%2==1:
                return False
            number = number//2
        return True

test = Solution()
test.isPowerOfTwo(16)