from collections import defaultdict
class Solution(object):
    def rearrangeCharacters(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: int
        """
        hash = defaultdict(int)
        for letter in s:
            hash[letter]+=1
        res = 0
        while True:
            end = False
            for letter in target:
                if hash[letter]>0:
                    hash[letter]-=1
                else:
                    end=True
                    break
            if end:
                break
            res+=1
        return res