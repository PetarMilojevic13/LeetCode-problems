class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """

        if len(original)!=m*n:
            return []

        matrix = []
        for i in range(m):
            matrix.append([])

        for index in range(len(original)):
            row = index//n
            matrix[row].append(original[index])
        return matrix

