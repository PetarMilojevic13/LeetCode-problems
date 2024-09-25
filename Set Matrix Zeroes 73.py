class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for row in range(len(matrix)):
                for column in range(len(matrix[0])):
                    if matrix[row][column]==0:

                        #Red
                        for k in range(len(matrix[0])):
                            if matrix[row][k]!=0:
                                matrix[row][k]=None
                        #Vrsta
                        for k in range(len(matrix)):
                            if matrix[k][column]!=0:
                                matrix[k][column]=None

        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if matrix[row][column]==None:
                    matrix[row][column]=0
        return matrix