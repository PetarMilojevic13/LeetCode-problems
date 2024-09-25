class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hashmap = dict()
        hashmap_sort = dict()
        for index in range(1,len(nums)+1):
            hashmap_sort[index] = set()
        for num in nums:
            if num not in hashmap.keys():
                hashmap[num]=1
                hashmap_sort[1].add(num)
            else:
                hashmap_sort[hashmap[num]].remove(num)
                hashmap[num]+=1
                hashmap_sort[hashmap[num]].add(num)
        current_counter = 0
        result = []
        index = len(nums)
        while current_counter<k:
            for m in hashmap_sort[index]:
                result.append(m)
                current_counter+=1
            index-=1
        return result

