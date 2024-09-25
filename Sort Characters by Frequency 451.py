from collections import defaultdict
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        hashmap = defaultdict(int)
        for letter in s:
            hashmap[letter]+=1
        key_values = [(value,key) for key,value in hashmap.items()]
        for value,key in sorted(key_values,reverse=True):
            for index in range(value):
                res+=key
        return res