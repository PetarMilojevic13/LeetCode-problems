from collections import defaultdict
class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        counter = defaultdict(int)
        counter[0] = 1
        current_odd = 0
        counter_res = 0
        for num in nums:
            current_odd += num%2
            counter_res += counter[current_odd-k]
            counter[current_odd]+=1


        return counter_res

