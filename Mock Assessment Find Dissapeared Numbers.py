class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        length = len(nums)
        res = []
        index = 0
        while index<len(nums):
            num = nums[index]
            if num-1<index:
                tmp = nums[num-1]
                nums[index]=tmp
                nums[num-1]=num
                if num==tmp:
                    index+=1
            elif num-1==index:
                index+=1
            else:
                tmp = nums[num-1]
                nums[index]=tmp
                nums[num-1]=num
                if num==tmp:
                    index+=1
        for number in range(1,length+1,1):
            if nums[number-1]!=number:
                res.append(number)
        return res


