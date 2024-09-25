class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        first = len(num1)-1
        second = len(num2)-1
        carry = 0
        res = ""
        while first>=0 or second>=0:

            first_num = 0
            second_num = 0
            if first>=0:
                first_num = ord(num1[first])-ord("0")
                first-=1
            if second>=0:
                second_num = ord(num2[second])-ord("0")
                second-=1

            number = (first_num+second_num+carry)%10
            carry = (first_num+second_num+carry)//10
            res = str(number)+res
        if carry>0:
            res = str(carry)+res
        return res

test = Solution()
print(test.addStrings("911","123"))