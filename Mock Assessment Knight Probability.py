from collections import deque
class Solution(object):
    def knightProbability(self, n, k, row, column):

        """
        :type n: int
        :type k: int
        :type row: int
        :type column: int
        :rtype: float
        """
        if n<1 or n>25:
            return 0.0
        if k==0:
            return 1.0



        total_number = 8**k

        move_counter = 0
        moves = deque()
        moves.append((row,column,0))

        directions = [(-2,-1),(-1,-2),(-2,1),(-1,2),(1,-2),(2,-1),(2,1),(1,2)]
        counter = float(0)
        while len(moves)>0:
            length = len(moves)
            cnt = 0
            while cnt<length:
                field = moves.popleft()
                r = field[0]
                c = field[1]
                m_c = field[2]
                if field[2]<k:


                    for direct in directions:
                        ro = r+direct[0]
                        co = c+direct[1]


                        if ro>=0 and ro<n and co>=0 and co<n:
                            moves.append((ro,co,m_c+1))
                else:
                    counter= counter + float(1)




                cnt+=1
            move_counter+=1
            if len(moves)==0:
                break



        total_number = float(total_number)


        num = float(counter/total_number)
        return num




