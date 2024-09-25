class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if (digits==""):
            return []
        mapping = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        array_res = [""]

        for digit in digits:
            digit=int(digit)
            length = len(array_res)
            for i in range(length):
                current = array_res.pop(0)
                for letter in mapping[digit]:
                    adding = current+letter
                    array_res.append(adding)
        return array_res

