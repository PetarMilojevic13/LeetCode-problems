class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        left = 0
        right = len(s)-1
        set_vowels = {'a', 'e', 'i', 'o','u'}

        while left<right:
            while left<right and s[left].lower() not in set_vowels:
                left+=1
            if left>=right:
                break

            while left<right and s[right].lower() not in set_vowels:
                right-=1
            if left>=right:
                break
            first = s[left]
            second = s[right]
            s = s[:left] + second + s[left+1:]
            s = s[:right] + first + s[right+1:]
            left+=1
            right-=1
        return s
test = Solution()


