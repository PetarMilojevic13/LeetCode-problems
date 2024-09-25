class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = len(board)
        column = len(board[0])
        grids = (rows*column)//9

        sets_row = []
        sets_column = []
        sets_grids = []

        for i in range(rows):
            sets_row.append(set())
        for i in range(column):
            sets_column.append(set())
        for i in range(grids):
            sets_grids.append(set())

        for index in range(rows*column):
            row_index = index//column
            column_index = index%column
            number = board[row_index][column_index]
            row_grid = row_index//3
            column_grid = column_index//3
            grid_index = row_grid*3+column_grid
            if number!=".":
                if (number in sets_row[row_index]) or (number in sets_column[column_index]) or (number in sets_grids[grid_index]):
                    return False
                else:
                    sets_row[row_index].add(number)
                    sets_column[column_index].add(number)
                    sets_grids[grid_index].add(number)
        return True

