class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows = len(matrix)
        columns = len(matrix[0])

        left = 0
        right = rows*columns - 1

        while left<=right:
            mid = (left+right)//2
            row = mid//columns
            column = mid%columns
            if matrix[row][column]==target:
                return True
            if matrix[row][column]<target:
                left=mid+1
            else:
                right=mid-1

        return False