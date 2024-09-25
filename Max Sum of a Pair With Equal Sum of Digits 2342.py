from collections import defaultdict
class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = -1
        hashmap = defaultdict(int)
        for num in nums:
            num_str = str(num)
            sum_digit = 0
            for n in num_str:
                sum_digit += int(n)
            if sum_digit in hashmap:
                current_sum = num+hashmap[sum_digit]
                if current_sum>maximum:
                    maximum=current_sum
                if hashmap[sum_digit]<num:
                    hashmap[sum_digit]=num
            else:
                hashmap[sum_digit]=num
        return maximum