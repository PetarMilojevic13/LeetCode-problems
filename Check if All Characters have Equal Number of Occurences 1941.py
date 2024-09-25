from collections import defaultdict
class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        hashmap = defaultdict(int)
        for letter in s:
            hashmap[letter]+=1
        first = True
        number = -1
        for key in hashmap:
            if first:
                first=False
                number = hashmap[key]
            else:
                if hashmap[key]!=number:
                    return False
        return True
