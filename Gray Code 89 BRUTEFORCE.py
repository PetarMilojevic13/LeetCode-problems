class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        visited = set()
        visited.add(0)
        res = [0]
        length = 2**n
        for i in range(1,length):
            for x in range(n):
                if ((1<<x)^res[-1] not in visited):
                    visited.add((1<<x)^res[-1])
                    res.append((1<<x)^res[-1])
                    break
        return res
