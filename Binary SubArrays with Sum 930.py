from collections import defaultdict
class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        prefix = []
        total_sum = 0
        for num in nums:
            total_sum+=num
            prefix.append(total_sum)
        hashmap = defaultdict(int)
        hashmap[0]=1
        res = 0
        for pref in prefix:
            second = pref-goal
            if second in hashmap:
                res+=hashmap[second]
            hashmap[pref]+=1
        return res

test = Solution()
print(test.numSubarraysWithSum([1,0,1,0,1],2))