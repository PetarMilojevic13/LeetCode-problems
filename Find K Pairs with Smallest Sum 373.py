import heapq


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = []
        for num1 in nums1:
            for num2 in nums2:
                pair = (num1+num2,num1,num2)
                heapq.heappush(heap,pair)
        res = []
        for index in range(k):
            sumarum,n1,n2 = heapq.heappop(heap)
            res.append([n1,n2])
        return res

test = Solution()
print(test.kSmallestPairs([1,2,4,5,6],[3,5,7,9],3))
