class Solution(object):
    def repeatedStringMatch(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        counter = 1

        if b=="":
            return 0

        for letter in b:
            if letter not in a:
                return -1


        string = a
        while counter<len(b) and b not in string:
            string +=a
            counter+=1
        if b in string:
            return counter
        return -1