class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        started = False
        res = 0
        negative = False

        max = 2**31 - 1


        for index in range(len(s)):
            char = s[index]
            if char=="-" and started==False:
                negative=True
                started = True
            elif char=="+" and started==False:
                negative=False
                started=True
            elif char==" " and started==False:
                continue
            elif char>="0" and char<="9":
                res = int(char) + res*10
                started=True
                if res>max and negative==False:
                    res=max
                if res>=max+1 and negative==True:
                    res=max+1
            else:
                break
        if negative:
            res = -res
        return res
            
