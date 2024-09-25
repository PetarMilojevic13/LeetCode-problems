class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = max(nums)
        longest_subarray = 0
        index = 0
        while index<len(nums):

            if nums[index]==maximum:
                index+=1
                current_subarray = 1
                while index<len(nums) and ((maximum & nums[index])==maximum):
                    current_subarray+=1
                    index+=1

                if current_subarray>longest_subarray:
                    longest_subarray=current_subarray


            else:
                index+=1
        return longest_subarray
