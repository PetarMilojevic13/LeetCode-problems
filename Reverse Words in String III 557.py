class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(" ")
        words_array=[]
        for word in words:
            words_array.append([])
            length = len(words_array)
            for index in range(len(word)-1,-1,-1):
                words_array[length-1].append(word[index])
        res = ""
        for index in range(len(words_array)):
            if index>0:
                res+=" "
            res+="".join(words_array[index])
        return res
