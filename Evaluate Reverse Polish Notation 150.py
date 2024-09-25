class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        ops = { '+', '-', '*',  '/'}
        stack = []

        for tok in tokens:
            if tok in ops:
                number2 = stack.pop()
                number1 = stack.pop()
                num=None
                if tok=="+":
                    num = number1+number2
                elif tok=="-":
                    num = number1 - number2
                elif tok=="*":
                    num = number1 * number2
                elif tok=="/":
                    num = abs(number1) // abs(number2)
                    if (number2<0 and number1>0) or (number2>0 and number1<0):
                        num = 0-num
                print(num)
                stack.append(int(num))
            else:
                stack.append(int(tok))
        return int(stack.pop())

