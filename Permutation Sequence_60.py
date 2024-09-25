class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        numbers = []
        factorial_current = 1
        for index in range(1,n+1,1):
            factorial_current*=index
            numbers.append(index)
        result = []
        current_pos = k-1

        auxilliary_divider = n

        while len(result)<n-1:
            current_divider = factorial_current // len(numbers)
            factorial_current = factorial_current // auxilliary_divider
            auxilliary_divider-=1
            index = current_pos // current_divider
            current_pos = current_pos % current_divider

            result.append(numbers[index])
            numbers.pop(index)
        res = ""
        result.append(numbers.pop(0))
        for r in result:
            res+=str(r)
        return res

test = Solution()
test.getPermutation(4,9)