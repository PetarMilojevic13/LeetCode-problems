class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique_nums = set(nums)
        maximum = 0
        for num in unique_nums:
            if num-1 not in unique_nums:
                current = num
                counter=0
                while current in unique_nums:
                    counter+=1
                    current+=1
                maximum = max(maximum,counter)
        return maximum
