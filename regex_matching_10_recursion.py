class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p)==0 :
            return s==""

        first_match = False
        if len(s)>0 and p[0] in {s[0],"."}:
                first_match=True

        if (len(p)>=2 and p[1]=="*"):
            return self.isMatch(s,p[2:]) or (first_match and self.isMatch(s[1:],p))
        else:
            return first_match and self.isMatch(s[1:],p[1:])

test = Solution()
print(test.isMatch("aaaaaaaaaaaaaaaaaaab","a*a*a*a*a*a*a*a*a*a*"))