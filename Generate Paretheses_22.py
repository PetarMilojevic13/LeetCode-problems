class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        stack_current = ["("]
        stack_num_brackets=[1]
        stack_num_brackets_open = [1]
        stack_currently_open=[1]
        stack_res=[]

        while len(stack_current)>0:
            current = stack_current.pop(0)
            current_num_brackts = stack_num_brackets.pop(0)
            current_num_brackets_open = stack_num_brackets_open.pop(0)
            current_open = stack_currently_open.pop(0)
            if(current_num_brackts>=n*2):
                stack_res.append(current)
            else:
                if current_num_brackets_open<n:
                    stack_current.append(current+"(")
                    stack_num_brackets.append(current_num_brackts+1)
                    stack_num_brackets_open.append(current_num_brackets_open+1)
                    stack_currently_open.append(current_open+1)
                if current_open>0:
                    stack_current.append(current + ")")
                    stack_num_brackets.append(current_num_brackts + 1)
                    stack_num_brackets_open.append(current_num_brackets_open)
                    stack_currently_open.append(current_open-1)
        return stack_res

test = Solution()
print(test.generateParenthesis(3))

