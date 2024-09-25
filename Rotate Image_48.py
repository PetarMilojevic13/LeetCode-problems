class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix[0])):
                tmp = matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=tmp
        for i in range(len(matrix)):
            for j in range(len(matrix[0])//2):
                tmp = matrix[i][j]
                matrix[i][j]=matrix[i][len(matrix[0])-j-1]
                matrix[i][len(matrix[0])-j-1]=tmp
        return matrix