class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1

        while left<right:
            mid = (left+right)//2
            if mid > 0 and nums[mid]<nums[mid-1]:
                return nums[mid]
            elif mid<len(nums)-1 and nums[mid]>nums[mid+1]:
                return nums[mid+1]
            else:
                if nums[mid]>nums[left] and nums[mid]>nums[right]:
                    left=mid+1
                else:
                    right=mid-1
        return nums[left]