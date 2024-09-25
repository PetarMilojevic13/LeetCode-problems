class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        current_sum = 0
        minimum = len(nums)+1
        counter = 0

        while True:
            while right<len(nums) and current_sum<target:
                current_sum+=nums[right]
                right+=1
                counter+=1
            if current_sum<target:
                break
            if counter<minimum:
                minimum=counter
            while left<right and current_sum>=target:
                current_sum-=nums[left]
                left+=1
                counter-=1
                if counter<minimum and current_sum>=target:
                    minimum=counter
            if counter < minimum and current_sum >= target:
                minimum = counter
            if left==len(nums):
                break


        if minimum==len(nums)+1:
            return 0
        return minimum

test = Solution()
print(test.minSubArrayLen(11,[1,1,1,1,1,1,1,1]))