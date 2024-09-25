class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        total_count = len(matrix)*len(matrix[0])

        counter = 0
        row = 0
        column = 0
        direction=0
        seen_positions = set()
        result = []
        while counter<total_count:
            counter+=1
            match direction:
                case 0:
                    #RIGHT
                    result.append(matrix[row][column])
                    seen_positions.add((row,column))
                    if column==len(matrix[0])-1 or (row,column+1) in seen_positions:
                        direction=1
                        row+=1
                    else:
                        column+=1
                case 1:
                    # DOWN
                    result.append(matrix[row][column])
                    seen_positions.add((row, column))
                    if row == len(matrix) - 1 or (row+1, column) in seen_positions:
                        direction = 2
                        column -= 1
                    else:
                        row += 1

                case 2:
                    # LEFT
                    result.append(matrix[row][column])
                    seen_positions.add((row, column))
                    if column == 0 or (row, column-1) in seen_positions:
                        direction = 3
                        row += 1
                    else:
                        column -= 1

                case 3:
                    # UP
                    result.append(matrix[row][column])
                    seen_positions.add((row, column))
                    if row == 0 or (row-1, column) in seen_positions:
                        direction = 0
                        column += 1
                    else:
                        row -= 1
        return result