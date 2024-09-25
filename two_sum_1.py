class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index in range(len(nums)):
            first = nums[index]
            second = target-first
            if second in nums:
                if second==first and nums.count(second)>1:
                    copy_list = nums.copy()
                    copy_list.remove(first)
                    index_second = copy_list.index(second)
                    return [index,index_second+1]
                if second!=first:
                    index_second = nums.index(second)
                    return [index, index_second]

test = Solution()
print(test.twoSum([3,3],6))