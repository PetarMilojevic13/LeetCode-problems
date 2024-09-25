class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = 0

        r=len(nums)-1
        current = 0

        while current<=r:
            if nums[current]==1:
                current+=1
            elif nums[current]==0:
                nums[current]=nums[l]
                nums[l]=0
                l+=1
                if l>current:
                    current+=1
            else:
                nums[current]=nums[r]
                nums[r]=2
                r-=1
