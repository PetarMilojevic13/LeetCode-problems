class Solution(object):

    def RLU(self,number):

        if number==1:
            return "1"

        string_number = self.RLU(number-1)
        string_number = str(string_number)
        index = 0
        res=""
        while index<len(string_number):
            num = string_number[index]
            index+=1
            counter=1
            while index<len(string_number) and string_number[index]==num:
                index+=1
                counter+=1
            res+=str(counter)
            res+=num
        return res+""

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        return self.RLU(n)

test = Solution()
test.countAndSay(4)