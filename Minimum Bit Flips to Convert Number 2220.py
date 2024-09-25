class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        difference = start ^ goal
        counter = 0
        while difference!=0:
            if difference & 1 == 1:
                counter+=1
            difference>>=1
        return counter