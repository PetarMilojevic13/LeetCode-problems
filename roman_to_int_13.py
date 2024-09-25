class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping = {"M":1000, "D":500,"C":100,"L":50,"X":10,"V":5,"I":1}

        number = 0

        length = len(s)
        length-=1
        current= ""
        previous = ""
        while(length>=0):
            current= s[length]
            if previous=="":
                number += mapping[current]
            elif mapping[current]<mapping[previous]:
                number -= mapping[current]
            else:
                number+=mapping[current]

            previous=current
            length-=1
        return number