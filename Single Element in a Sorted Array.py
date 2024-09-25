class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left<right:
            mid = (left+right)//2
            if mid==0:
                return nums[0]
            if mid==len(nums)-1:
                return nums[mid]
            if nums[mid-1]!=nums[mid] and nums[mid+1]!=nums[mid]:
                return nums[mid]
            left_count = mid-left
            right_count = right-mid
            if nums[mid-1]==nums[mid]:
                left_count-=1
            else:
                right_count-=1
            if left_count%2==1:
                if nums[mid-1]==nums[mid]:
                    right=mid-2
                else:
                    right=mid-1
            else:
                if nums[mid+1]==nums[mid]:
                    left=mid+2
                else:
                    left=mid+1
        return nums[left]