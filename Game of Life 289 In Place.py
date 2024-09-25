class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

        for m in range(len(board)):
            for n in range(len(board[0])):
                live_cnt = 0
                for d in directions:
                    row = m+d[0]
                    column = n+d[1]
                    if row>=0 and row<len(board) and column>=0 and column<len(board[0]):
                        if board[row][column] == 1 or board[row][column] == -1:
                            live_cnt+=1
                row = m
                column = n
                if board[row][column] == 1 and (live_cnt<2 or live_cnt>3):
                    board[row][column] = -1
                elif board[row][column] == 1 and live_cnt>=2 and live_cnt<=3:
                    board[row][column] = 1
                elif board[row][column] == 0 and live_cnt==3:
                    board[row][column] = 2
        print(board)
        for m in range(len(board)):
            for n in range(len(board[0])):
                if board[m][n] == 1 or board[m][n] == 2:
                    board[m][n]=1
                else:
                    board[m][n] = 0
        return board
