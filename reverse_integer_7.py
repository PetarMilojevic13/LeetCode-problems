class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        number = x
        min = 0 - 2**31
        max = 2**31 - 1
        res=0
        end = abs(number)
        while end>0:
            if(x<0):
                old = res
                res = res * 10 - end % 10
                if res<min:
                    return 0
                number = abs(number) // 10
                number = -number
            else:
                old = res
                res = res*10 + number%10
                if res>max:
                    return 0
                number = abs(number) // 10
            end=end//10

        return res

test = Solution()
print(test.reverse(-123))