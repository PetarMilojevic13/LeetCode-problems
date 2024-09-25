from collections import defaultdict
class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1)!=len(word2):
            return False

        hashmap1 = defaultdict(int)
        hashmap2 = defaultdict(int)

        for index in range(len(word1)):
            hashmap1[word1[index]] += 1
            hashmap2[word2[index]] += 1

        array1 = []
        array2 = []


        keys1 = set()
        keys2 = set()


        for key in hashmap1:
            array1.append(hashmap1[key])
            keys1.add(key)

        for key in hashmap2:
            array2.append(hashmap2[key])
            keys2.add(key)

        if sorted(array1)==sorted(array2) and keys1==keys2:
            return True
        return False




