from collections import defaultdict
class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        hashmap = defaultdict(int)
        for row in range(len(grid)):
            sum_tot = ""
            for column in range(len(grid)):
                sum_tot+= str(grid[row][column]) + "_"

            hashmap[sum_tot]+=1
        res = 0
        for column in range(len(grid)):
            sum_tot = ""
            for row in range(len(grid)):
                sum_tot+= str(grid[row][column]) + "_"

            if sum_tot in hashmap:
                res = res+ hashmap[sum_tot]
        return res
test = Solution()
print(test.equalPairs([[3,2,1],[1,7,6],[2,7,7]]))
