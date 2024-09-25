class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        set_letters = set()
        for letter in s:
            if letter in set_letters:
                return letter
            set_letters.add(letter)