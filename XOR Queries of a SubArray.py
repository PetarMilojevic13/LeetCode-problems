class Solution(object):


    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        res = []

        prefix = [arr[0]]

        for index in range(1,len(arr)):
            prefix.append(prefix[index-1]^arr[index])

        for i in range(len(queries)):
            left = queries[i][0]
            right = queries[i][1]
            if left==right:
                res.append(arr[right])
            else:
                current_value = prefix[right]
                if left==0:
                    res.append(current_value)
                else:
                    left-=1
                    current_value = current_value ^ prefix[left]
                    res.append(current_value)



        return res

test = Solution()
print(test.xorQueries([1,3,4,8],[[0,1],[1,2],[0,3],[3,3]]))

