class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if (numRows==1):
            return s

        matrix = []
        for i in range(numRows):
            matrix.append(list())

        down = True

        current_row = 0

        for index in range(len(s)):

            if(down):
                matrix[current_row].append(s[index])
                if(current_row==numRows-1):
                    current_row-=1
                    down=False
                else:
                    current_row+=1
            else:
                if(current_row==0):
                    matrix[current_row].append(s[index])
                    current_row+=1
                    down=True
                else:
                    matrix[current_row].append(s[index])
                    current_row-=1
        res = ""
        for i in range(numRows):
            array = matrix[i]
            for j in range(len(array)):
                res += matrix[i][j]
        return res

test = Solution()
print(test.convert("PAYPALISHIRING",3))