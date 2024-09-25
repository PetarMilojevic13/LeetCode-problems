class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix = [nums[0]]
        current_sum = nums[0]
        for i in range(1,len(nums)):
            current_sum+=nums[i]
            prefix.append(current_sum)
        res = 0
        for i in range(len(nums)-1):
            first_sum = prefix[i]
            second_sum = prefix[len(nums)-1]-prefix[i]
            if first_sum>=second_sum:
                res+=1
        return res