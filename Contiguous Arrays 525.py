from collections import defaultdict
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash = defaultdict(int)
        current_zero = 0
        current_ones = 0
        maximum = 0

        for index in range(len(nums)):

            if nums[index]==0:
                current_zero+=1

            if nums[index]==1:
                current_ones+=1

            key = current_ones-current_zero
            if key not in hash:
                hash[key] = index



            if current_ones==current_zero:
                maximum=index+1

            elif key in hash:
                length = index - hash[key]
                if length>maximum:
                    maximum=length

        return maximum

test = Solution()
print(test.findMaxLength([0,1,0,1,1,1,0,0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,1,1,1,0,1,0,0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,1,1,0,1,1,1,1,0,1,1,0,0,0,1,1]))