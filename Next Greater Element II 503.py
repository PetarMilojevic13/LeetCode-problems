class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #STACK



        stack = []
        counter = 0
        res = []
        index = 0
        for i in range(len(nums)):
            res.append(-1)
        total = 0

        while counter<len(nums) and total<2*len(nums):

            while True:
                if len(stack)==0 or nums[index]<=stack[len(stack)-1][0]:
                    break
                number,ind = stack.pop()
                res[ind] = nums[index]

            stack.append((nums[index],index))
            index+=1
            total+=1
            index = index % len(nums)
        return res