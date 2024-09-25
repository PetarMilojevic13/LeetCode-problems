class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        array_res = []
        counter = 0

        index = 0
        while index<len(nums):
            num = nums[index]
            index += 1
            while index < len(nums) and nums[index]==num:
                nums.pop(index)
        return len(nums)

test = Solution()
nums = [1,1,2]
test.removeDuplicates(nums)
print(nums)