class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        number = ""
        for n in s:
            num = ord(n)-96
            number+=str(num)

        current = number
        index = 0
        while index<k:
            sum=0
            for num in current:
                sum+=int(num)
            current=str(sum)
            index+=1
        return int(current)
