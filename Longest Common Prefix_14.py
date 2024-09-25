class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        min =200
        prefix=""
        for i in range(len(strs)):
            if len(strs[i])<min:
                min=len(strs[i])

        for i in range(min):
            end=False
            current_letter = ""
            for j in range(len(strs)):
                if(current_letter==""):
                    current_letter=strs[j][i]
                else:
                    if strs[j][i]!=current_letter:
                        end=True
                        break
            if end:
                break
            prefix+=current_letter
        return prefix