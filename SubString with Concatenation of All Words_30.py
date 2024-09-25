class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        length = len(words[0])
        if len(s) < len(words) * length:
            return []

        count = len(s) // length

        dictionary = dict()
        for g in words:
            if g not in dictionary.keys():
                dictionary[g] = 1
            else:
                dictionary[g] += 1

        index = 0

        results = []
        stack = []

        while index < len(s):
            if len(s)-index<len(words)*length:
                break
            counter = len(words)
            word = s[index:index + length]
            stack = dictionary.copy()
            j = index + length
            if word in stack.keys():
                stack[word] -= 1
                error = False
                counter -= 1
                while counter > 0:
                    word = s[j:j + length]
                    if word not in stack.keys():
                        error = True
                        break
                    else:
                        if stack[word] <= 0:
                            error = True
                            break
                    j += length
                    stack[word] -= 1
                    counter -= 1
                if error == False:
                    results.append(index)
                index += 1
            else:
                index += 1
        return results


test = Solution()
print(test.findSubstring("barfoothefoobarman",["foo","bar"]))
