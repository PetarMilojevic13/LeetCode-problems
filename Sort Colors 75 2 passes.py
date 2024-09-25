class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zeros=0
        ones=0
        twos=0

        while len(nums)>0:
            number = nums.pop(0)
            if number==0:
                zeros+=1
            if number==1:
                ones+=1
            if number == 2:
                twos += 1

        for i in range(zeros):
            nums.append(0)

        for i in range(ones):
            nums.append(1)
        for i in range(twos):
            nums.append(2)