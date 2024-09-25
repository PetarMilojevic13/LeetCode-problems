class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        current = 1

        current_length= n
        current_difference = 1

        left = True

        while current_length>1:
            if left:
                current+=current_difference
                current_difference=current_difference*2
                current_length=current_length//2
                left=False
            else:
                if current_length%2==1:
                    current+=current_difference
                current_difference = current_difference * 2
                current_length = current_length // 2
                left = True
        return current

test = Solution()
print(test.lastRemaining(9))