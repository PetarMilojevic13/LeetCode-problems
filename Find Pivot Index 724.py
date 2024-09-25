class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = 0
        for num in nums:
            total_sum+=num
        left = 0
        for index in range(len(nums)):
            num = nums[index]
            right = total_sum-left-num
            if left==right:
                return index
            left+=num
        return -1