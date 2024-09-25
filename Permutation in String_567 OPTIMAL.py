class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        if len(s1)>len(s2):
            return False

        s1_dict = dict()
        s2_dict = dict()

        for index in range(len(s1)):
            s2_dict[s2[index]] = 1 + s2_dict.get(s2[index],0)
            s1_dict[s1[index]] = 1 + s1_dict.get(s1[index], 0)
        if s2_dict==s1_dict:
            return True

        removal = 0
        for index in range(len(s2)):
            s2_dict[s2[index]] = 1 + s2_dict.get(s2[index], 0)

            s2_dict[s2[removal]]-=1
            if s2_dict[s2[removal]]:
                del s2_dict[s2[removal]]


            if s1_dict==s2_dict:
                return True
            removal+=1

        return False
