class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        count = 0
        for word in words:
            error = False
            for letter in word:
                if letter not in allowed:
                    error=True
                    break
            if error==False:
                count+=1
        return count