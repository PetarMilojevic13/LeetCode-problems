class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        open_brackets = ["(","[","{"]
        close_brackets = [")","]","}"]

        stack = []

        for bracket in s:
            if bracket in open_brackets:
                stack.append(bracket)
            else:
                try:
                    current_bracket = stack.pop()
                    index_open = open_brackets.index(current_bracket)
                    index_close = close_brackets.index(bracket)
                    if(index_open!=index_close):
                        return False
                except:
                    return False

        if len(stack)>0:
            return False
        return True