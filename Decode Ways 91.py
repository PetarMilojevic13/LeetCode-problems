class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        if s[0]=="0" or s=="":
            return 0

        dp = {len(s):1}
        for index in range(len(s)-1,-1,-1):

            if s[index]!="0":
                dp[index]=dp[index+1]

                if index<len(s)-1 and s[index]!="0" and (s[index]=="1" or (s[index]=="2" and s[index+1] in "0123456")):
                    dp[index]+=dp[index+2]

            else:
                dp[index]=0
        return dp[0]


test = Solution()
print(test.numDecodings("1201234"))