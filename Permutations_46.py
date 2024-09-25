class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        queue = []
        results = []
        number = len(nums)

        total_number = 1
        index = len(nums)-1
        while index>1:
            total_number*=index
            index-=1

        for num in nums:
            queue.append([num])

        while len(queue)>0:
            current = queue.pop(0)
            if len(current)==number:
                results.append(current)
            else:
                for num in nums:
                    if num in current:
                        continue
                    else:
                        tmp = current.copy()
                        tmp.append(num)
                        if tmp not in queue:
                            queue.append(tmp)

        return results
