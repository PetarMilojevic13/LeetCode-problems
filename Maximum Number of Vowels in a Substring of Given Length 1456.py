class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = {"a","e","i","o","u"}
        number_vowels = 0
        for i in range(k):
            if s[i] in vowels:
                number_vowels+=1
        maximum = number_vowels
        for i in range(k,len(s)):
            if s[i-k] in vowels:
                number_vowels-=1
            if s[i] in vowels:
                number_vowels += 1
            if number_vowels>maximum:
                maximum=number_vowels
        return maximum