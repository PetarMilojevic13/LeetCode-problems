#LAKSE JE U JAVI JER SU INT 32 BITA

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        res = 0

        res = a
        y = b
        mask = 0xffffffff
        while y!=0:
            carry = (res & y) << 1
            res = res ^ y
            y = carry
            y = y & mask
        return res

test = Solution()
print(test.getSum(-1,1))