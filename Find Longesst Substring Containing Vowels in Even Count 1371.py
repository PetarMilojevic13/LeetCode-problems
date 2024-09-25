class Solution(object):
    def findTheLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        vowels = {"a","e","i","o","u"}
        current_len = 0
        maximum = 0
        mask = 0
        hashmap={0:-1}

        index = 0
        while index<len(s):
            letter = s[index]
            if letter in vowels:
                if letter=="a":
                    mask = mask ^ 1
                if letter=="e":
                    mask = mask ^ 2
                if letter=="i":
                    mask = mask ^ 4
                if letter=="o":
                    mask = mask ^ 8
                if letter=="u":
                    mask = mask ^ 16
            if mask not in hashmap.keys():
                hashmap[mask]=index
            current_len = index-hashmap[mask]
            maximum = max(current_len,maximum)
            index+=1
        return maximum




