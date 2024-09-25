class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        current_direction = 0

        # 0:right,1:down,2:left,3:up

        matrix = []
        for i in range(n):
            matrix.append([])

        for i in range(n):
            for j in range(n):
                matrix[i].append(0)

        current_row = 0
        current_column = 0
        current_number = 1
        position_seen = []

        while current_number<=n*n:

            match current_direction:
                case 0:


                        #right
                        if current_column==n or (current_row,current_column) in position_seen:
                            current_direction=(current_direction+1)%4
                        else:
                            matrix[current_row][current_column]=current_number
                            current_number+=1
                            position_seen.append((current_row,current_column))
                            # right
                            if current_column == n - 1 or (current_row, current_column+1) in position_seen:
                                current_direction = (current_direction + 1) % 4
                                current_row+=1
                            else:
                                current_column+=1
                case 1:
                        #down
                        if current_row == n or (current_row, current_column) in position_seen:
                            current_direction = (current_direction + 1) % 4
                        else:

                            matrix[current_row][current_column] = current_number
                            current_number += 1
                            position_seen.append((current_row, current_column))
                            # right
                            if current_row == n - 1 or (current_row+1, current_column) in position_seen:
                                current_direction = (current_direction + 1) % 4
                                current_column -= 1
                            else:
                                current_row += 1
                case 2:
                        #left
                        if current_column == -1 or (current_row, current_column) in position_seen:
                            current_direction = (current_direction + 1) % 4
                        else:
                            matrix[current_row][current_column] = current_number
                            current_number += 1
                            position_seen.append((current_row, current_column))
                            # right
                            if current_column == 0 or (current_row, current_column-1) in position_seen:
                                current_direction = (current_direction + 1) % 4
                                current_row -= 1
                            else:
                                current_column -= 1
                case 3:
                        #up
                        if current_row == -1 or (current_row, current_column) in position_seen:
                            current_direction = (current_direction + 1) % 4
                        else:
                            matrix[current_row][current_column] = current_number
                            current_number += 1
                            position_seen.append((current_row, current_column))
                            # right
                            if current_row == 0 or (current_row-1, current_column) in position_seen:
                                current_direction = (current_direction + 1) % 4
                                current_column += 1
                            else:
                                current_row -= 1
        return matrix

test = Solution()
print(test.generateMatrix(5))