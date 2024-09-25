import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hashmap = dict()
        sorted_hash = []
        for num in nums:
            if num not in hashmap.keys():
                hashmap[num]=1
            else:
                hashmap[num]+=1
        for h in hashmap.keys():
            sorted_hash.append((len(nums)-hashmap[h],h))
        heapq.heapify(sorted_hash)
        print(sorted_hash)
        counter = 0
        result=[]
        while counter<k and len(sorted_hash)>0:
            cnt,num = heapq.heappop(sorted_hash)
            result.append(num)
            counter+=1
        return result

