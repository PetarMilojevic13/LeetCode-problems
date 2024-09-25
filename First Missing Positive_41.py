class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        index = 0

        while index<n:
            if nums[index]<=n and nums[index]>0 and nums[index]-1==index:
                index+=1
            elif nums[index]>n or nums[index]<=0:
                index+=1
            else:
                value = nums[index]
                if nums[value-1]!=value:

                    nums[index]=nums[value-1]
                    nums[value-1]=value
                else:
                    index+=1

        index = 0

        while index<n:
            if nums[index]-1!=index:
                return index+1
            index+=1
        return n+1

test = Solution()
print(test.firstMissingPositive([1, 1]))