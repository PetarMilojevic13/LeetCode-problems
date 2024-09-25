from collections import defaultdict
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sums = defaultdict(int)
        sums[0] = 1
        current_sum = 0
        counter = 0
        for num in nums:
            current_sum += num
            counter+=sums[current_sum-k]
            sums[current_sum]+=1
        return counter