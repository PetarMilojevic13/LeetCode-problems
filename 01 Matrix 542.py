class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        seen = []
        for i in range(len(mat)):
            result.append([])
            seen.append([])
            for j in range(len(mat[0])):
                result[i].append(-1)
                seen[i].append(False)
        queue = []

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    result[i][j]=0
                    queue.append((i,j))

        while len(queue)>0:
            row,column = queue.pop(0)
            if seen[row][column]==False:
                seen[row][column]=True
                #LEFT
                if column-1>=0 and (result[row][column-1]==-1 or result[row][column-1]>result[row][column]+1) and seen[row][column-1]==False:
                    result[row][column-1]=result[row][column]+1
                    queue.append((row,column-1))
                #RIGHT
                if column+1<len(mat[0]) and (result[row][column+1]==-1 or result[row][column+1]>result[row][column]+1) and seen[row][column+1]==False:
                    result[row][column+1]=result[row][column]+1
                    queue.append((row,column+1))
                #UP
                if row-1>=0 and (result[row-1][column]==-1 or result[row-1][column]>result[row][column]+1) and seen[row-1][column]==False:
                    result[row-1][column]=result[row][column]+1
                    queue.append((row-1,column))
                #DOWN
                if row+1<len(mat) and (result[row+1][column]==-1 or result[row+1][column]>result[row][column]+1) and seen[row+1][column]==False:
                    result[row+1][column]=result[row][column]+1
                    queue.append((row+1,column))
        return result
