class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        left = 0
        right = len(nums)-1
        index = -1
        mid=-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid]==target:
                index=mid
                break
            else:
                if nums[mid]>target:
                    right=mid-1
                else:
                    left=mid+1

        if index==-1:
            return [-1,-1]

        mid_left = mid
        left_right = mid-1
        left_left = left

        if mid_left>0 and nums[mid_left-1]==target:
            while mid_left>0  and left_left<=left_right:
                mid_left = (left_left+left_right)//2
                if nums[mid_left]==target:
                    if mid_left==0 or nums[mid_left-1]!=target:
                        break
                    else:
                        left_right=mid_left-1
                else:
                    left_left = mid_left+1

        mid_right = mid
        right_right = right
        right_left = mid+1

        if mid_right<len(nums)-1 and nums[mid_right+1]==target:

            while mid_right<len(nums)-1 and right_left<=right_right:
                mid_right = (right_left+right_right)//2
                if nums[mid_right]==target:
                    if mid_right==len(nums)-1 or nums[mid_right+1]!=target:
                        break
                    else:
                        right_left = mid_right + 1
                else:
                    right_right=mid_right-1

        return [mid_left,mid_right]

test = Solution()
print(test.searchRange([0,0,1,1,1,2,2,3,3,3,4,4,4,4,5,5,6,6,6,8,10,10],4))