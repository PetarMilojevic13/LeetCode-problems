from collections import defaultdict
class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        hashmap = defaultdict(int)
        for array in nums:
            for num in array:
                hashmap[num]+=1
        length = len(nums)
        res = []
        for key in sorted(hashmap):
            if hashmap[key]==length:
                res.append(key)
        return res