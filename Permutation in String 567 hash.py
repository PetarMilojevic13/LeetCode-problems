from collections import defaultdict
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        hash1 = defaultdict(int)
        hash2 = defaultdict(int)
        for s in s1:
            hash1[s]+=1
        left = 0
        for i in range(len(s2)):
            hash2[s2[i]]+=1
            if hash1==hash2:
                return True
            if hash2[s2[i]]>hash1[s2[i]]:
                while left<=i:
                    hash2[s2[left]]-=1
                    if s2[left]==s2[i]:
                        left+=1
                        break
                    left+=1
        return False

test = Solution()
print(test.checkInclusion("ab","eidbaooo"))
