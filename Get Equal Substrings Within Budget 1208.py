class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        money_left = maxCost
        maximum = 0
        left = 0
        right = 0
        while right <len(s):
            difference = abs(ord(t[right]) - ord(s[right]))
            while difference>money_left:
                money_left+=abs(ord(t[left]) - ord(s[left]))
                left+=1

            money_left-=difference
            if right-left+1>maximum:
                maximum=right-left+1
            right+=1
        return maximum