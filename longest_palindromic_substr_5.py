class Solution(object):

    def palindrome(self,index,even,s):

        if(even):
            if(index==0):
                return s[index]
            else:
                res = ""
                left = index - 1
                right = index
                while(True):
                    if(left<0 or right>=len(s)):
                        break
                    if s[left]!=s[right]:
                        break
                    res=s[left] + res
                    res+=s[right]
                    left-=1
                    right+=1
                if res=="":
                    return s[index]
                else:
                    return res

        else:
            res = s[index]
            left = index - 1
            right = index+1
            while (True):
                if (left < 0 or right >= len(s)):
                    break
                if s[left] != s[right]:
                    break
                res=s[left] + res
                res += s[right]
                left -= 1
                right += 1
            if res == "":
                return s[index]
            else:
                return res


    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        best = ""
        for index in range(len(s)):
            res = self.palindrome(index,True,s)
            if(len(res)>len(best)):
                best=res
            res = self.palindrome(index, False, s)
            if(len(res)>len(best)):
                best=res

        return best


