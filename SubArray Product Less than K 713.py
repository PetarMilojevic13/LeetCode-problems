class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        if k <= 1:
            return 0

        left = 0
        current_product = 1
        number_products = 0
        for right in range(len(nums)):
            current_product *= nums[right]
            while current_product >= k:
                current_product = current_product // nums[left]
                left += 1
            number_products += right - left + 1
        return number_products


test = Solution()
print(test.numSubarrayProductLessThanK([10,5,2,6],100))
