class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.numbers = nums
        self.presum = []
        current_sum = 0
        for index in range(len(nums)):
            current_sum+=nums[index]
            self.presum.append(0)
            self.presum[index]=current_sum



    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """

        sum = 0
        if left==0:
            return self.presum[right]
        else:
            sum = self.presum[right]
            sum -= self.presum[left-1]
            return sum

