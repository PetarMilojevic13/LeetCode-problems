class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if(p=="*"):
            return True
        p_index = 0
        preceding_char = ""
        index = 0
        start_star = -1
        while index<len(s) and p_index<len(p):
            p_char = p[p_index]
            if not (p_index<len(p)-1 and p[p_index+1]=="*"):
                if p_char=="*":
                    preceding_char = p[p_index-1]
                    fail = False
                    while (index < len(s)):
                        if preceding_char==".":
                            index+=1
                        else:
                            if s[index]!=preceding_char:
                                break
                            else:
                                index+=1
                    if(index<len(s)):
                        p_index += 1
                    else:
                        if(p_index<len(p)-1):
                            break
                        else:
                            p_index+=1
                            break

                elif p_char==".":
                    p_index+=1
                    index += 1
                else:
                    if p_char!=s[index]:
                        return False
                    p_index += 1
                    index += 1
            else:
                p_index+=1


        if (index<len(s)):
            return False
        if p_index<len(p) and index>=len(s) and p[p_index]=="*":
            index = len(s)-1
            p_index = len(p)-1
            while p[p_index]!="*":
                if p[p_index]==".":
                    p_index-=1
                    index-=1
                elif p[p_index]==s[index]:
                    p_index -= 1
                    index -= 1
                else:
                    return False
        elif p_index<len(p):
            return False
        return True

test = Solution()
print(test.isMatch("aaa","a*a"))