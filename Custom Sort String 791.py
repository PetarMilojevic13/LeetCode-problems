from collections import defaultdict
class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        keys = set(s)
        hashmap = defaultdict(int)
        for letter in s:
            hashmap[letter]+=1
        res = ""
        for letter in order:
            if letter in keys:
                for i in range(hashmap[letter]):
                    res+=letter
                keys.remove(letter)
        for letter in keys:
            for i in range(hashmap[letter]):
                res += letter
        return res
