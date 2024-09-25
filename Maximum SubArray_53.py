class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maximum = nums[0]
        sum_current = nums[0]
        index = 1
        while index< len(nums):
            if nums[index]<0:
                if nums[index]>maximum:
                    maximum=nums[index]
                sum_negative = nums[index]
                index+=1
                while index<len(nums) and nums[index]<0:
                    if nums[index] > maximum:
                        maximum = nums[index]
                    sum_negative+=nums[index]
                    index+=1
                if index==len(nums):
                    break
                else:
                    if sum_negative+sum_current>=0:
                        sum_current=sum_negative+sum_current
                    else:
                        sum_current=0

            else:
                if sum_current<0:
                    sum_current=0
                sum_current+=nums[index]
                index+=1
                while index<len(nums) and nums[index]>=0 :
                    sum_current+=nums[index]
                    index+=1
                if index==len(nums):
                    if sum_current>maximum:
                        maximum=sum_current
                    break
                else:
                    if sum_current>maximum:
                        maximum=sum_current
        return maximum
