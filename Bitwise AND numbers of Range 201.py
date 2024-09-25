class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        current = left
        while left<=right and current>0:
            current = current & left
            left+=1
        return current