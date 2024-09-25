class Solution(object):

    def formNumber(self,str,length):

        starting_index = len(str)-1

        first=True
        res = ""
        while starting_index>=0:
            num = str[starting_index]
            if first:
                first=False
                if length%2==1:
                    res+=num
                else:
                    res = num + res
                    res+=num
            else:
                res = num + res
                res += num
            starting_index-=1
        return res
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """

        res = ""
        starting_index = len(n)//2
        if len(n)%2==1:
            starting_index+=1

        half = n[0:starting_index]
        print(half)

        candidates = []
        candidates.append(self.formNumber(half,len(n)))

        smaller = int(half)-1
        smaller = str(smaller)
        candidates.append(self.formNumber(smaller, len(n)))

        bigger = int(half)+1
        bigger = str(bigger)
        candidates.append(self.formNumber(bigger, len(n)))

        candidates.append(str(10**(len(n))+1))
        candidates.append(str(10 ** (len(n)-1) -1))

        min = -5
        res = ""

        for num in candidates:
            num_int = int(num)
            if num_int==int(n):
                continue

            difference = abs(num_int-int(n))
            if res=="":
                res = num
                min = difference
            elif difference==min and num_int<int(res):
                res = num
                min = difference
            elif difference<min:
                res=num
                min = difference
        return res





test = Solution()
test.nearestPalindromic("10")