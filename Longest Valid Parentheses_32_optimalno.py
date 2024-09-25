from collections import deque
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        maximum=0
        index = 0

        valid = []
        stack = []
        for i in range(len(s)):
            valid.append(False)
            if s[i]=="(":
                stack.append(i)
            else:
                if(len(stack))>0:
                    valid[i]=True
                    valid[stack.pop()]=True
        counter = 0
        for val in valid:
            if val:
                counter+=1
            else:
                counter=0
            if counter>maximum:
                maximum=counter


        return maximum