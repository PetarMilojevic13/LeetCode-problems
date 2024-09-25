from collections import deque
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        maximum=0
        index = 0
        opened = deque()
        while index<len(s):
            if s[index]=="(":
                tracker = index+1
                error = False
                start = index
                opened.append(index)

                while tracker<len(s):
                    if s[tracker]=="(":
                        opened.append(tracker)

                    else:
                        if len(opened)==0:
                            error=True
                            break
                        else:
                            opened.pop()
                    tracker+=1
                sum_parentheses = 0
                if tracker==len(s):
                    if len(opened)>0:

                        error_place = opened.popleft()
                        sum_parentheses = error_place-start
                        index=error_place+1
                        while len(opened)>0:
                            opened.pop()
                    else:
                        sum_parentheses = tracker - start
                        index=tracker
                else:
                    sum_parentheses = tracker - start
                    index=tracker+1
                if sum_parentheses>maximum:
                    maximum=sum_parentheses

            else:
                index+=1
        return maximum