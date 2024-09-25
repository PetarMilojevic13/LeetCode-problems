class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        if len(s1)>len(s2):
            return False

        index_s2 = 0

        helper_first = []
        for letter in s1:
            helper_first.append(letter)
        helper = helper_first.copy()

        while index_s2<len(s2):
            if s2[index_s2] in helper:
                helping_s2 = index_s2+1
                helper.remove(s2[index_s2])
                while helping_s2<len(s2) and len(helper)>0:
                    if s2[helping_s2] not in helper:
                        break
                    helper.remove(s2[helping_s2])
                    helping_s2+=1
                if len(helper)==0:
                    return True
                if helping_s2==len(s2):
                    return False
                if s2[helping_s2] not in s1:
                    index_s2=helping_s2+1
                else:
                    index_s2 += 1
                helper = helper_first.copy()
            else:
                index_s2+=1


        return False

test = Solution()
print(test.checkInclusion("ab","eidbaooo"))