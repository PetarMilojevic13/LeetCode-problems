# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def spiralMatrix(self, m, n, head):
        """
        :type m: int
        :type n: int
        :type head: Optional[ListNode]
        :rtype: List[List[int]]
        """

        direction = 0
        matrix = []
        for i in range(m):
            matrix.append([])
            for j in range(n):
                matrix[i].append(-1)

        current_node = head
        current_row = 0
        current_column = 0
        total_counter = 0
        seen_field = set()
        while total_counter<m*n and current_node!=None:
            print(matrix)
            match direction:
                case 0:
                    #RIGHT
                    if current_column==n or (current_row,current_column) in seen_field:
                        current_row+=1
                        direction+=1
                    else:
                        matrix[current_row][current_column] = current_node.val
                        seen_field.add((current_row,current_column))
                        current_node = current_node.next
                        total_counter+=1
                        if current_column==n-1 or (current_row,current_column+1) in seen_field:
                            direction+=1
                            current_row+=1
                        else:
                            current_column+=1
                case 1:
                    #DOWN
                    if current_row ==m or (current_row, current_column) in seen_field:
                        current_column -= 1
                        direction += 1
                    else:
                        matrix[current_row][current_column] = current_node.val
                        seen_field.add((current_row, current_column))
                        current_node = current_node.next
                        total_counter += 1
                        if current_row == m-1 or (current_row+1, current_column) in seen_field:
                            direction += 1
                            current_column -= 1
                        else:
                            current_row += 1
                case 2:
                    #LEFT
                    if current_column == -1 or (current_row, current_column) in seen_field:
                        current_row -= 1
                        direction += 1
                    else:
                        matrix[current_row][current_column] = current_node.val
                        seen_field.add((current_row, current_column))
                        current_node = current_node.next
                        total_counter += 1
                        if current_column == 0 or (current_row, current_column-1) in seen_field:
                            direction += 1
                            current_row -= 1
                        else:
                            current_column -= 1
                case 3:
                    #UP
                    if current_row == -1 or (current_row, current_column) in seen_field:
                        current_column += 1
                        direction = 0
                    else:
                        matrix[current_row][current_column] = current_node.val
                        seen_field.add((current_row, current_column))
                        current_node = current_node.next
                        total_counter += 1
                        if current_row == 0 or (current_row-1, current_column) in seen_field:
                            direction = 0
                            current_column += 1
                        else:
                            current_row -= 1
        return matrix

